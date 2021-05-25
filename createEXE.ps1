cd dist
if ($?) {
    pyinstaller --onefile -w ..\projectfiles\main.py
}
