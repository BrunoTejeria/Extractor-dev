def create_dirs():
    try:
        # Iterar a través de las URL en la configuración
        for site in config[1]["site"]:
            # Obtener el tipo que es el resultado para saber en qué carpeta hay que guardarlo
            search_type: dict = config[1]["site"][site]["genere"]

            # Crear un archivo para los resultados o resetearlo si ya existe
            try:
                file = open(f"{result_path}/{search_type}/{site}.txt", "w")
            except FileNotFoundError:
                if os.path.exists(f"{result_path}/{search_type}"):
                    continue  # Siguiente iteración si ya existe la carpeta
                else:
                    os.mkdir(f"{result_path}/{search_type}")
                    file = open(f"{result_path}/{search_type}/{site}.txt", "w")
            except:
                os.mkdir(f"{result_path}/others")
                file = open(f"{result_path}/others/{site}.txt", "w")

    except:
        return {"message": True}
