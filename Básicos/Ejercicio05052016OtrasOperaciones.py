import random
def crearVector(n):
      v=[]
      for i in range(n):
            v.append(random.randint(1, 200))
      return v

##Programa Principal

vecA=crearVector(10)
#print(vecA)
#print("La Longitud es: ",len(vecA))
vecA.sort()
#print("El vector de Menor a mayor: ",vecA)
vecA.reverse()
#print("El vector de mayor a menor:  ",vecA)
#print("El valor mínimo es: ",min(vecA))
#print("El valor máximo es: ",max(vecA))
elemContar=int(input("Elemento a contar: "))
#print("Numero de veces es:  ",vecA.count(elemContar))
texto=input("Ingrese texto:  ")
ejemSplit=texto.split(" ")
#print(ejemSplit)
ejemList = list(texto)
#print(ejemList)
v=['f','r','f']
seq = ["J", "U", "A"," ","N"]
#print("%%".join( seq ))



