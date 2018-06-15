def suma_de_matriz(matriz):
    suma=0
    for i in matriz:
        suma+=sum(i)
    return(suma)
    
def tablero():
    matriz=[]
    for i in range(10):
        matriz.append([0]*10)
    return(matriz)

def posbarcos(jugador1):
    for k in range(4):
        while True:
            fila=int(input("Ingrese fila: "))
            columna=int(input("Ingrese columna: "))
            if fila>-1 and fila<11 and columna>-1 and columna<11:
                break
            print("las coordenadas salen de el tablero, ingrese nuevamente: ")
        jugador1[fila][columna]=1
        print("ORIENTACION: derecha, izquierda, arriba o abajo")
        orien=str(input("Orientacion del barco: "))
        jugador1[fila][columna]=1
        for i in range(k+1):
            if orien=="derecha":
                jugador1[fila][columna+i]=1
            elif orien=="izquierda":
                jugador1[fila][columna-i]=1
            elif orien=="abajo":
                jugador1[fila+i][columna]=1
            elif orien=="arriba":
                jugador1[fila-i][columna]=1
            else:
                print("Este barco no ingresó a la matriz")
    return jugador1

def jugando(jugador1,jugador2):
    while suma_de_matriz(jugador1)!=0 and suma_de_matriz(jugador2)!=0:
        print("                         Turno de jugador1")
        print("                         Ingrese coordenadas de tiro")
        fila=int(input("                         ingrese fila: "))
        columna=int(input("                         ingrese columna: "))
        if jugador2[fila][columna]==1:
            print("                          Exploto!!!")
            jugador2[fila][columna]=0
        if suma_de_matriz(jugador1)==0:
            return ("todos los barcos destruidos, el jugador2 ha ganado")
        print("Turno de jugador2")
        print("Ingrese coordenadas de tiro")
        fila=int(input("ingrese fila: "))
        columna=int(input("ingrese columna: "))
        if jugador1[fila][columna]==1:
            print("Exploto!!!")
            jugador1[fila][columna]=0
        if suma_de_matriz(jugador2)==0:
            return ("todos los barcos destruidos, el jugador1 ha ganado")

print("TABLERO DE JUGADOR 1")
jugador1=tablero()
x=posbarcos(jugador1)
for bid in x:
    print(bid)
print("TABLERO DE JUGADOR 2") 
jugador2=tablero()
y=posbarcos(jugador1)
for bid in y:
    print(bid)
print("¡A JUGAR!")
print(jugando(jugador1,jugador2))


    
        


