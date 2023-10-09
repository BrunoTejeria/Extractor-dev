#!/bin/bash

# Ruta de la carpeta que se esta trabajando
working="working/"

# Ruta de la build
build="build/"

# Copiar archivos en la build
cp -r "$working"/* "$build/"
