def imprimir_Mat(matriz,filas):
    for i in range(filas):
        print(matriz[i])
def Crear_matriz(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([0]*columnas)
    for f in range(filas):
        for c in range (columnas):
            matriz[f][c]=float(input("{f},{c} : ".format(f=f+1,c=c+1)))
    return matriz

def Intercambiar_filas(matriz,cambio1,cambio2):
    matriz[cambio1],matriz[cambio2]=matriz[cambio2],matriz[cambio1]
    return matriz

def fila_por_escalar(matriz,escalar,fila):
    for i in range(len(matriz[fila])):
        matriz[fila][i]*=escalar
    return matriz

def Sumar_fila(matriz,cambio1,cambio2):
    for i in range(len(matriz[0])):
        matriz[cambio1][i]+=matriz[cambio2][i]
    return matriz


def Restar_fila(matriz,cambio1,cambio2):
    for i in range(len(matriz[0])):
        matriz[cambio1][i]-=matriz[cambio2][i]
    return matriz

def Sumar_fila_x_ESCALAR(matriz,cambio1,escalar,cambio2):
    for i in range(len(matriz[0])):
        matriz[cambio1][i]+=matriz[cambio2][i]*escalar
    return matriz

def Restar_fila_x_ESCALAR(matriz,cambio1,escalar,cambio2):
    for i in range(len(matriz[0])):
        matriz[cambio1][i]-=matriz[cambio2][i]*escalar
    return matriz

def Validar_operacion(matriz,operar):
    if "<->" in operar:
        if operar.count('F')!=2:
            return "Error de sintaxis"
        try:
            cambio1=int(operar[1:operar.find('<')])-1
            cambio2=int(operar[operar.find('>F')+2:])-1
            print(cambio2)
            matriz=Intercambiar_filas(matriz,cambio1,cambio2)
            return matriz
        except:
            return "Error de sintaxis"
    elif operar.count('F')==1:
        try:
            escalar=operar[:operar.find('F')]
            if escalar.count('/')==1:
                escalar=int(escalar[:escalar.find('/')])/int(escalar[escalar.find('/')+1:])
            elif  escalar==0:
                return "Error de sintaxis"
            else:
                escalar=int(escalar)
            fila=int(operar[operar.find('F')+1:])-1
            matriz=fila_por_escalar(matriz,escalar,fila)
            return matriz
        except:
            return "Error de sintaxis"
    elif operar.count('+F')==1 or operar.count('-F')==1 and operar.count('F')==2:
        cambio1=int(operar[1:operar.find('F',1)-1])-1
        cambio2=int(operar[operar.find('F',1)+1:])-1
        if '+' in operar:
            matriz=Sumar_fila(matriz,cambio1,cambio2)
        else:
            matriz=Restar_fila(matriz,cambio1,cambio2)
            
        return matriz
    elif operar.count('F')==2 and (operar.count('+')==1 or operar.count('-')==1):
        if operar.count('+')==1:
            cambio1=int(operar[1:operar.find('+')])-1
            escalar=operar[operar.find('+')+1:operar.find('F',1)]
            if escalar.count('/')==1:
                escalar=int(escalar[:escalar.find('/')])/int(escalar[escalar.find('/')+1:])
            else:
                escalar=int(escalar)
            cambio2=int(operar[operar.find('F',1)+1:])-1
            matriz=Sumar_fila_x_ESCALAR(matriz,cambio1,escalar,cambio2)
            return matriz
        elif operar.count('-')==1:
            cambio1=int(operar[1:operar.find('-')])-1
            escalar=operar[operar.find('-')+1:operar.find('F',1)]
            if escalar.count('/')==1:
                escalar=int(escalar[:escalar.find('/')])/int(escalar[escalar.find('/')+1:])
            else:
                escalar=int(escalar)
            cambio2=int(operar[operar.find('F',1)+1:])-1
            matriz=Restar_fila_x_ESCALAR(matriz,cambio1,escalar,cambio2)
            return matriz
        else:
            return "Error de sintaxis"
    else:
        return "Error de sintaxis"
            
print("   TAMAÑO MATRIZ ")
filas=int(input("filas: "))
columnas=int(input("columnas: "))
print("     ENTRADAS: ")
matriz=Crear_matriz(filas,columnas)
while True:
    operar=(input("Operacion:  ").upper()).replace(" ","") # UPPER: pasa a mayuscula ; REPLACE: quita todos los espacios
    if Validar_operacion(matriz,operar)=="Error de sintaxis":
        print("Error de sintaxis")
    else:
        imprimir_Mat(matriz,filas)

