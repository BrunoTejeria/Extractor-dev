from ..m_file.file import File
from ..m_config.config import Config
from tqdm import tqdm
# Ruta del archivo de configuracion
config_path = 'extractor/etc/config.json'

class ConfigValues(Config):
    def __init__(self):
        config_json = Config(config_path)
        config = config_json.read()
        self.url =  config[1]['url']
        self.file_search =  config[0]['textFile']['textSearch']
        self.file_result = config[0]['textFile']['textResult']


class Check(File, ConfigValues):
    def __init__(self):

        # Heredar de clase ConfigValuesd
        ConfigValues.__init__(self)

        # Heredar de clase File
        File.__init__(self, self.file_search, self.file_result)
        File.read(self)


    def process_lines(self):
        result_lines = []

        with tqdm(total=len(self.lines), desc="Procesando", unit=" línea", colour='blue') as progress_bar:
            for line in self.lines:
                progress_bar.update(1)
                if line != '\n':
                    if self.url in line:
                        result = ''
                        try:
                            post_result = line.find(':', line.find(':') + 1)
                            if self.url in line[:post_result]:
                                try:
                                    result = line[line.index(' ') + 1:]
                                except ValueError:
                                    post_result = line.find(':', line.find(':') + 1)
                                    result = line[post_result + 1:]
                        except ValueError:
                                try:
                                    result = line[line.index(' ') + 1:]
                                except ValueError:
                                    pass
                        if result != '':
                            result_lines.append(result)

            with open(self.file_result, 'a',) as file_:
                for line in result_lines:
                    try:
                        file_.write(line)
                    except:
                        pass


        return result_lines


'''text_file = 'working/etc/data/text.txt'
check_obj = Check(text_file, 'https://github.com/')
processed_lines = check_obj.process_lines()
print(processed_lines)'''
