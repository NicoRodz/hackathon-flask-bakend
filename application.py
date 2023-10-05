from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/')
def hello():
    return "¡Hola Mundo!"

@application.route('/test', methods=['GET'])
def test():
    from helpers.firebase import FirebaseHelper
    print("start with firebase")
    firebase = FirebaseHelper()
    firebase.create_data()
    print("end, created")
    return "¡Hola Mundo!"


@application.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)

if __name__ == "__main__":
    application.run()
