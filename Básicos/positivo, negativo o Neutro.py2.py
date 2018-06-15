contP=0
contNeg=0
ContN=0
print("USTED VA INGRESAR 4 NUMEROS")
for i in range(1,5):
    n=int(input("ingrese numero "))
    if n>0:
        contP=contP+1
    elif n<0:
        contNeg=contNeg+1
    else:
        ContN=ContN+1
print("usted ingresó: ",contP," positivos,",contNeg," negativos,",ContN," neutros")

        
