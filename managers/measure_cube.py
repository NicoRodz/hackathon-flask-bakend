from core.exceptions import InvalidInputException
import os
import zipfile
from core.constants import UPLOAD_FOLDER, HARDCODED_MEASURE_RESPONSE
from helpers.cv2 import CV2CubeMeasurement
from helpers.files import FileHelper
from helpers.math import MathHelper

class MeasureCube:

    collection = "active"
    measurement_document = "measurement"

    @classmethod
    def initialize(cls, firebase, request):
        cube_identifier = request.args.get('cube_identifier')

        if cube_identifier is None:
            raise InvalidInputException("Please provide the 'cube_identifier' value")
        data = {"cube_identifier": cube_identifier}
        firebase.create_data(cls.collection, cls.measurement_document, data)

    @classmethod
    def clean_measurement(cls, firebase):
        firebase.update_data(cls.collection, cls.measurement_document, {"cube_identifier": None})
        

    @classmethod
    def measure_distances(cls, request):
        """
            raise InvalidInputException if image has no name of width or depth
        """
        if 'file' not in request.files:
            raise InvalidInputException("Please provide a file with images")

        file = request.files['file']

        if not file.filename.endswith('.zip'):
            raise InvalidInputException("Please provide a zip file")

        zip_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(zip_path)

        extracted_files_folder = 'extracted_files'
        full_extracted_files_path = UPLOAD_FOLDER + "/" + extracted_files_folder + "/"

        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            zip_file.extractall(os.path.join(UPLOAD_FOLDER, extracted_files_folder))

        file_paths = FileHelper.get_filepaths_from_folder(full_extracted_files_path)

        measure_results = []
        for path in file_paths:
            measure_results.append(CV2CubeMeasurement.measure_image(full_extracted_files_path + path))

        FileHelper.deep_folder_delete(full_extracted_files_path)
        return MathHelper.get_cube_measurements(measure_results)