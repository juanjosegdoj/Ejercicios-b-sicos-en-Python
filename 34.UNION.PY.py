def crear_vector():
    v=[0]
    tam=int(input("ingrese tamaño de vector: "))
    v=v*tam
    for i in range(0,tam):
        v[i]=int(input("ingrese numero: "))
    return v
A=crear_vector()
B=crear_vector()
UNION=A+B
UNION.sort() 
cont=0   ##Nro de elementos sin repetir(cont)
l="s"
vec=[]  
for i in range(0,len(UNION)):
   x=UNION[i]
   if x!=l:
        cont=cont+1
        vec.append(x)
        l=x
print("la UNION entre el conjunto A y el conjunto B es: ",vec)
