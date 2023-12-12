from ..

class Check():
  def __init__(self):
      # Leer la configuración
      self.config = Config(config_path).read

      # Llamar al constructor de la clase Config
      Config.__init__(self, config_path)




      # Iterar entre documentos de texto y extraer sis lineas
      self.file_lines = []
      for text in self.config[0]["textFile"]:
          if os.path.exists(text):
              file = File(text)
              file.read()
              for line in file.lines:
                  self.file_lines.append(line)