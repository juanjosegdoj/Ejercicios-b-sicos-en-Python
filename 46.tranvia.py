def tranvia(n,cap):
    tranvia=0
    for i in range(n):
        print("parada: ",i+1)
        ai=int(input("Numero de pasajeros que suben: "))
        bi=int(input("Numero de pasajeros que bajan: "))
        tranvia=tranvia+ai-bi
        print("num personas en tranvia: ",tranvia)
        if i==n-1:
            tranvia=0
        if tranvia>cap:
            return False
    return True
n=int(input("Ingrese numero de paradas del tranvia: ")) 
cap=int(input("Ingrese capacidad del tranvia: "))
print(tranvia(n,cap))


        
    
    
