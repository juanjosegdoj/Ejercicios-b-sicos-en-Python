"""
Por Juan José Giraldo Jimenez
Objetivo:
La explicación del ejercicio se encuentra en el punto 1 de:
http://ingeniero.wahio.com/ejercicios-con-while/
"""

x=input(":: ")
if len(x)==1:
    x+="0"
v=[int(x[-2]),int(x[-1])]
while v[len(v)-1]<int(x):
    v.append(v[-2]+v[-1])
if v[-2]==int(x):      #######
    print("si está")   #######
else:                  #######
    print("No está")   #######

# Las lineas que están marcadas (######) se podian reemplazar por lo siguiente:
"""
if int(x) in v:
    print ("si está")

Pero esto es mas lento porque recorre la lista en orden y teniendo
en cuenta que si el numero está, se encontraria en el penultima posición
"""
