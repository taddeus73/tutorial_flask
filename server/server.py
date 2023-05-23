from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

'''
creo una rotta (route) per raggiungere l'endpoint homepage
il metodo utilizzato è GET
'''
@app.route('/', methods=["GET"])
def home():
    return {"mesg:":"beneventuo"}

'''
creo una rotta (route) per raggiungere l'endpoint me
il metodo utilizzato è GET
'''
@app.route('/me/', methods=["GET"])
def me():
    # restituisce un oggetto user in formato JSON
    response = {
        "user":{
            "nome":"fabio", 
            "cognome":"ciao",
            "eta":18
        }
    }
    return jsonify(response)

'''
creo una rotta per gestire una richieta POST
'''
@app.route('/users/', methods=["POST"])
def create_user():
    response = request.get_json()
    return jsonify({"nome": response['name'],
                    "email": response['email']
                    }
    )


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')