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
def crear_vector():
    v=[0]
    tam=int(input("ingrese tamaño de vector: "))
    v=v*tam
    for i in range(0,tam):
        v[i]=int(input("ingrese numero: "))
    return v
vector=crear_vector()
cont=0
for f in range(0,len(vector)):
    x=es_primo(vector[f])
    if x==True:
        cont=cont+1
print("el numero de primos en el vector: ",cont)

    
