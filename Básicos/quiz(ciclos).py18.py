numero=float(input("Ingrese numero: "))
numero=numero*1.0
if numero>=0:
    p=numero
    i=0
    while i!=p:
        i=p
        p=(numero/p+p)/2
    print("Resultados es: ", p)

else :
    print("Numero incorrecto")
