"""
Por: Juan José Giraldo Jimenez

Objetivo:
La explicación está en el punto 2 de la página:
    http://ingeniero.wahio.com/ejercicios-con-while/
    
"""
def centro(n):
    centro=n-1
    while True:
        mayor,menor=0,0
        for i in range(1,n+1):
            if i>centro:
                mayor+=i
            elif i<centro:
                menor+=i
            if mayor==menor:
                return "este es centro numerico: ",centro
        centro-=1
        if mayor>menor:
            return "no tiene centro"
print (centro(int(input(": "))))
