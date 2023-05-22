from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return {"mesg:":"beneventuo"}

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
    
# per eseguire lanciare il comando
# python server.py
# oppure
# export FLASK_APP=server.py
# lask run --port=8000 --host=0.0.0.0