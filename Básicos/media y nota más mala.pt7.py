suma=0
notmal=5
for i in range(1,12):
    n=float(input("ingrese nota de alumno"))
    if n>=0 and n<=5:
        suma=suma+n
        if n<notmal:
            notmal=n
    else:
        print("ERROR!, la nota debe estar entre 0 o 5")
print("la media del grupo es ",suma/40," y la nota mas mala es ",notmal)
