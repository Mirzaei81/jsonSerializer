Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName Microsoft.VisualBasic

# $title = 'Admin Username: '
# $msg   = 'Enter Admin Username: '

# $DJANGO_SUPERUSER_USERNAME= [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)

# $title = 'Admin Email: '
# $msg   = 'Enter Admin Email: '

# $DJANGO_SUPERUSER_EMAIL= [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)
# $title = 'Admin Password: '
# $msg   = 'Enter Admin Password: '

# $DJANGO_SUPERUSER_PASSWORD = [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)
if(Test-Path -Path ".\.venv"){
    Write-Output ".\venv Exist"
}else{
    python -m venv .\.venv
} 
# .\.venv\Scripts\pip.exe install -r .\jsonSerializer\requirements.txt
# $makemigrationErrors = (.\.venv\Scripts\python.exe .\jsonSerializer\manage.py  makemigrations 2>&1 ) -join [System.Environment]::NewLine
# [System.Windows.Forms.MessageBox]::Show($makemigrationErrors, "Makemigrations ", [System.Windows.Forms.MessageBoxButtons]::OK)
# $migrationErrors=.\.venv\Scripts\python.exe .\jsonSerializer\manage.py migrate
# [System.Windows.Forms.MessageBox]::Show($migrationErrors, "Migrate", [System.Windows.Forms.MessageBoxButtons]::OK)
# $createSuperUserCommand  = "from django.contrib.auth.models import User; User.objects.create_superuser('$($DJANGO_SUPERUSER_USERNAME)', '$($DJANGO_SUPERUSER_EMAIL)','$($DJANGO_SUPERUSER_PASSWORD)')" 
# $createSuperUser =.\.venv\Scripts\python.exe .\jsonSerializer\manage.py shell -c $createSuperUserCommand 2>&1 | Out-String
# [System.Windows.Forms.MessageBox]::Show($runServer, "SuperUser", [System.Windows.Forms.MessageBoxButtons]::OK)
Start-Process -FilePath ".\.venv\Scripts\python.exe" -ArgumentList @(".\jsonSerializer\manage.py", "runserver", "127.0.0.1:1234") -NoNewWindow
Start-Process "http://127.0.0.1:1234/admin"
