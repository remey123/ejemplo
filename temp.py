# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

try:
    archivo = open("texto-guardado.txt", "w")
    archivo.write("usé python para escribir un archivo")
except:
    print("No pude abrir el archivo")
finally: 
    archivo.close()
    
    
    print ("Archivo cerrado")
    print("archivo abierto")
    
if __name__ == "__main__":
    pass