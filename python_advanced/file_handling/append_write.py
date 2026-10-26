#!/usr/bin/env python3
"""Añade texto UTF-8 al final de un archivo."""


def append_write(filename="", text=""):
    """Añade el texto indicado y devuelve los caracteres escritos."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
