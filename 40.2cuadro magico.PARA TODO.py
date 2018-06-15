def matrices(filCOL):
    matriz=[]
    for i in range(filCOL):
        matriz.append([0]*filCOL)
    for f in range(filCOL):
        for c in range (filCOL):
            matriz[f][c]=int(input("Elemento: ")) 
    return matriz
tamaño=int(input("¿De qué tamaño desea la matriz?"))
matriz=(matrices(tamaño))
x="h"
for elemento in matriz:
    print(elemento)
suma=sum(matriz[0])
for k in range(len(matriz[0])):
    cont=0
    for m in range(len(matriz[0])):
        cont=cont+matriz[m][k]
    if cont!=suma:
        x="sale"
        break
if x!="sale":
    for i in range(len(matriz)):
        if sum(matriz[i])!=suma:
            x="sale"
            break
hor=0
for f in range(len(matriz)):
    for c in range (len(matriz)):
        if f==c:
            hor=hor+matriz[f][c]
if hor!=suma:
    x="sale"
hor=0
for f in range(len(matriz)):
    for c in range (len(matriz)):
        if f+c==len(matriz)-1:
            hor=hor+matriz[f][c]
if suma!=hor:
    x="sale"
if x!="sale":
    print("Esta matriz efectivamente es un cuadro magico")
else:
    print("Esta matriz, no es un cudro mágico")
    

    
            
    
    

    
        
    
