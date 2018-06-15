n=int(input("ingrese numero: "))
spac=len(str(n*n))+1
for i in range(1,n+1):
    for j in range(1,n+1):
        spa=(spac-len(str(i*j)))*" "
        print(i*j,end=(spa))
    print()
    
###############################################################

n=int(input("ingrese numero: "))
spac=len(str(n*n))+3
for i in range(1,n+1):
    for j in range(1,n+1):
        print(str(i*j).center(spac," "),end=(""))
    print()

