import math
def es_primo(n):
    if n <= 1:
        return False
    elif n == 2.0:
        return True
    elif n % 2 == 0:
        return False
    for i in range (3, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
def Crear_vector():
    vect=[0]
    tam=int(input("ingrese numero de elementos en el vector "))
    vect=tam*vect
    for i in range(0,tam):
        vect[i]=int(input("ingrese elemento de vector: ")) 
    return vect
Vector=Crear_vector()
cont=0
for elemento in Vector:
    if es_primo(elemento)==True:
        cont=cont+1
print("En este vector hay ",cont," numeros primos")
        
