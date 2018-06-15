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
print(matriz)
silla=0
for elemento in matriz:
    filaMEN=(elemento.index(min(elemento)))
    cont=0
    for i in range(0,columnas):
        if matriz[i][filaMEN] > min(elemento):
            cont=cont-1
        else:
            cont=cont+1
    if cont==3:
        silla=silla+1
if silla==1:
    print("En esta matriz hay una silla")
else:
    print("En esta matriz no hay sillas")
         

    
                
            
        
    
