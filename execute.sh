pip install -r requirements.txt
pip install PyInstaller

pyinstaller --onefile src/main.pyw
cp src/config.json src/dist/config.json
cp src/symbols.json src/dist/symbols.json