from ..m_file import File
from tqdm import tqdm

class Check(File):
    def __init__(self, file_search, file_result, url):
        super().__init__(file_search, file_result)
        super().read()
        self.url = url


    def process_lines(self):
        result_lines = []

        with tqdm(total=len(self.lines), desc="Procesando", unit=" línea", colour='blue') as progress_bar:
            for line in self.lines:
                progress_bar.update(1)
                if line != '\n':
                    if self.url in line:
                        try:
                            result = line[line.index(' ') + 1:]
                        except ValueError:
                            post_result = line.find(':', line.find(':') + 1)
                            result = line[post_result + 1:]
                        File.write(self, content=result, mode='a')
                        result_lines.append(result)

        return result_lines


'''text_file = 'working/etc/data/text.txt'
check_obj = Check(text_file, 'https://github.com/')
processed_lines = check_obj.process_lines()
print(processed_lines)'''
