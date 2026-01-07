# Usamos una imagen base oficial de Python ligera
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el script de Python al contenedor
COPY src/script.py .

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "script.py"]
