n=int(input("ingrese el numero de obreros "))
for i in range(1,n+1):
    print("empleado ",i)
    time=int(input("cuánto trabaja  el obrero a la semana "))
    if time<=40:
        sal=time*20
    else:
        time=time-40
        sal=(time*25)+(40*20)
    print(sal)
        
        
    
