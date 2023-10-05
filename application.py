from flask import Flask, request, jsonify, g
from helpers.firebase import FirebaseHelperSingleton
from managers.measure_cube import MeasureCube
from managers.cut_process import CutProcess
from core.exceptions import InvalidInputException
import os
from core.constants import UPLOAD_FOLDER
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
firebase = FirebaseHelperSingleton()

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@application.route('/')
def hello():
    return "Hackathon API"

@application.route('/initialize_measurements', methods=['GET'])
def initialize_measurements():
    try:
        MeasureCube().initialize(firebase, request)
    except InvalidInputException as e:
        return jsonify(str(e)), 422
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 501

    return jsonify("Successful configured"), 200

@application.route("/clean_measurement", methods=["PUT"])
def clean_measurement():
    try:
        MeasureCube().clean_measurement(firebase)
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 501
    
    return jsonify("Successful updated"), 200

@application.route('/initialize_cut', methods=['GET'])
def initialize_cut():
    try:
        CutProcess().initialize(firebase, request)
    except InvalidInputException as e:
        return jsonify(str(e)), 422
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 501

    return jsonify("Successful configured"), 200

@application.route("/clean_cut", methods=["PUT"])
def clean_cut():
    try:
        CutProcess().clean(firebase)
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 501
    
    return jsonify("Successful updated"), 200

@application.route('/measure_distances', methods=['POST'])
def measure_distances():
    try:
        distances = MeasureCube().measure_distances(request)
    except InvalidInputException as e:
        return jsonify(str(e)), 422
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 501
        
    return jsonify(distances), 200

if __name__ == "__main__":
    print("Running app...")
    application.run()
