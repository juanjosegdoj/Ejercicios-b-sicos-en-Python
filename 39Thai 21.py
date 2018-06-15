rocas_en_pila=int(input("ingrese numero de rocas en pila"))
Nro_de_jugadores=int(input("ingrese numero de jugadores"))
cont=1
while rocas_en_pila!=0:
    while True:
        if cont>Nro_de_jugadores:
            cont=1
        print("Turno jugador",cont)
        rocas=int(input("Rocas a extraer "))
        if rocas>0 and rocas<4:
            if rocas<=rocas_en_pila:
                rocas_en_pila = rocas_en_pila-rocas
                cont=cont+1
                print("Rocas que quedan en pila ",rocas_en_pila)
                break
            print("No hay todo ese numero de rocas en la pila")
        print("sólo puedes cojer entre 1 y 3 rocas")
print("El jugador ",cont-1," ha ganado")
