string=str(input("string: "))
texto=str(input("texto: "))
cont=0
for i in range(len(texto)):
    if i==(len(texto)-1):
        break
    elif string==texto[i]+texto[i+1]:
        cont=cont+1
        print(cont)
