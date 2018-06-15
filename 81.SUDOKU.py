

 #          AQUI SE VA A CREAR EL TABLERO CON ENTRADA PREESTABLECIDAS POR EL CREADOR DEL SUDOKU 

def llenar_tablero(tam):                           # creo la plantilla de el sudoku con las preentradas que me dieron
    table = []                                     # este caso va a estar llena de ceros 
    for i in range(tam):
        table.append(([0]*tam))
        
    for f in range(9):                         # recorro cada una de las entradas de table 
        for c in range(9):                     #
            while True: # creo un ciclo infinito que sólo termina cuando me dan una entrada entre 1 y 9
                var_temp = float(input("{f},{c} : ".format(f=f+1,c=c+1)))    # solicito la entrada, y muestra la posicion en donde se va a meter
                if var_temp ==0:
                    break
                if var_temp >= 1 and var_temp <=9  : 
                    if validador(table,f,c,var_temp):
                        table[f][c] = var_temp
                        break
                    print("No se puede almacenar esa entrada, intente con otro número.")
                print("el numero debe estar entre 1 y 9")
    return table

     # NOTA: En este caso los campos vacios van a ser representados con un cero (0)


# ESTA FUNCION SE ENCARGA DE EVALUAR TODAS LAS CONDICIONES PARA QUE UNA ENTRADA SEA CONSIDERDA CORRECTA 


def validador(tablero,fila,columna,entrada):
    if entrada in tablero[fila]:  # verifico que no este la entrada en la fila que la voy a almacenar
        return False            # en caso de si este retorno False y finaliza la funcion validador

    for i in range(9):
        if tablero[i][columna] == entrada:  # recorro toda la columna viendo si existe mi entrada 
            return False                    # en caso de que si, retorno False y la funcion validador finaliza 

    # y la ultima verificacion (SUBCUADRICULAS) que es un poco dificil porque hay que saber a que seccion
    # del sudoku pertenece la entrada
    interv_total = [[0,1,2],[3,4,5],[6,7,8]]

    # Con los dos siguientes ciclos verifico en que intervalo está la fila y la columna
    
    for i in interv_total:         
        if fila in i:
            interv_fila = i     
            break

    for i in interv_total:
        if columna in i:
            interv_columna = i
            break

    # Ahora procedo a verificar si la entrada esta en la SUBCUADRICULA

    for i in interv_fila:
        for j in interv_columna:
            if tablero[i][j] == entrada:
                return False

    # SI EL ALGORITMO SIGUIE CORRIENDO HASTA AQUI ES PORQUE YA SE HAN CUMPLIDO TODAS LAS CONDICIONES

    return True

def tablero_lleno(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return False
    return True

tablero = llenar_tablero(9)

while not(tablero_lleno(tablero)):  
    while True:
        print( "\nCOOORDENADAS DE LE TABLERO")
        fila = int(input("Ingrese fila: "))-1   # le resto 1 porque la lista debe estar entre 0 y 8
        columna = int(input("Ingrese fila: "))-1  # recordando que una lista empieza desde cero
        entrada = int(input("entrada en las coordenadas antes especificadas: "))
        if entrada>=1 and entrada<=9 and fila>=0 and fila<=8 and columna>=0 and columna<=8: # hay que certifica que las variable, fila, columna
            break                                                                           # esten en un intervalo de [0,8] por obvias razones y
        print("ALGUNA ENTRADA NO ES VALIDA")                                                # entrada que este en un intervalo de [1,9]

    respuesta = validador(tablero,fila,columna,entrada) # llamo la funcion validador 

    if respuesta:
        print("la entrada se pueda colocar ")
    else:
        print("la entrada NO se puede colocar")




####################################################################################################################################################################
####################################################################################################################################################################



    

#                   A PARTIR DE AQUI QUERIA DEMOSTRAR QUE EL EJERCICO EVIDENTEMENTE FUNCIONA
"""
NOTA SUPER IMPORTANTE:

el siguiente ciclo while nunca va a terminar (por eso le puse el contador), este algoritmo no esta en la capacidad de hacer
todo el SUDOKU, pero si que te vas a dar cuenta de todos los pasos logicos que toma el algoritmo y como NO irrumpe ninguna de las
reglas del sudoku.



import random

def tablero_lleno(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return False

tablero = llenar_tablero(9)
cont = 0
while not(tablero_lleno(tablero)):   # mientras el tablero no este lleno, seguir ejecutando entradas
    cont += 1
    respuesta = False
    fila = random.randint(0,8)
    columna = random.randint(0,8)
    entrada = random.randint(1,9)

    if tablero[fila][columna] == 0:
        respuesta = validador(tablero,fila,columna,entrada) 

    if respuesta  and respuesta:
        tablero[fila][columna] = entrada 

    print()
    for i in tablero:
        print(i)
    print()
    if cont == 1500:   # el algoritmo hace 1500 iteraciones antes de salir del programa
        break
for i in tablero:
    print(i)
    

"""
