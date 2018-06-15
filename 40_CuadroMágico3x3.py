def Crear_matriz():
    matriz=[]
    for i in range(3):
        matriz.append([0]*3)
    for f in range(3):
        for c in range (3):
            matriz[f][c]=int(input("elemento %d,%d : "%(f,c)))
    return matriz
def filas(matriz):
    for i in range(1,4):
        for elemento in matriz:
            if sum(elemento)!=15:
                return False
        return True
def Columnas(matriz):
    cont=0
    for f in range(0,3):
        for c in range(0,3):
            cont=matriz[f][c]+cont
        if cont!=15:
            return False
        return True
def diagonal(matriz):
    cont=0
    inv=0
    for f in range(0,3):
        for c in range(0,3):
            if f==c:
                cont=matriz[f][c]+cont
            if f+c==2:
                inv=matriz[f][c]+inv
    if cont!=15 and inv!=15:
        return False
    return True 
print("RECUERDE QUE ESTE ALGORITMO SOLO FUNCIONA PARA CUADROS DE 3*3")
matriz=Crear_matriz()
if True==(filas(matriz))and(Columnas(matriz))and(diagonal(matriz)):
    print("es uncuadro magico")
else:
    print("No es un cuadro magico")


    

