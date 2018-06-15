def Patrullas_matriz():
    patrullas=[["disponibilidad","Nro de agentes","motorizada","armas"]]
    matriz=[]
    filas=int(input("cantidad de patrullas"))
    for i in range(filas):
        matriz.append([0]*4)
    for f in range(filas):
        print("patrulla ",f+1)
        for c in range (4):    
            if c==0:
                matriz[f][0]="disponible"
            elif c==1:
                matriz[f][c]=int(input("Cuántos agentes para controlar la situacion(numero)"))
            elif c==2:
                matriz[f][c]=input("¿Es o no motorizada?(True o False)")
            else:
                matriz[f][c]=input("Es posble enfrentarse con sospechos armados(True o False)")
    return matriz

def llamada_Emergencia():
    print("Necesitamos una patrulla urgente con las siguientes caracteristicas")
    patrullas=[["disponible","Nro de agentes","motorizada","armas"]]
    vector=[[0],[0],[0],[0]]                   
    for c in range(0,4):
        if c==0:
            vector[0]="disponible"
        elif c==1:
            vector[1]=agent=int(input("Cuántos agentes para controlar la situacion(numero)"))
        elif c==2:
            vector[2]=input("¿Es o no motorizada?(True o False)")
        else:
            vector[3]=input("Es posble enfrentarse con sosopechos armados(True o False)")
    return vector

def comparacion(patrullas):
    Emerg=llamada_Emergencia()
    for elemento in patrullas:
        for i in range(0,len(patrullas)):
            if Emerg[0]==elemento[0]and elemento[1]>=Emerg[1] and elemento[2]==Emerg[2] and Emerg[3]==elemento[3]:
                print("si hay una patrulla para socorrer")
                elemento[0]="ocupada"
                print("Así quedo la lista de patrullas ocupadas y disponibles de la policia",patrullas )
                return ("LA PATRULLA SI PUEDE ATENDER LA EMERGENCIA ")
    return ("ninguna patrulla puede solucionar el incidente")

patrullas=Patrullas_matriz()
dat=int(input("cuantos llamadas de emergencia va a realizar"))
for i in range(0,dat):
    print(comparacion(patrullas))

