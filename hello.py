#!/usr/bin/env python3
"""Hello World multi-languages

Depending on the language configured in the environment, the program displays
the corresponding message.

HOW TO USE:
Have the `LANG` variable properly configured, i.e.:

    $ export LANG=pt_BR

HOW TO RUN:
    python3 hello.py
    OR
    ./hello.py
    OR
    LANG=pt_BR ./hello.py
"""

__version__ = "0.0.1"
__author__  = "João Cardoso"
__licence__ = "Unlicence"

import os

current_language = os.getenv("LANG")[:5]

def printing_upper_word():
    if current_language == "pt_BR":
        message = "olá, mundo!"
        print(message.capitalize())
    elif current_language == "it_IT":
        message = "ciao, mondo!"
        print(message.capitalize())
    elif current_language == "es_SP":
        message = "hola, mundo!"
        print(message.capitalize())
    elif current_language == "fr_FR":
        message = "bonjour, monde!"
        print(message.capitalize())
    else:
        message = "hello, world!"
        print(message.capitalize())

if __name__ == "__main__":
    printing_upper_word()