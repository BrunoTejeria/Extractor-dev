
# Importación de módulos necesarios
from ..m_file.file import *
from ..m_config.config import *


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
result_path = 'extractor/etc/data/processed_data/'

# Definir consola
console = Console()

# Definición de la clase Check, que hereda de las clases File y Config
# Importar las clases File y Config
class Check(File, Config):
    def __init__(self):
        # Leer la configuración
        self.config = Config(config_path).read()

        # Llamar al constructor de la clase Config
        Config.__init__(self, config_path)

        # Obtener rutas de archivos desde la configuración
        self.file_search =  self.config[0]['textFile']['textSearch']

        # Llamar a los constructores de las clases File y Config
        File.__init__(self, self.file_search)
        File.read(self)

    # Método para procesar líneas del archivo
    def process_lines(self):
        # Obtener las líneas del archivo
        file_lines: list = self.lines
        count: int = 1

        # Iterar a través de las URL en la configuración
        for site in self.config[1]['site']:
            # Objeten el tipo que es el resultado para saber en que carpeta hay que guardarlo
            search_type: dict = self.config[1]['site'][site]['genere']

            # Crear un archivo para los resultados o resetearlo si ya existe
            try:
                file = open(f'{result_path}{search_type}/{site}.txt', 'w')
                file_path: str = f'{result_path}{search_type}/{site}.txt'
            except FileNotFoundError:
                os.mkdir(f'{result_path}/{search_type}')
                file = open(f'{result_path}{search_type}/{site}.txt', 'w')
                file_path: str = f'{result_path}{search_type}/{site}.txt'
            except:
                os.mkdir(f'{result_path}/others')
                file = open(f'{result_path}/others/{site}.txt', 'w')
                file_path = f'{result_path}/others/{site}.txt'

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

            with tqdm(total=len(file_lines * len(self.config[1]['site'][site]["searchSites"])), desc="Procesando", unit="línea", colour='green', unit_scale=True) as progress_bar:

                # Iterar a través de las URL y búsquedas en la configuración
                for searchSite in self.config[1]["site"][site]["searchSites"]:
                    url: dict = self.config[1]['site'][site]["searchSites"][searchSite]

                    # Iterar a través de las líneas del archivo de búsqueda
                    result: str = ''

                    # Iterar entre lineas del archivo
                    for line in file_lines:

                        # Actualizar la barra de progreso
                        progress_bar.update(1)

                        # Tomar user:pass
                        post_result: str = line.find(':', line.find(':') + 1)

                        # Comprobar si la URL está en la línea
                        if url in line[:post_result]:
                            result: str = line[post_result + 1:]
                            result_lines.append(result)




            print('\n')



            results_first_part = set()

            # Seleccionar la condición común para ambos casos fuera del bucle
            common_condition = lambda result: "UNKNOWN" not in result and result_div[0] not in results_first_part and result_div[1] != " "
            # Crear una barra de progreso con tqdm
            with tqdm(total=len(result_lines), desc="Chequeando", unit="línea", colour='blue', unit_scale=True) as progress_bar:
                for result in result_lines:
                    try:
                        result_div = result.split(':')

                        if common_condition(result):
                            if userType == 'mail' and '@' in result_div[0]:
                                results_first_part.add(result_div[0])
                                results.append(result)
                            elif userType != 'mail':
                                results_first_part.add(result_div[0])
                                results.append(result)
                    except ValueError as e:
                        print(e)

                    progress_bar.update(1)

            # Escribir los resultados en un archivo
            with open(file=file_path, mode='a',) as file_:
                    for result in results:
                        if result != '\n':
                            try:
                                file_.write(result)
                            except:
                                continue
            console.print("[bold green]\nResultados totales: [/bold green]" + str(len(results)))
            print('\n \n')

        # Devolver la lista de resultados
        return result_lines
