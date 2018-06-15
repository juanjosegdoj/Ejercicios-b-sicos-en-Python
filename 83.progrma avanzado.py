import itertools

def operar(numeros,operadores):
    soluc = [numeros[0],operadores[0],numeros[1],operadores[1],numeros[2],operadores[2],numeros[3]]
    print(soluc,end=" = ")

    # TOCA PONERME COMO UN MARICA A DIFINIR OPERACIONES BÁSICAS DE +,-,*,/
             
    while True :                        # las multiplicaciones
        if not("*" in soluc):
            break
        x = soluc.index("*")
        re = soluc[x-1]*soluc[x+1]
        soluc[x-1] = re
        soluc.pop(x)
        soluc.pop(x)

             
    while True :                      # las divisiones
        if not("/" in soluc):
            break
        x = soluc.index("/")
        re = soluc[x-1]/soluc[x+1]
        soluc[x-1] = re
        soluc.pop(x)
        soluc.pop(x)
             


    while True :                      # las sumitas
        if not("+" in soluc):
             break
        x = soluc.index("+")
        re = soluc[x-1]+soluc[x+1]
        soluc[x-1] = re
        soluc.pop(x)
        soluc.pop(x)


    while True :
        if not("-" in soluc):
            break
        x = soluc.index("-")             # y las resticas
        re = soluc[x-1]-soluc[x+1]
        soluc[x-1] = re
        soluc.pop(x)
        soluc.pop(x)

    print(soluc[0])
    return soluc[0]
    

def buscar_solucion(grupo):
    numeros = grupo[:-1]  # excluyo el último ya que es el resultado
    objetivo = grupo[-1] # obtengo el último numero ingresado

    operadores = []
    operd_1 = list(map(list, itertools.combinations_with_replacement(["+","-","/","*"],3))) # todas las posibles combinaciones con repeticion
    
    for i in operd_1:
        y = list(map(list,itertools.permutations(i,3)))

        
        for k in y :
            if not(k in operadores):
                operadores.append(k)

    comb_REP = []
    comb = list(map(list, itertools.combinations_with_replacement(numeros,4)))
    
    for i in comb:
        if not(i in comb_REP):
            comb_REP.append(i)

    for grup in comb_REP:
        
        r = list((map(list,itertools.permutations(grup,4))))
        x = []
        for i in r:
            if i not in x:
                x.append(i)
        
        for op in operadores:     
            for perm in x:
                resultado = operar(perm,op)
                if resultado == objetivo:
                    print("la operación anterior a solucionado el problema: ",resultado)
                    archivo = open("resultado.txt","a")
                    archivo.write(str(resultado))           
                    archivo.close() 

                        
                    return

    print("No existe solucón para el problema")
            

numeros = [float(input("ingrese numero "+str(i+1)+": ")) for i in range(5)]
print("este proceso va a tardar un par de horas, le recomendamos que deje compilando y acuestese a dormir")
input("Continuar")

buscar_solucion(numeros)



