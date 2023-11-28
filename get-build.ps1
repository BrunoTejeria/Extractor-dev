# Ruta de la carpeta que se está trabajando
$dev = ".\dev\"

# Ruta de la build
$build = ".\build\"

$buildDelete = ".\build\extractor"

# Borrar directorio de build
Remove-Item -Path $buildDelete -Recurse -Force

# Copiar archivos en la carpeta de build
Copy-Item "$dev\*" -Destination $build -Recurse

# Ruta del archivo de texto
$texto = ".\build\text.txt"

# Ruta de texto para pegar
$textoRuta = ".\build\extractor\etc\data\raw_data\"

# Preguntar si se debe copiar el archivo de texto
$textoPegar = Read-Host "¿Deseas copiar el archivo de texto? (Y/N)"

# Verificar la respuesta del usuario en textoPegar (sensible a mayúsculas)
if ($textoPegar -eq "Y" -or $textoPegar -eq "y" -or $textoPegar -eq "S" -or $textoPegar -eq "s") {
    # Copiar archivo de texto
    Copy-Item $texto -Destination $textoRuta
}

# Preguntar si se debe ejecutar la build
$ejecutar = Read-Host "¿Deseas ejecutar la build? (Y/N)"

# Verificar la respuesta del usuario en ejecutar (sensible a mayúsculas)
if ($ejecutar -eq "Y" -or $ejecutar -eq "y" -or $ejecutar -eq "S" -or $ejecutar -eq "s" -or $ejecutar -eq "") {
    # Ruta del ejecutador de la build (ajusta según sea necesario)
    $buildScriptPath = ".\build.ps1"
    if (Test-Path $buildScriptPath) {
        # Ejecutar el script de la build
        & $buildScriptPath
    } else {
        Write-Host "Error: El script de la build no se encontró en la ruta especificada."
    }
}
