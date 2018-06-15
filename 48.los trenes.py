def retornos(string,i):
    for k in string:
        if k==i:
            if i!=" ":
                return "OK"
    return "Alerta"
while True:
    string=input("semaforo: ")
    tren1=input("tren1: ")
    tren2=input("tren2: ")
    if len(tren1)==len(tren2):
        break
    print("los dos trenes deben tener la misma longitud")
    
f=0
x="OK"
for i in tren1:
    if i==tren2[f] and i!=" ":
        x=retornos(string,i)
    f+=1
print(x)
    
        
        
            
