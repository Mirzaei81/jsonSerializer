Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName Microsoft.VisualBasic
$currentPath = Get-Location
$pipPath =Join-Path $currentPath ".venv\Scripts\pip.exe"
$pythonPath =Join-Path  $currentPath ".venv\Scripts\python.exe"
$title = 'Admin Username: '
$msg   = 'Enter Admin Username: '

$DJANGO_SUPERUSER_USERNAME= [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)

$title = 'Admin Email: '
$msg   = 'Enter Admin Email: '

$DJANGO_SUPERUSER_EMAIL= [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)
$title = 'Admin Password: '
$msg   = 'Enter Admin Password: '
$DJANGO_SUPERUSER_PASSWORD = [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)
if(Test-Path -Path ".\.venv"){
    Write-Output ".\venv Exist"
}else{
    python -m venv .\.venv
} 
Invoke-Expression "$pipPath install -r requirements.txt"
Invoke-Expression "$pythonPath manage.py makemigrations"
Invoke-Expression "$pythonPath manage.py migrate"
$createSuperUserCommand  = "from django.contrib.auth.models import User; User.objects.create_superuser('$($DJANGO_SUPERUSER_USERNAME)', '$($DJANGO_SUPERUSER_EMAIL)','$($DJANGO_SUPERUSER_PASSWORD)')" 
Invoke-Expression "$pythonPath manage.py shell -c `"$createSuperUserCommand`"" 
Start-Process -FilePath "$pythonPath" -ArgumentList @("manage.py", "runserver", "127.0.0.1:1234") -NoNewWindow
Start-Process "http://127.0.0.1:1234/admin"
Read-Host "Enter a key to close the server"
