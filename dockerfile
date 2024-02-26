# Usa una imagen base que incluya Python
FROM python:3.12

# Configura el directorio de trabajo en /app
WORKDIR /app



# Copia el script Python al directorio de trabajo
COPY dev/* .
COPY build/*.txt ./extractor/etc/data/wordlists

# Convierte el formato de línea del script bash para evitar problemas
RUN python3 -m pip install -r ./requirements.txt

RUN ls

