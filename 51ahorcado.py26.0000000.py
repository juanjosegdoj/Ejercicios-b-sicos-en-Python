def ya_existe(ingresadas, letra):
    for i in range(0, len(ingresadas)):
        if ingresadas[i] == letra:
            return True
    return False
 
def ganador(juego):
    for i in range(0, len(juego)):
        if juego[i] == '-':
            return False
    return True
 
solucion = 'LISTA'
juego = ['-', '-', '-', '-', '-']
vidas = 6
ingresadas = []
while True:
    print
    print ('Le quedan ', vidas)
    print ('Ha ingresado ', ingresadas)
    print (juego)
 
    letra = input('Digite una letra ')
    if ya_existe(ingresadas, letra) == True:
        print ('Digite otra letra')
    else:
        ingresadas.append(letra)
        pierde_vida = True
        for i in range(0, len(solucion)):
            if solucion[i] == letra:
                juego[i] = letra
                pierde_vida = False
 
        if pierde_vida == True:
            vidas = vidas - 1
 
        if vidas == 0:
            print ('PIERDE')
            break
        if ganador(juego) == True:
            print ('GANA')
            break
         
