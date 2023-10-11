from ..m_json.json import Json

path = 'extractor/etc/config.json'

class Config(Json):
    def __init__(self, json_path, mode_='r', data=''):

        super().__init__(json_path, mode_)
        super().read()
        """ opciones edit y delete hay que terminar
        super().edit(data)
        super().delete(data)
        """


