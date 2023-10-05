# Utilizar una imagen base de Python
FROM python:3.8-slim

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Establecer el comando por defecto para ejecutar Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "application:application"]