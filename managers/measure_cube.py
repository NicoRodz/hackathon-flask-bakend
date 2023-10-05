from core.exceptions import InvalidInputException
import os
import zipfile
from core.constants import UPLOAD_FOLDER, HARDCODED_MEASURE_RESPONSE

class MeasureCube:

    collection = "active"
    measurement_document = "measurement"
    cut_machine_document = "cut_machine"

    @classmethod
    def initialize(cls, firebase, request):
        cube_identifier = request.args.get('cube_identifier')

        if cube_identifier is None:
            raise InvalidInputException("Please provide the 'cube_identifier' value")
        data = {"cube_identifier": cube_identifier}
        firebase.create_data(cls.collection, cls.measurement_document, data)

    @classmethod
    def measure_distances(cls, request):
        print(str(request.files))
        if 'file' not in request.files:
            raise InvalidInputException("Please provide a file with images")

        file = request.files['file']

        if not file.filename.endswith('.zip'):
            raise InvalidInputException("Please provide a zip file")

        zip_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(zip_path)

        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            zip_file.extractall(os.path.join(UPLOAD_FOLDER, UPLOAD_FOLDER + '/extracted_files/'))

        #TODO logica de lectura del cubo

        return HARDCODED_MEASURE_RESPONSE

    @classmethod
    def get_cube_data(cls, firebase, request):
        cube_identifier = request.args.get('cube_identifier')

        if cube_identifier is None:
            raise InvalidInputException("Please provide the 'cube_identifier' value")
        data = {"cube_identifier": cube_identifier}
        firebase.create_data(cls.collection, cls.cut_machine_document, data)