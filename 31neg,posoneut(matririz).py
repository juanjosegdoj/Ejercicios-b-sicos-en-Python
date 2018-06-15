def Crear_matriz():
    matriz=[]
    filas=int(input("Cantidad de filas: "))
    columnas=int(input("Cantidad de columnas: "))
    for i in range(filas):
        matriz.append([0]*columnas)
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c]=int(input("elemento %d,%d :"%(f,c)))
    return matriz
matriz=Crear_matriz()
contneg=0
contneu=0
contpos=0
for elemento in matriz:
    for x in elemento:
        if x<0:
            contneg=contneg+1
        elif x==0:
            contneu=contneu+1
        else:
            contpos=contpos+1
print("son negativos: ",contneg,", son neutros: ",contneu,", son positivos: ",contpos)
