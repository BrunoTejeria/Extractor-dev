from ..m_check.check import (
    Check
)
from rich.console import Console
from rich import print
from rich.table import Table

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

from curses import *

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
"""def init():
    print(f'[green]{text}[/green]')
    # Crear una instancia de la clase Table
    table = Table()

    # Definir las columnas de la tabla
    table.add_column("Nombre", style="bold")
    table.add_column("Edad", justify="center")
    table.add_column("Ciudad")

    # Agregar filas a la tabla
    table.add_row("Juan", "30", "Madrid")
    table.add_row("María", "25", "Barcelona")
    table.add_row("Carlos", "40", "Valencia")

    # Crear una instancia de la clase Console para mostrar la tabla
    console = Console()
    console.print(table)
    curses.wrapper(main)



    '''check_obj = Check()
    processed_lines = check_obj.process_lines()'''"""
    