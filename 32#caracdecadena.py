x=input("ingrese texto ")
cont=0
for i in x:
    if i!="":
        cont=cont+1
x=x.split()
x.extend(".")
x="".join(x)
print(x)
print(cont)
