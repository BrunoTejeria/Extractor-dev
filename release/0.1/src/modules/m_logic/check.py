class Check:
    def __init__(self, text_file, url):
        self.lines = Lines
        self.url = url

        with tqdm(total=Lines.count, desc="Procesando", unit=" línea", colour='blue') as progress_bar:
            for line in lines:
                progress_bar.update(1)
                if line != '\n':
                    if url in line:
                        try:
                            result = line[line.index(' ') + 1:]
                        except ValueError:
                            post_result = line.find(':', line.find(':')  + 1)
                            result = line[post_result + 1:]
                        lines.append(result)