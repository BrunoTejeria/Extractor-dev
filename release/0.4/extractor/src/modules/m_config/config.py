from ..m_json.json import Json

path = 'extractor/etc/config.json'

class Config(Json):
    def __init__(self, config_path, mode_='r', data=''):
        super().__init__(config_path, mode_)
        super().read()
        



