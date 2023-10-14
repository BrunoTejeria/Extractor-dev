# Importación de módulos y bibliotecas necesarios
from ..m_file.file import File
from ..m_config.config import Config
from tqdm import tqdm
import json

# Ruta del archivo de configuración
config_path = 'extractor/etc/config.json'
result_path = 'extractor/etc/data/processed_data/'

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
        self.url = config

    # Método para procesar líneas del archivo
    def process_lines(self):
        file_lines = self.lines
        count = 1
        # Reiniciar el archivo de búsqueda al principio
        File.reset(self)

        # Iterar a través de las URL en la configuración
        for site in self.url[1]['url']:
            file_result = self.file_result
            print(site)

            # Crear una barra de progreso con tqdm
            with tqdm(total=len(file_lines * 2), desc="Procesando", unit="línea", colour='green') as progress_bar:
                result_lines = []
                # Iterar a través de las URL y búsquedas en la configuración
                for search in self.url[1]['url'][site]:
                    url = self.url[1]['url'][site][search]

                    # Iterar a través de las líneas del archivo de búsqueda
                    for line in file_lines:
                        progress_bar.update(1)

                        # Comprobar si la URL está en la línea
                        if url in line and line != '\n':
                            result = ''
                            try:
                                post_result = line.find(':', line.find(':') + 1)
                                if url in line[:post_result]:
                                    try:
                                        result = line[line.index(' ') + 1:]
                                    except ValueError:
                                        result = line[post_result + 1:]
                            except ValueError:
                                try:
                                    result = line[line.index(' ') + 1:]
                                except ValueError:
                                    pass

                            # Comprobar si se encontró un resultado que no sea UNKNOWN de nombre y si resultado no esta en la lista con los resultado
                            if result != '' and not 'UNKNOWN' in result and not result in result_lines and not result in result_lines:
                                if 'netflix' in url or 'netflix' in url or 'hbo' in url or 'starplus' in url:
                                    # Comprobar si el resultado contiene '@' o es un número
                                    if '@' in result[:result.find(':')] or result[:result.find(':')].isdigit():
                                        result_lines.append(result)
                                else:

                                    result_lines.append(result)

                    # Escribir los resultados en un archivo
                    with open(f'{result_path}result_{site}.txt', 'a',) as file_:
                        for line in result_lines:
                            try:
                                file_.write(line)
                            except:
                                pass

        # Devolver la lista de resultados
        return result_lines
