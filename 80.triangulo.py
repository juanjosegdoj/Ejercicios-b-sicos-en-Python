import math
def convertir(lista):
    string=""
    for i in lista:
        string+=str(i)
    return(string)
string=[]
x=int(input("Ingrese numero: "))
if x%2!=0:
    for i in range(1,x+1):
        if i<=math.ceil(x/2):
            string.append("X")
            print(convertir(string))
        else:
            string.pop()
            print(convertir(string))
else:
    for i in range(1,x+1):
        if i<=x/2:
            string.append("X")
            print(convertir(string))
        elif i==x/2+1:
            print(convertir(string))
        else:
            string.pop()
            print(convertir(string))

