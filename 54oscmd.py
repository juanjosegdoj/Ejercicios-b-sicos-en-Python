import os

def link_informacion():      #si desea saber más acerca de los siguientes operadores;
    os.system("start http://pythonya.appspot.com/detalleconcepto?deta=Creaci%C3%B3n,%20carga%20y%20lectura%20de%20archivos%20de%20texto")

def enlace_python():
    os.system("start http://pythonya.appspot.com/" )
    
def creaciontxt():  ## esta funcion crea un archivo .exe/.bat vacio (NO guarda datos)-- queda almacenado en el lugar donde se encuentra este archivo                                                                                  # ESTA FUNCION CREA ARCHIVOS .TXT/.py/.bat
    print("NOTA: el nombre de archivo se debe escribir con la extension")
    archivo=input("INGRESE NOMBRE DEL ARCHIVO: ")
    archi=open(archivo,'w')
    archi.close()

def creartxt():
    archi=open('datosjamon.txt','w')
    archi.close()

def grabartxt():
    print("nota: escriba el nombre co la extension")
    string=input("ingrese el archivo a buscar o ingrese un nuevo nombre de archivo: ")
    archi=open(string,'a')      # la opcion open abre el archivo señala, y si no exite lo crea
    while string!="":                          ##desde aqui empiezo a llenarlo:
        string=input("ingrese datos: ")
        archi.write((string+"\n"))
    archi.close()

def leertxtenlista():
    try:
        archi=open('datos.txt','r')
        lineas=archi.readlines()
        for li in lineas:
            print (li)
        archi.close()
    except:
        print("Estuve buscando informacion que pudiera hacerla la lectura de archivo ")
        print("Sin embargo, no me fue posible por la informacion obsoleta")
        print("si aun asi insiste, dirijase a la OPCION 5")



##menu principal
print("                      OPCIONES DE SISTEMA ")
print("")
print("1. Creacion DE ARCHIVOS con nombre opcional")
print("2. Creacion de archivos")
print("3. grabar informacionen ARCHIVOS directamente")
print("4. Leer archivos en lista")
print("5. mas informacion")
print("6. Todo lo que necesitas para ser un experto en python")
print("")
opcion=int(input("Ingrese su opcion: "))
if opcion==1:
    creaciontxt()
elif opcion==2:
    creartxt()
elif opcion==3:
    grabartxt()
elif opcion==4:
    leertxtenlista()
elif opcion==5:
    link_informacion()
elif opcion==6:
    enlace_python()
else:
    print("No existe ninguna opcion con el valor asigando")
    

    



