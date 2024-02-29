def reinstall(Q=False):
    print("Desear descargar de nuevo los paquetes? (s/n)")
    ask = input(">> ")
    if ask == "si" or ask == "yes" or ask == "s" or ask == "y":
        print("Descargando paquetes...")
        """try:
			os.system("python3 install.py")
		except as error:
			print(f'[!] Error al importar "{error.name}: {error.args[0]}"')"""
        if Q == True:
            quit()

    else:
        print("Saliendo...")
        quit()
