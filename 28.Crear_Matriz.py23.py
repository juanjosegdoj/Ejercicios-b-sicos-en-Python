def Crear_matriz(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([0]*columnas)
    for f in range(filas):
        for c in range (columnas):
            matriz[f][c]=int(input("elemento %d,%d : "%(f,c)))
    return matriz
filas=int(input("ingrese numero de filas: "))
columnas=int(input("ingrese numero de columnas: "))
matriz=Crear_matriz(filas,columnas)

    
                
