import os 
#yield en Python es muy particular, y es muy diferente de un return.

#Se usa para retornar "generators", objetos iteradores que se comportan de manera muy similar a una lista.

#Veamos primero un ejemplo:
def contador(max):
    n=0
    while n < max:
            yield n
            n=n+1

mycont = contador(5)

for i in mycont:
    print(i)

for i in mycont:  ##esto quiere decir que no se puede recorrer más de una vez
    print(i)

print(mycont)
print("")
print("Si desea más informacion sobre el operador YIELD, PRESIONE 1 : ")
x=int(input())
if x==1:
    os.system("start http://es.stackoverflow.com/questions/6048/cu%C3%A1l-es-el-funcionamiento-de-yield-en-python")
    


