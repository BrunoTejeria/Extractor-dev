class Lines:

    #lineas_cantidad = Lines(file=text_file)
    #lineas_cantidad.count()

    def __init__(self,file_search):
        with open(file=file_search,
            mode='r',
            encoding='utf-8'
        ) as file:
            lines = file.readlines()
            file.close()
        self.lines = lines

    def count(self):
        total_lines = sum(1 for line in self.lines)
        self.count = total_lines