from ..m_file.file import File
from ..m_config.config import Config
from tqdm import tqdm
import json
# Ruta del archivo de configuracion
config_path = 'extractor/etc/config.json'
result_path = 'extractor/etc/data/processed_data/'
class Check(File, Config):
    def __init__(self):
        config_json_class = Config(config_path)
        config = config_json_class.read()
        
        self.file_search =  config[0]['textFile']['textSearch']
        self.file_result = config[0]['textFile']['textResult']
        File.__init__(self, self.file_search, self.file_result)
        File.read(self)
        self.url = config


    def process_lines(self):
        
        count = 1
        File.reset(self)
        for site in self.url[1]['url']:
            file_result = self.file_result
            print(site)
            with tqdm(total=len(self.lines*2), desc="Procesando", unit=" línea", colour='blue') as progress_bar:
                result_lines = []
                
                for search in self.url[1]['url'][site]:
                    url = self.url[1]['url'][site][search]
                    for line in self.lines:
                        
                        progress_bar.update(1)
                        if line != '\n' and url in line:
                            result = ''
                            try:
                                post_result = line.find(':', line.find(':') + 1)
                                if url in line[:post_result]:
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
                            if result != ''and not 'UNKNOWN' in result and not result in result_lines:
                                result_lines.append(result)

                    with open(f'{result_path}result_{site}.txt', 'a',) as file_:
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
