import subprocess

resultado = subprocess.run(["bash", ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)