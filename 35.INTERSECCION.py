def crear_vector():
    v=[0]
    tam=int(input("ingrese tamaño de vector: "))
    v=v*tam
    for i in range(0,tam):
        v[i]=int(input("ingrese numero: "))
    return v
A=crear_vector()
B=crear_vector()
inter=[]
for i in range(0,len(A)):
    for k in range (0,len(B)):
        if A[i]==B[k]:
            inter.append(A[i])
print("la interseccion es del conjunto A y el B es: ",inter)
