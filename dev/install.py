
import subprocess


# Ejecuta el comando Bash desde Python
resultado = subprocess.run('bash extractor/etc/install.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Imprime la salida estándar y el error estándar
print("Salida estándar:")
print(resultado.stdout)

print("Error estándar:")
print(resultado.stderr)
