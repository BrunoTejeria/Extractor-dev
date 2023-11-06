import numpy as np

class File:

    def __init__(self,file_search='', file_write=''):
        self.file_read = file_search
        self.file_write = file_write
        return self.file_read, self.file_write

    def read(self):
        with open(file=self.file_read, mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            file.close()
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
            return True
        except:
            print('error')