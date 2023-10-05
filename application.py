from flask import Flask, request, jsonify, g
from helpers.firebase import FirebaseHelperSingleton
from managers.measure_cube import MeasureCube
from core.exceptions import InvalidInputException
import os
from core.constants import UPLOAD_FOLDER

application = Flask(__name__)
firebase = FirebaseHelperSingleton()

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@application.route('/')
def hello():
    return "¡Gogogogogogogo!"

@application.route('/initialize_measurements', methods=['GET'])
def initialize_measurements():
    try:
        MeasureCube().initialize(firebase, request)
    except InvalidInputException as e:
        return jsonify(str(e)), 422
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 500

    return jsonify("Successful configured"), 200

@application.route('/measure_distances', methods=['POST'])
def measure_distances():
    try:
        distances = MeasureCube().measure_distances(request)
    except InvalidInputException as e:
        return jsonify(str(e)), 422
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 500

    return jsonify(distances), 200

@application.route('/cube_data_for_cut_machine', methods=['GET'])
def cube_data_for_cut_machine():
    try:
        MeasureCube().show_cube_data(firebase, request)
    except InvalidInputException as e:
        return jsonify(str(e)), 422
    except Exception as e:
        print("HandledException: " + str(e))
        return jsonify("HandledException: " + str(e)), 500

    return jsonify("Successful configured"), 200




if __name__ == "__main__":
    application.run()
