#!/usr/bin/env python3
"""Escribe texto UTF-8 en un archivo y devuelve los caracteres escritos."""


def write_file(filename="", text=""):
    """Sobrescribe el archivo con el texto indicado."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
