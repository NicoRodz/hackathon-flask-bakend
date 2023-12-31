import base64
import numpy as np
import cv2
from core.constants import CSV_CORRECTION_FACTOR as CF
from core.exceptions import InvalidInputException


class CV2CubeMeasurement:

    @classmethod
    def is_width_or_depth(cls, image_path):
        if "width" in image_path:
            return "width"
        elif "depth" in image_path:
            return "depth"
        else:
            print("Error with file: " + image_path)
            raise InvalidInputException("File is not width or depth specified")

    @classmethod
    def measure_image(self, image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        ret, thresh = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        kernel = np.ones((5,5),np.uint8)
        opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations = 2)
        processed_kernel = np.ones((6,6),np.uint8)
        dilate = cv2.dilate(opening, processed_kernel, iterations=3)
        imgBlur = cv2.GaussianBlur(dilate, (5,5), 0)

        # Detectar bordes usando Canny
        border = cv2.Canny(imgBlur, 50, 150)

        # Encontrar contornos
        contour, _ = cv2.findContours(border, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Suponiendo que el cubo es el contorno más grande
        cube_contour = max(contour, key=cv2.contourArea)

        # Calcular rectángulo envolvente
        x, y, w, h = cv2.boundingRect(cube_contour)
        
        print("\nimage_path: " + image_path + " | " + self.is_width_or_depth(image_path))
        print("Width: " + str(w*CF))
        print("Height:" + str(h*CF))
        print("========================")
        return {
            "width": w*CF, 
            "height": h*CF, 
            "type": self.is_width_or_depth(image_path)
        }