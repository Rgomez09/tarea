import os

nombre_carpeta = 'carpeta'

contenido = os.listdir(nombre_carpeta)

print(f'Los ficheros de {nombre_carpeta} son:')
for elemento in contenido:
    ruta_completa = os.path.join(nombre_carpeta, elemento)
    if os.path.isfile(ruta_completa):  
        print(elemento, ruta_completa, sep=', ')#ruta completa

print()

print(f'Las carpetas de {nombre_carpeta} son:')
for elemento in contenido:
    ruta_completa = os.path.join(nombre_carpeta, elemento)
    if os.path.isdir(ruta_completa):  
        print(elemento, ruta_completa, sep=', ')#nombre del elemento y ruta completa