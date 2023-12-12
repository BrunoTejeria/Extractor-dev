# Método para procesar líneas del archivo
def process_lines(self):
  # Obtener las líneas del archivo
  file_lines = self.file_lines
  print(self.create_dirs())

  count: int = 1
  for site in self.config[1]['site']:
    exception = False

    # Configurar archivo de salida
    search_type: dict = self.config[1]['site'][site]['genere']
    file_path = f'{result_path}/{search_type}/{site}.txt'
    print(file_path)

    # Imprimir en qué se está buscando
    console.print(
      f'''
      [bold red]{site}[/bold red]
      '''
    )

    # Obtener el tipo de búsqueda (mail, user, all)
    userType = self.config[1]['site'][site]['type']

    # Inicializar listas para los resultados
    results: list = []
    result_lines: list = []

    # Crear una barra de progreso con tqdm
    with tqdm(total=sum(1 for i in file_lines) * len(self.config[1]['site'][site]['searchSites']),
              desc="Procesando", unit="línea", colour='green', unit_scale=True) as progress_bar:

      # Iterar a través de las URL y búsquedas en la configuración
      for searchSite in self.config[1]["site"][site]["searchSites"]:
        url = self.config[1]['site'][site]["searchSites"][searchSite]

        # Iterar a través de las líneas del archivo de búsqueda
        result: str = ''

        # Iterar entre líneas del archivo
        for line in file_lines:

          # Actualizar la barra de progreso
          progress_bar.update(1)

          # Tomar user:pass
          post_result = line.find(':', line.find(':') + 1)

          # Comprobar si la URL está en la línea
          if url in line[:post_result] and post_result != ":":
            result = line[post_result + 1:]
            result_lines.append(result)
