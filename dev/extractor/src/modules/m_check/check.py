

# Importar bibliotecas necesarias
try:
    from rich.console import Console
    from tqdm import tqdm
    import json
    import os
    import numpy as np
    import time
    import logging
except ImportError:
    pass

# Ruta del archivo de configuración
config_path = 'extractor/etc/config.json'
result_path = 'extractor/etc/data/processed_data'

# Definir consola
console = Console()

class Config:
    class Json:
        def __init__(self, json_path, mode='r'):
            self.file_path = json_path
            self.mode = mode

        def read(self):
            try:
                with open(self.file_path, mode=self.mode) as file:
                    data = json.load(file)
                    return data
            except FileNotFoundError:
                return None

        def edit(self, data):
            with open(self.file_path, mode='w') as file:
                json.dump(data, file, indent=4)

        def delete(self, data):
            pass

    def __init__(self, config_path, mode_='r', data=''):
        self.Json.__init__(self, config_path)
        self.read = self.Json.read(self)

class File:
    def __init__(self,file_search='', file_write=''):
        self.file_read = file_search
        self.file_write = file_write


    def read(self):
        with open(file=self.file_read, mode='r', encoding='utf-8') as file:
            lines = []

        try:
            with open(file=self.file_read, mode='rb') as file:
                for line_number, raw_line in enumerate(file, 1):
                    try:
                        # Decodificar la línea como UTF-8
                        line = raw_line.decode('utf-8').strip()
                        lines.append(line)
                    except UnicodeDecodeError as e:
                        print(f"Error decoding line {line_number}: {e}")
                        # Omitir la línea que genera el error y continuar con la siguiente
                        continue
        except FileNotFoundError:
            print(f"El archivo {self.file_read} no fue encontrado.")
            return {"message": f"Archivo no encontrado: {self.file_read}"}
        self.lines = lines

    def reset(self):
        with open \
        (
            file=self.file_write,
            mode='w',
            encoding='utf-8'
        ) as file:
            file.close()

    def write(self, content, mode='w'):
        with open \
        (
            file=self.file_write,
            mode=mode,
            encoding='utf-8'
        ) as file:
            file.write(content)
            file.close()

    def count(self):
        total_lines = sum(1 for line in self.lines)
        self.count = total_lines

    def clear(self, file_clear):
        try:
            with open \
            (
                file=file_clear,
                mode='w'
            ) as f:
                # The file is reset (cleared)
                pass
            return {"message": True}
        except:
            return {"message": True}

# Definición de la clase Check, que hereda de las clases File y Config
# Importar las clases File y Config
class Check(File, Config):
    def __init__(self):
        # Leer la configuración
        self.config = Config(config_path).read

        # Llamar al constructor de la clase Config
        Config.__init__(self, config_path)




        # Iterar entre documentos de texto y extraer sis lineas
        self.file_lines = []
        for text in self.config[0]["textFile"]:
            if os.path.exists(text):
                file = File(text)
                file.read()
                for line in file.lines:
                    self.file_lines.append(line)


    def create_dirs(self):
        try:
            # Iterar a través de las URL en la configuración
            for site in self.config[1]['site']:
                # Objeten el tipo que es el resultado para saber en que carpeta hay que guardarlo
                search_type: dict = self.config[1]['site'][site]['genere']

                # Crear un archivo para los resultados o resetearlo si ya existe
                try:
                    file = open(f'{result_path}/{search_type}/{site}.txt', 'w')
                except FileNotFoundError:
                    if os.path.exists(f"{result_path}/{search_type}"):
                        next
                    else:
                        os.mkdir(f'{result_path}/{search_type}')
                        file = open(f'{result_path}/{search_type}/{site}.txt', 'w')
                except:
                    os.mkdir(f'{result_path}/others')
                    file = open(f'{result_path}/others/{site}.txt', 'w')


        except:
            return {"message": True}


    # Método para procesar líneas del archivo
    def process_lines(self):
        # Obtener las líneas del archivo
        file_lines = self.file_lines
        print(self.create_dirs())
        count: int = 1
        for site in self.config[1]['site']:
            exception = False

            # Configurar archivo de salida
            search_type: dict = self.config[1]['site'][site]['genere']

            file_path = f'{result_path}/{search_type}/{site}.txt'
            print(file_path)

            # imprimir en que se esta buscando
            console.print \
            (f'''
            [bold red]{site}[/bold red]
            ''')

            # Obtener el tipo de búsqueda (mail, user, all)
            userType = self.config[1]['site'][site]['type']

            # Inicializar listas para los resultados
            results: list = []
            result_lines: list = []

            # Crear una barra de progreso con tqdm

            with tqdm(total=sum(1 for i in file_lines) * len(self.config[1]['site'][site]['searchSites']), desc="Procesando", unit="línea", colour='green', unit_scale=True) as progress_bar:

                # Iterar a través de las URL y búsquedas en la configuración
                for searchSite in self.config[1]["site"][site]["searchSites"]:
                    url = self.config[1]['site'][site]["searchSites"][searchSite]

                    # Iterar a través de las líneas del archivo de búsqueda
                    result: str = ''

                    # Iterar entre lineas del archivo
                    for line in file_lines:

                        # Actualizar la barra de progreso
                        progress_bar.update(1)

                        # Tomar user:pass
                        post_result = line.find(':', line.find(':') + 1)

                        # Comprobar si la URL está en la línea
                        if url in line[:post_result] and post_result != ":":
                            result = line[post_result + 1:]
                            result_lines.append(result)





            print('\n')



            results_first_part = set()

            # Seleccionar la condición común para ambos casos fuera del bucle
            common_condition = lambda result: "UNKNOWN" not in result and result_div[0] not in results_first_part and result_div[1] != " "
            # Crear una barra de progreso con tqdm
            for result in result_lines:
                try:
                    result_div = result.split(':')
                    if result != "\n":
                        if common_condition(result):
                            if userType == 'mail' and '@' in result_div[0]:
                                results_first_part.add(result_div[0])
                                results.append(result)
                            elif userType == "int":
                                try:
                                    int(result_div[0])
                                except:
                                    continue
                                results.append(result)
                            elif userType == "float":
                                try:
                                    float(result_div[0])
                                except:
                                    continue
                                results.append(result)

                            elif userType == "fenixzone":
                                if "_" in result:
                                    results.append(result)

                            elif userType != 'mail':
                                results_first_part.add(result_div[0])
                                results.append(result)

                except Exception as e:
                    if exception == True:
                        pass
                    else:
                        print(e)
                        exception = True
            exception = False

            # Escribir los resultados en un archivo
            with open(file=file_path, mode='a') as file_:
                    for result in results:

                        try:
                            file_.write(f"{result}\n")
                        except:
                            continue
            console.print("[bold green]\nResultados totales: [/bold green]" + str(len(results)))
            print('\n \n')

        # Devolver la lista de resultados
        return result_lines
