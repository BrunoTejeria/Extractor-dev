
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
                    for line in file_lines:

                        # Actualizar la barra de progreso
                        progress_bar.update(1)

                        post_result: str = line.find(':', line.find(':') + 1)

                        # Comprobar si la URL está en la línea
                        if url in line[:post_result]:
                            result = line[post_result + 1:]
                            """
                            Aquí se realiza la operación de agregar el resultado a la lista result_lines.
                            Esta operación puede ser lenta debido a que se utiliza la función np.append() en cada iteración del bucle.
                            Para mejorar el rendimiento, se recomienda utilizar una lista estándar de Python en lugar de un array de numpy.
                            Esto se debe a que la función np.append() crea una nueva matriz en cada llamada, lo que puede ser ineficiente en términos de memoria y tiempo de ejecución.
                            Además, se puede considerar utilizar una comprensión de lista para agregar los resultados a la lista result_lines, ya que es más eficiente que la función np.append().
                            """
                            result_lines.append(result)



            
            print('\n')

            # Crear una barra de progreso con tqdm
            with tqdm(total=len(result_lines), desc="Chequeando", unit="línea", colour='blue', unit_scale=True) as progress_bar:
                results_first_part: list = []
                if userType == 'mail':
                    for result in result_lines:
                        try:
                            if not "UNKNOWN" in result:
                                if len(result) <= 64:
                                    result_first_part: str = result.split(':')[0]
                                    if result_first_part not in results_first_part:
                                        # Comprobar si el resultado contiene una @
                                        if '@' in result_first_part:
                                            # Añadir el resultado a la lista de resultado
                                            results_first_part.append(result_first_part)
                                            results.append(result)
                        except ValueError as e:
                            print(e)
                        progress_bar.update(1)
                else:
                    for result in result_lines:
                        try:
                            if not "UNKNOWN" in result:
                                if len(result) <= 64:
                                    result_first_part: str = result.split(':')[0]
                                    if not result_first_part in results_first_part:
                                            results_first_part.append(result_first_part)
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
