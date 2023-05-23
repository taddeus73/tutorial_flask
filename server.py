from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return {"mesg:":"beneventuo"}

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
