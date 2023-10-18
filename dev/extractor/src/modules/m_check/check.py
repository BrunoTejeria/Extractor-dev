
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
        # Crear una instancia de la clase Config para leer la configuración
        config_json_class = Config(config_path)
        config = config_json_class.read()

        # Obtener rutas de archivos desde la configuración
        self.file_search =  config[0]['textFile']['textSearch']
        self.file_result = config[0]['textFile']['textResult']

        # Llamar a los constructores de las clases File y Config
        File.__init__(self, self.file_search, self.file_result)
        File.read(self)
        self.urls = config


    # Método para procesar líneas del archivo
    def process_lines(self):
        file_lines = self.lines
        count = 1
        # Reiniciar el archivo de búsqueda al principio
        File.reset(self)

        # Iterar a través de las URL en la configuración
        for site in self.urls[1]['site']:
            # imprimir en que se esta buscando
            console.print \
            (f'''
            [green]{site}[/green]
            ''')

            # Crear una barra de progreso con tqdm
            with tqdm(total=len(file_lines * len(self.urls[1]['site'][site])), desc="Procesando", unit="línea", colour='green') as progress_bar:
                result_lines = []
                # Iterar a través de las URL y búsquedas en la configuración
                for search in self.urls[1]['site'][site]:
                    url = self.urls[1]['site'][site][search]

                    # Iterar a través de las líneas del archivo de búsqueda
                    for line in file_lines:
                        result_split = []
                        result = ''
                        progress_bar.update(1)

                        # Comprobar si la URL está en la línea
                        if url in line:
                                try:
                                    post_result = line.find(':', line.find(':') + 1)
                                    if url in line[:post_result]:
                                        try:
                                            result = line[post_result + 1:]
                                        except ValueError:
                                            result = line[line.index(' ') + 1:]
                                except ValueError:
                                    continue

                                if 'UNKNOWN' not in result and result not in result_lines and ('netflix' in url or 'disney' in url or 'starplus' in url or 'hbo' in url) and '@' in result[:result.find(':')]:
                                    result_lines.append(result)

                    # Escribir los resultados en un archivo
                    with open(f'{result_path}result_{site}.txt', 'a',) as file_:
                            for line in result_lines:
                                file_.write(line)

        # Devolver la lista de resultados
        return result_lines
