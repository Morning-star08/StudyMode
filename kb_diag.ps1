$ErrorActionPreference = 'Continue'

'ADMIN=' + ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

try {
    $obj = Get-CimInstance -Namespace root\wmi -Query "SELECT * FROM LENOVO_GAMEZONE_DATA" -ErrorAction Stop | Select-Object -First 1
    'GZ_INSTANCE=' + ($obj -ne $null)
    if ($obj) {
        try {
            $r = Invoke-CimMethod -InputObject $obj -MethodName GetKeyboardLight -ErrorAction Stop
            'GETKB=' + $r.Data
        } catch {
            'GETKB_ERR=' + $_.Exception.Message
        }
        try {
            $s = Invoke-CimMethod -InputObject $obj -MethodName IsSupportLightingFeature -ErrorAction Stop
            'ISLIGHT=' + $s.Data
        } catch {
            'ISLIGHT_ERR=' + $_.Exception.Message
        }
    }
} catch {
    'GZ_ERR=' + $_.Exception.Message
}

try {
    $l = Get-CimInstance -Namespace root\wmi -Query "SELECT * FROM LENOVO_LIGHTING_DATA" -ErrorAction Stop
    'LIGHT_COUNT=' + @($l).Count
    foreach ($x in $l) {
        'LIGHT_ITEM=' + ($x | ConvertTo-Json -Compress)
    }
} catch {
    'LIGHT_ERR=' + $_.Exception.Message
}

try {
    $m = Get-CimInstance -Namespace root\wmi -Query "SELECT * FROM LENOVO_LIGHTING_METHOD" -ErrorAction Stop | Select-Object -First 1
    'LIGHT_METHOD_INSTANCE=' + ($m -ne $null)
    if ($m) {
        try {
            $r = Invoke-CimMethod -InputObject $m -MethodName Get_Lighting_Current_Status -Arguments @{
                Lighting_ID = [byte]0
                Current_State_Type = [byte]0
                Current_Brightness_Level = [byte]0
            } -ErrorAction Stop
            'GET_LIGHT_METHOD=' + ($r | ConvertTo-Json -Compress)
        } catch {
            'GET_LIGHT_METHOD_ERR=' + $_.Exception.Message
        }
    }
} catch {
    'LIGHT_METHOD_ERR=' + $_.Exception.Message
}
