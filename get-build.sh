#!/bin/bash

# Ruta de la carpeta que se está trabajando
dev="./dev/"

# Ruta de la build
build="./build/"

# Copiar archivos en la carpeta de build
cp -r "$dev"/* "$build/"

# Ruta del archivo de texto
texto="./build/text.txt"

# Ruta de texto para pegar
textoRuta="./build/extractor/etc/data/raw_data/"

# Preguntar si se debe copiar el archivo de texto
echo "¿Deseas copiar el archivo de texto? (Y/N):"
read textoPegar

# Verificar la respuesta del usuario en textoPegar (sensible a mayúsculas)
if [ "$textoPegar" == "Y" ] || [ "$textoPegar" == "y" ] || [ "$textoPegar" == "S" ] || [ "$textoPegar" == "s" ] || [ "$textoPegar" == "" ]; then
    # Copiar archivo de texto (sin la opción -r)
    cp "$texto" "$textoRuta"
fi

# Preguntar si se debe ejecutar la build
echo "¿Deseas ejecutar la build? (Y/N):"
read ejecutar

# Verificar la respuesta del usuario en ejecutar (sensible a mayúsculas)
if [ "$ejecutar" == "Y" ] || [ "$ejecutar" == "y" ] || [ "$ejecutar" == "S" ] || [ "$ejecutar" == "s" ] || [ "$ejecutar" == "" ]; then
    # path de ejecutador de la build
    ./build.sh
fi
