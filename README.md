# tutorial flask
## creare request GET e POST e restituiamo la risposta in JSON

### creare il virtual-env con il seguente comando
```bash
python -m venv my_venv
````

## attivare il virtual-env
### su windows
```bash
my_venv/scripts/activate.bat
```
#### su macos
```bash
source my_env/bin/activate
````

## lanciare il comando pip install per installare flask
```bash
pip install flask
```
    
### per eseguire lanciare il comando su macos
```bash
python server.py
```
oppure
```bash
export FLASK_APP=server.py
flask run --port=8000 --host=0.0.0.0
```

### per eseguire lanciare il comando su windows
```bash
python server.py
set FLASK_APP=server.py
flask run --port=8000 --host=0.0.0.0
```

