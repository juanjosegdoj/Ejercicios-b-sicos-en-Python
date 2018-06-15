##ENCRIPTADO
matriz=[["A","F","K", "P","U"], ["B", "G", "L", "Q" , "V"], ["C", "H", "M", "R", "X"], ["D", "I", "N", "S", "Y"],["E", "J", "O", "T", "Z"]]
texto=str(input("ingrese texto: ")).upper()
lista=[]
for letra in texto:
    for f in range(len(matriz[0])):
        for c in range(len(matriz)):
            if matriz[f][c]==letra:
                lista.append(f+1)
                lista.append(c+1)
            if letra==" ":
                lista.append(" ")
                letra="!="
string=""
for i in lista:
    string=string+str(i)
##DESENCRIPTAR
print(string)
string=list(input("Ingrese texto encriptado: "))
desencriptado=""
while string!=[]:
    if string[0]==' ':
        desencriptado=desencriptado+" "
        string.pop(int(0))
    elif string[1]==' ':
        desencriptado=desencriptado+" "
        string.pop(int(1))
    else:
        pos1=int(string[0])-1
        pos2=int(string[1])-1
        desencriptado=desencriptado+matriz[pos1][pos2]
        string.pop(int(0))
        string.pop(int(0))
print(desencriptado)
