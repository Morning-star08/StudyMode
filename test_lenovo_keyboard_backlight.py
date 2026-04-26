"""
Standalone Lenovo keyboard backlight test tool.

This does not start Study Mode and does not touch streak/session files.
It writes a small log next to this file so failed runs still leave clues.

Usage:
    python test_lenovo_keyboard_backlight.py
    python test_lenovo_keyboard_backlight.py status
    python test_lenovo_keyboard_backlight.py on
    python test_lenovo_keyboard_backlight.py off
    python test_lenovo_keyboard_backlight.py toggle
    python test_lenovo_keyboard_backlight.py diag
"""

import ctypes
import os
import sys
import time
from datetime import datetime

import win32com.client


KB_OFF = 0
KB_ON = 1
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keyboard_backlight_test.log")


def log(message):
    stamped = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    print(stamped)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as handle:
            handle.write(stamped + "\n")
    except Exception:
        pass


def is_admin():
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False


def relaunch_as_admin():
    if is_admin():
        return True
    if sys.platform != "win32":
        return True

    python_exe = sys.executable
    script_path = os.path.abspath(__file__)
    args = " ".join(f'"{arg}"' for arg in sys.argv[1:])
    inner = f'"{python_exe}" "{script_path}" {args}'.strip()
    ps = f'Start-Process -FilePath "cmd.exe" -ArgumentList \'/k {inner}\' -Verb RunAs'
    try:
        import subprocess

        subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
            check=True,
            timeout=10,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    except Exception as exc:
        log(f"Could not relaunch with administrator rights: {exc}")
        return False
    log("Opened a new administrator terminal for the test.")
    return None


def connect_wmi():
    locator = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    return locator.ConnectServer(".", "root\\wmi")


def first_instance(service, class_name):
    query_variants = [
        f"SELECT * FROM {class_name} WHERE Active = TRUE",
        f"SELECT * FROM {class_name}",
    ]
    last_error = ""
    for query in query_variants:
        try:
            result = service.ExecQuery(query)
            for item in result:
                return item, ""
        except Exception as exc:
            last_error = str(exc)
    return None, last_error or "No instance returned."


def exec_instance_method(service, class_name, method_name, args=None):
    obj, err = first_instance(service, class_name)
    if obj is None:
        return None, f"{class_name}: {err}"

    try:
        class_obj = service.Get(class_name)
        if args:
            in_params = class_obj.Methods_(method_name).InParameters.SpawnInstance_()
            for key, value in args.items():
                in_params.Properties_(key).Value = value
            out = service.ExecMethod_(obj.Path_.Path, method_name, in_params)
        else:
            out = service.ExecMethod_(obj.Path_.Path, method_name)
        return out, ""
    except Exception as exc:
        return None, f"{class_name}.{method_name}: {exc}"


def get_gamezone_keyboard_light(service):
    out, err = exec_instance_method(service, "LENOVO_GAMEZONE_DATA", "GetKeyboardLight")
    if out is None:
        return None, err
    try:
        return int(out.Properties_("Data").Value), ""
    except Exception as exc:
        return None, f"LENOVO_GAMEZONE_DATA.GetKeyboardLight parse error: {exc}"


def set_gamezone_keyboard_light(service, value):
    out, err = exec_instance_method(
        service,
        "LENOVO_GAMEZONE_DATA",
        "SetKeyboardLight",
        {"Data": int(value)},
    )
    if out is None:
        return False, err
    return True, ""


def get_lighting_status(service, lighting_id=0):
    out, err = exec_instance_method(
        service,
        "LENOVO_LIGHTING_METHOD",
        "Get_Lighting_Current_Status",
        {"Lighting_ID": int(lighting_id)},
    )
    if out is None:
        return None, err
    try:
        return {
            "lighting_id": int(lighting_id),
            "state": int(out.Properties_("Current_State_Type").Value),
            "brightness": int(out.Properties_("Current_Brightness_Level").Value),
        }, ""
    except Exception as exc:
        return None, f"LENOVO_LIGHTING_METHOD.Get_Lighting_Current_Status parse error: {exc}"


def set_lighting_status(service, lighting_id, state, brightness):
    out, err = exec_instance_method(
        service,
        "LENOVO_LIGHTING_METHOD",
        "Set_Lighting_Current_Status",
        {
            "Lighting_ID": int(lighting_id),
            "Current_State_Type": int(state),
            "Current_Brightness_Level": int(brightness),
        },
    )
    if out is None:
        return False, err
    return True, ""


def state_label(value):
    if value == KB_OFF:
        return "OFF"
    if value == KB_ON:
        return "ON"
    if value is None:
        return "UNKNOWN"
    return f"UNKNOWN ({value})"


def get_keyboard_light():
    service = connect_wmi()

    value, err = get_gamezone_keyboard_light(service)
    if value is not None:
        return value, "gamezone"

    lighting, lighting_err = get_lighting_status(service, lighting_id=0)
    if lighting is not None:
        return lighting["brightness"], "lighting_method"

    return None, f"{err} | {lighting_err}"


def set_keyboard_light(value):
    service = connect_wmi()

    ok, err = set_gamezone_keyboard_light(service, value)
    if ok:
        return True, "gamezone"

    lighting_before, lighting_err = get_lighting_status(service, lighting_id=0)
    if lighting_before is None:
        return False, f"{err} | {lighting_err}"

    target_brightness = 0 if value == KB_OFF else max(1, lighting_before["brightness"] or 4)
    target_state = lighting_before["state"]
    ok, lighting_set_err = set_lighting_status(
        service,
        lighting_id=lighting_before["lighting_id"],
        state=target_state,
        brightness=target_brightness,
    )
    if ok:
        return True, "lighting_method"

    return False, f"{err} | {lighting_set_err}"


def print_status(prefix="Current"):
    value, source = get_keyboard_light()
    if value is None:
        log(f"{prefix} keyboard backlight state: unavailable")
        log(str(source))
        return None
    log(f"{prefix} keyboard backlight state: {state_label(value)} (source: {source})")
    return value


def command_status():
    return 0 if print_status() is not None else 1


def command_set(value):
    before, _ = get_keyboard_light()
    ok, source = set_keyboard_light(value)
    if not ok:
        log("Failed to change keyboard backlight.")
        log(str(source))
        return 1
    log(f"Set command sent using: {source}")
    time.sleep(0.7)
    after = print_status("New")
    if after is None:
        return 1
    if before == after and before == value:
        log("Keyboard backlight was already in that state.")
    return 0


def command_toggle():
    current, source = get_keyboard_light()
    if current is None:
        log("Could not read current keyboard backlight state.")
        log(str(source))
        return 1
    target = KB_OFF if current == KB_ON else KB_ON
    return command_set(target)


def command_diag():
    service = connect_wmi()
    log(f"Admin: {is_admin()}")
    for class_name in ["LENOVO_GAMEZONE_DATA", "LENOVO_LIGHTING_DATA", "LENOVO_LIGHTING_METHOD"]:
        obj, err = first_instance(service, class_name)
        if obj is None:
            log(f"{class_name}: instance unavailable")
            log(err)
            continue
        log(f"{class_name}: instance found -> {obj.Path_.Path}")
        if class_name == "LENOVO_LIGHTING_DATA":
            try:
                props = {}
                for prop in obj.Properties_:
                    props[prop.Name] = prop.Value
                log(f"{class_name} props: {props}")
            except Exception as exc:
                log(f"{class_name} prop read failed: {exc}")

    value, source = get_keyboard_light()
    if value is None:
        log(f"Readable keyboard state unavailable: {source}")
    else:
        log(f"Readable keyboard state: {value} via {source}")
    return 0


def interactive_menu():
    log("Lenovo Keyboard Backlight Test")
    log(f"Log file: {LOG_FILE}")
    print("1. Show current state")
    print("2. Turn ON")
    print("3. Turn OFF")
    print("4. Toggle")
    print("5. Diagnostic info")
    print("Q. Quit")
    while True:
        choice = input("\nChoose: ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            return 0
        if choice == "1":
            command_status()
        elif choice == "2":
            command_set(KB_ON)
        elif choice == "3":
            command_set(KB_OFF)
        elif choice == "4":
            command_toggle()
        elif choice == "5":
            command_diag()
        else:
            print("Enter 1, 2, 3, 4, 5, or Q.")


def main():
    elevated = relaunch_as_admin()
    if elevated is None:
        return 0
    if elevated is False:
        return 1

    log("Starting keyboard backlight test.")
    log(f"Log file: {LOG_FILE}")

    command = sys.argv[1].strip().lower() if len(sys.argv) > 1 else ""
    if command in {"", "menu"}:
        return interactive_menu()
    if command == "status":
        return command_status()
    if command == "on":
        return command_set(KB_ON)
    if command == "off":
        return command_set(KB_OFF)
    if command == "toggle":
        return command_toggle()
    if command == "diag":
        return command_diag()

    log(f"Unknown command: {command}")
    log("Use: status, on, off, toggle, diag")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
