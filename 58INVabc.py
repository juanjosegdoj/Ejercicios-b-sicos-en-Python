"""
Por: Juan José Giraldo Jimenez

Imprimir el abecedario en forma inversa es decir de la 20 a la 1 y luego
vaya eliminando de una letra en una empezando por la z hasta que quede la a.

"""

v,i=[],90
while(i!=64):
    v.append(chr(i))
    i-=1
for i in range(26):
    print(v)
    v.pop(0)

"""

x=['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
for i in range(26):
    print(x)
    x.pop(0)

"""
