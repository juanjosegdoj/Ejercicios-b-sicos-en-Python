import random
def crearVector(n):
      v=[]
      for i in range(n):
            v.append(random.randint(1,5))
      return v

##Programa Principal

vector=crearVector(10)
print(vector)
elemBus=int(input("Ingrese número a buscar:  "))
if elemBus in vector: ##Devuelve true si lo encuentra
      print("Indice es: ",vector.index(elemBus))  ## Devuelve la posición del elemento buscado
else:
      print("Número no se encuentra")
##Borra el último
vector.pop()
print("Luego de Borrar el último Elemento(POP) ",vector)
elemBor=int(input("Ingrese número a borrar:  "))
if elemBor in vector:
      vector.remove(elemBor)
      print("Sin elemento:  ",vector)
else:
      print("Elemento no existe")
pos=int(input("Posición:  "))
elemInse=int(input("Elemento a insertar:  "))
vector.insert(pos,elemInse)
print("Luego de Insertar el elemento: ",vector)
vec2=crearVector(5)
vector.append("---")
vector.extend(vec2)
print("Vector mas:  ",vector)
