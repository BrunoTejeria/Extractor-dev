try:
    import os
except:
    print("[!] Error al importar os")
    quit()

try:
    import json
except:
    print("[!] Error al importar json")
    quit()


"""try:"""
from rich.console import Console
from rich.prompt import Prompt
from rich import print
"""except ImportError as error:
    print(f'[!] Error al importar "{error.name}: {error.args[0]}"')
    reinstall(Q=True)"""


try:
    from ..m_check.check import Check
except:
    print("[!] Error al importar Check")
    quit()


# Crear objeto para chequear
search = Check()

# Crear objeto de configuración
# config = Config()

# Crea una instancia de la consola Rich
console_rich = Console()


# Banner
text = """
:::::::::: :::    ::: ::::::::::: :::::::::      :::      ::::::::  :::::::::::  ::::::::  :::::::::  
:+:        :+:    :+:     :+:     :+:    :+:   :+: :+:   :+:    :+:     :+:     :+:    :+: :+:    :+: 
+:+         +:+  +:+      +:+     +:+    +:+  +:+   +:+  +:+            +:+     +:+    +:+ +:+    +:+ 
+#++:++#     +#++:+       +#+     +#++:++#:  +#++:++#++: +#+            +#+     +#+    +:+ +#++:++#:  
+#+         +#+  +#+      +#+     +#+    +#+ +#+     +#+ +#+            +#+     +#+    +#+ +#+    +#+ 
#+#        #+#    #+#     #+#     #+#    #+# #+#     #+# #+#    #+#     #+#     #+#    #+# #+#    #+# 
########## ###    ###     ###     ###    ### ###     ###  ########      ###      ########  ###    ### 
"""

# Tabla con las opciones
table_menu = """
[green]1.[/green] [red]Buscar[/red]
[green]2.[/green] [red]Configuración[/red]
[green]3.[/green] [red]Bla Bla[/red]
[green]0.[/green] [red]Salir[/red]

"""

table_config_url = """
[green]1.[/green] [red]Desactivar/Activar Urls[/red]
[green]2.[/green] [red]Agregar Url[/red]
[green]3.[/green] [red]Bla Bla[/red]
[green]0.[/green] [red]Salir[/red]

"""


# Función para configurar
def config():
    # Función para configurar sitios
    def site():
        # Crear lista de opciones para la tabla de configuración de urls
        table_config_url_choices = [0]
        for site in search.config[1]["site"]:
            table_config_url_choices.append(site)

        table_config_url_choices_index_str = str(list(range(1, len(table_config_url_choices) + 1)))
        table_config_url_choices_index_int = list(range(1, len(table_config_url_choices) + 1))

        # Bucle para seleccionar el sitio a configurar
        while True:
            console_rich.print("Selecciona el sitio el cual quieres configurar:")
            index = 1
            for site in table_config_url_choices:
                console_rich.print(f"[green]{index}.[/green] [red]{site}[/red]")
                index += 1
            # Preguntar al usuario por la opción seleccionada

            while not selected_option in table_config_url_choices_index_str:
                selected_option = input("Selecciona una opción (ingresa 0 para salir):")
                if not selected_option in table_config_url_choices_index_str:
                    console_rich.print(f"[bool red]Opción no válida[/bool red]")

            selected_option = Prompt.ask("Selecciona una opción (ingresa 0 para salir)", choices=table_config_url_choices_index_str, show_choices=True)
            print(int(selected_option))
            selected_option = table_config_url_choices[int(selected_option) - 1]
            if selected_option == 0:
                break
            console_rich.print(f"Sitio seleccionado: [green]{selected_option}[/green]")

            # Bucle para configurar el sitio seleccionado
            while True:
                console_rich.clear()
                print(f"[green]{text}[/green]")
                console_rich.print(table_config_url)
                selected_option = Prompt.ask("Selecciona una opción (ingresa 0 para salir):", choices=["0", "1", "2", "3"],)
                if selected_option != 0:
                    with open(search.config, "r") as file:
                        data = json.load(file)
                        print(data)
                else:
                    break

    # Función para configurar urls
    def text_read():
        console_rich.clear()
        console_rich.print("Pon en documento de texto en la carpeta 'extractor/etc/data/raw_data' y luego pon el nombre con su .txt")
        text_doc = Prompt.ask("Nombre de documento")
        # Dumpear json

    # Función para configurar urls
    def text_write():
        pass

    selected_option = Prompt.ask("Opcion")
    if selected_option == "1":
        site()
    elif selected_option == "2":
        text_read()

# Función para ejecutar el programa
def main():
    print(f"[green]{text}[/green]")
    while True:
        console_rich.print(table_menu)
        selected_option = Prompt.ask("Selecciona una opción (ingresa 0 para salir):", choices=["0", "1", "2", "3"],)

        if selected_option == "1":
            console_rich.print("Has seleccionado 'Buscar'", style="bold green")
            search.process_lines()
            console_rich.clear

        elif selected_option == "2":
            console_rich.print("Has seleccionado 'Configuración'", style="bold green")
            config()

        elif selected_option == "3":
            console_rich.print("Has seleccionado 'Opción 3'", style="bold green")

        elif selected_option == "0":
            console_rich.print("Saliendo...", style="bold red")
            break
        else:
            console_rich.print("Opción no válida.", style="bold red")
