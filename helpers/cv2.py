import base64
import numpy as np
import cv2


class CV2CubeMeasurement:

    @classmethod
    def measure_image(self, image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        imgBlur = cv2.GaussianBlur(image, (5,5), 0)

        # Detectar bordes usando Canny
        border = cv2.Canny(imgBlur, 50, 150)

        # Encontrar contornos
        contour, _ = cv2.findContours(border, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Suponiendo que el cubo es el contorno más grande
        cube_contour = max(contour, key=cv2.contourArea)

        # Calcular rectángulo envolvente
        x, y, w, h = cv2.boundingRect(cube_contour)

        return w, h # Ancho, Alto



# # El input debe ser base64 de la imagen, en caso solo manden un texto, avisar para hacer el cambio y aquí mismo hacer la conversion a esa base.
# im_b64 = "IMAGENBASE64"
# im_bytes = base64.b64decode(im_b64)
# im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
# array_img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
# img = cv2.resize(array_img, (0,0), None, 0.5, 0.5)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
# imgCanny = cv2.Canny(imgBlur, 100,100)
# kernel = np.ones((5,5))
# imgDial = cv2.dilate(imgCanny, kernel, iterations=3)
# imgThre = cv2.erode(imgDial, kernel, iterations=2)
# contours, hiearchy = cv2.findContours(imgThre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     rect = cv2.minAreaRect(cnt)
#     (x, y), (w, h), angle = rect


# # Los valores que nos importan son w, h
# # Se considera una relación de 1 a 7, considerando que la foto se ha tomado a una distancia aproximada de 1m
# final_value = (w/7, h/7)



# def medir_cubo_en_foto(ruta_imagen):
#     # Cargar la imagen
#     imagen = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

#     # Aplicar filtro Gaussiano para reducir el ruido
#     imagen_suavizada = cv2.GaussianBlur(imagen, (5,5), 0)

#     # Detectar bordes usando Canny
#     bordes = cv2.Canny(imagen_suavizada, 50, 150)

#     # Encontrar contornos
#     contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Suponiendo que el cubo es el contorno más grande
#     contorno_cubo = max(contornos, key=cv2.contourArea)

#     # Calcular rectángulo envolvente
#     x, y, w, h = cv2.boundingRect(contorno_cubo)

#     return w, h

# ruta_imagen = "ruta_a_tu_imagen.jpg"
# ancho, alto = medir_cubo_en_foto(ruta_imagen)
# print(f"Ancho: {ancho} píxeles, Alto: {alto} píxeles")