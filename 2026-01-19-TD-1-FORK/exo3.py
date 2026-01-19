#!/usr/bin/env python3 
# SHEBANG: indique l'interpréteur à utiliser pour exécuter ce script
import os, sys

def do_it():
    os.fork()
    os.fork()
    print("hello!")

if __name__ == "__main__":
    do_it()
    print("salut")
    sys.exit(0)