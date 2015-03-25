# abrimos el archivo solo de lectura
f = open("C:/Users/Dpandales002/Google Drive/COMPARTIDA/PwC/instalados.txt","r")

# Creamos una lista con cada una de sus lineas
lineas = f.readlines()

# cerramos el archivo
f.close()

# abrimos el archivo pero vacio
f = open("C:/Users/Dpandales002/Google Drive/COMPARTIDA/PwC/instalados.txt","w")

# recorremos todas las lineas
for linea in lineas:
    
    # miramos si el contenido de la linea es diferente a la linea a eliminar
    # añadimos al final \n que es el salto de linea
    if linea.startswith('Microsoft')!=-1:
        
        # Si no es la linea que queremos eliminar, guardamos la linea en el archivo
        f.write(lineas)

# cerramos el archivo
f.close()