import subprocess

bash = subprocess.run(["bash", '.extractor/etc/install.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(bash.stderr)

error = bash.stderr
if bash.returncode == 0:
    print('instalado')
else:
    python = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(python.stderr)
    if python.returncode == 0:
        print('instalado')
    else:
        print('error')