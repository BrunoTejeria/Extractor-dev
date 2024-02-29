class File:

    def __init__(self, file):
        self.file = file
        return file

    def clear(self, file):
        with open(file, 'w') as f:
            # The file is reset (cleared)
            pass
        print('archivo reseteado')