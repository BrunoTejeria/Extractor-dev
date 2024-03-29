try:
    from rich.console import Console
    from rich import print
    from rich.prompt import Prompt
except ImportError:
    print('[!] Error al importar rich')
except:
    print('[!] Error')

from ..m_check.check import (
    Check
)




# Crear objeto para chequear
search = Check()

# Crear objeto de configuracion
#config = Config()

# Crea una instancia de la consola Rich
console = Console()



# Banner
text = \
'''
:::::::::: :::    ::: ::::::::::: :::::::::      :::      ::::::::  :::::::::::  ::::::::  :::::::::  
:+:        :+:    :+:     :+:     :+:    :+:   :+: :+:   :+:    :+:     :+:     :+:    :+: :+:    :+: 
+:+         +:+  +:+      +:+     +:+    +:+  +:+   +:+  +:+            +:+     +:+    +:+ +:+    +:+ 
+#++:++#     +#++:+       +#+     +#++:++#:  +#++:++#++: +#+            +#+     +#+    +:+ +#++:++#:  
+#+         +#+  +#+      +#+     +#+    +#+ +#+     +#+ +#+            +#+     +#+    +#+ +#+    +#+ 
#+#        #+#    #+#     #+#     #+#    #+# #+#     #+# #+#    #+#     #+#     #+#    #+# #+#    #+# 
########## ###    ###     ###     ###    ### ###     ###  ########      ###      ########  ###    ### 
'''

# Tabla con las opciones
table_menu = \
'''
[green]1.[/green] [red]Buscar[/red]
[green]2.[/green] [red]Configuración[/red]
[green]3.[/green] [red]Bla Bla[/red]
[green]0.[/green] [red]Salir[/red]

'''

table_config = \
'''
[green]1.[/green] [red]Desactivar Urls[/red]
[green]2.[/green] [red]Agregar Url[/red]
[green]3.[/green] [red]Bla Bla[/red]
[green]0.[/green] [red]Salir[/red]

'''





def config():
    print(f'[green]{text}[/green]')
    while True:
        console.print(table_config)
        selected_option = Prompt.ask('Selecciona una opción (ingresa 0 para salir):', choices=['0','1','2','3'])

        if selected_option == "1":
            console.print("Has seleccionado 'Buscar'", style="bold green")
            a = search.process_lines()
            console.clear

        elif selected_option == "2":
            console.print("Has seleccionado 'Configuración'", style="bold green")

        elif selected_option == "3":
            console.print("Has seleccionado 'Opción 3'", style="bold green")

        elif selected_option == "0":
            console.print("Saliendo...", style="bold red")
            break
        else:
            console.print("Opción no válida.", style="bold red")















# Funcion para ejecutar el programa
def main():
    print(f'[green]{text}[/green]')
    while True:
        console.print(table_menu)
        selected_option = Prompt.ask('Selecciona una opción (ingresa 0 para salir):', choices=['0','1','2','3'])

        if selected_option == "1":
            console.print("Has seleccionado 'Buscar'", style="bold green")
            a = search.process_lines()
            console.clear

        elif selected_option == "2":
            console.print("Has seleccionado 'Configuración'", style="bold green")
            config()

        elif selected_option == "3":
            console.print("Has seleccionado 'Opción 3'", style="bold green")

        elif selected_option == "0":
            console.print("Saliendo...", style="bold red")
            break
        else:
            console.print("Opción no válida.", style="bold red")

