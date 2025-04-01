# Imagen base con Python 3.10
FROM python:3.10

# Configurar el directorio de trabajo en Docker
WORKDIR /app

# Copiar archivos del proyecto a la imagen de Docker
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000 para FastAPI
EXPOSE 8000

# Comando para iniciar la API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
