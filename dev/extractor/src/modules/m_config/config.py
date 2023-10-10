from ..m_json.json import Json

path = 'extractor/etc/config.json'

class Config(Json):
    def __init__(self, json_path, mode_='r'):
        super().__init__(json_path, mode_)

    def get_content(self):
        return self.read()

# Crear una instancia de la clase Config
config = Config(path)
# Leer el contenido del archivo JSON
data = config.get_json_content()

print(data)
