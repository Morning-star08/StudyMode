Dim objShell
Dim pyExe
Dim pyScript

Set objShell = CreateObject("WScript.Shell")

pyExe    = "C:\Users\namas\AppData\Local\Programs\Python\Python311\pythonw.exe"
pyScript = "C:\Users\namas\OneDrive\Documents\study_mode\study_mode_krish.py"

objShell.Run Chr(34) & pyExe & Chr(34) & " " & Chr(34) & pyScript & Chr(34), 0, False
