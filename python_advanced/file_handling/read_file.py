#!/usr/bin/env python3
"""Lee e imprime el contenido de un archivo de texto UTF-8."""


def read_file(filename=""):
    """Imprime el contenido del archivo sin añadir otra nueva línea."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
