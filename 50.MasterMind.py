import random
while True:
    digitos=int(input("ingrese numero de digitos: "))
    if digitos>1 and digitos<11:
        break
    print("debe ser un numero entre 2 y 10")
while True:
    x="r"
    respuesta = random.randint(10**(digitos-1),(10**digitos)-1)
    vector=[]
    for i in str(respuesta):
        if int(i) in vector:
            x="h"
        vector.append(int(i))
    if x=="r":
        break
while True:
    while True:
        numero=input("ingrese un numero: ")
        if digitos==len(numero):
            break
        print("Recuerde que el tamaño de el numero debe ser de ",digitos)
    vector2=[]
    for i in numero:
        vector2.append(int(i))
    cooincidencias=0
    for i in vector:
        if i in vector2:
            cooincidencias+=1
    print("cooincidencias: ",cooincidencias)
    aciertos=0
    for i in range(digitos):
        if vector[i]==vector2[i]:
            aciertos+=1
    print("aciertos: ",aciertos)
    if aciertos==digitos:
        print("has ganado tio!!!")
        break
    
        

