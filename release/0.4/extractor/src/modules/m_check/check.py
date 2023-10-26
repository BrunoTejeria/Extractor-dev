
# Importación de módulos necesarios
from ..m_file.file import *
from ..m_config.config import *

# Importar bibliotecas necesarias
try:
    from rich.console import Console
    from tqdm import tqdm
    import json
except ImportError:
    pass

# Ruta del archivo de configuracion
config_path = 'extractor/etc/config.json'
result_path = 'extractor/etc/data/processed_data/'

# Definir consola
console = Console()

# Definición de la clase Check, que hereda de las clases File y Config
class Check(File, Config):
    def __init__(self):
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
        file_lines = self.lines
        count = 1


        # Iterar a través de las URL en la configuración
        for site in self.config[1]['site']:
            # Crear un archivo para los resultados o resetearlo si ya existe
            file = open(f'{result_path}result_{site}.txt', 'w')

            # imprimir en que se esta buscando
            console.print \
            (f'''
            [green]{site}[/green]
            ''')
            if self.config[1]['site'][site]['type'] == 'mail':
                userType = 'mail'
            elif  self.config[1]['site'][site]['type'] == 'user':
                userType = 'user'
            else:
                userType = 'all'
            # Crear una barra de progreso con tqdm
            with tqdm(total=len(file_lines * len(self.config[1]['site'][site])), desc="Procesando", unit="línea", colour='green') as progress_bar:
                results = []
                result_lines = []
                # Iterar a través de las URL y búsquedas en la configuración
                for search in self.config[1]['site'][site]:
                    url = self.config[1]['site'][site][search]
                    # Iterar a través de las líneas del archivo de búsqueda
                    for line in file_lines:
                        result = ''

                        progress_bar.update(1)

                        # Comprobar si la URL está en la línea
                        if url in line:
                                try:
                                    post_result = line.find(':', line.find(':') + 1)
                                    if url in line[:post_result]:
                                        result = line[post_result + 1:]
                                        result_lines.append(result)
                                except ValueError:
                                    continue

                # Iterar a través de los resultados
                for result in result_lines:
                    # Si el resultado no está en la lista de resultados, añadirlo
                    if not result in results[:200]:
                        if userType == 'mail':
                            # Comprobar si el resultado contiene una @
                            if '@' in result:
                                # Añadir el resultado a la lista de resultado

                                results.append(result)
                        else:
                            results.append(result)


                # Escribir los resultados en un archivo
                with open(f'{result_path}result_{site}.txt', 'a',) as file_:
                        for result in results:
                            if result != '\n':
                                file_.write(result)
            console.print("[bold green]\nResultados totales: [/bold green]" + str(len(results)))

        # Devolver la lista de resultados
        return result_lines
