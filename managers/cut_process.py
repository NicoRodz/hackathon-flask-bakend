from core.exceptions import InvalidInputException
import os
import zipfile
from helpers.cv2 import CV2CubeMeasurement
from helpers.files import FileHelper
from helpers.math import MathHelper


class CutProcess:

    collection = "active"
    cut_machine_document = "cut_machine"

    @classmethod
    def initialize(cls, firebase, request):
        cube_identifier = request.args.get('cube_identifier')

        if cube_identifier is None:
            raise InvalidInputException("Please provide the 'cube_identifier' value")
        data = {"cube_identifier": cube_identifier}
        firebase.create_data(cls.collection, cls.cut_machine_document, data)

    @classmethod
    def clean(cls, firebase):
        firebase.update_data(cls.collection, cls.cut_machine_document, {"cube_identifier": None})