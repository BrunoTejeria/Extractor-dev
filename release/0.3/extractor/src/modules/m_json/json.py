import json

class Json:
    def __init__(self, json_path, mode_='r'):
        self.file_path = json_path
        self.mode = mode_

    def read(self):
        try:
            with open(self.file_path, mode=self.mode) as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return None

    def edit(self, data):
        with open(self.file_path, mode='w') as file:
            json.dump(data, file, indent=4)

    def delete(self, data):
        pass