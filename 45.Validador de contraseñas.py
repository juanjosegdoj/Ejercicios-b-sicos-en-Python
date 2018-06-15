def validar(password):
    if len(password)<5:
        return False
    minuscula=0
    mayuscula=0
    digito=0
    for c in password:
        if c>="a" and c<="z":
            minuscula+=1
        elif c>="A" and c<="Z":
            mayuscula+=1
        elif c>="0" and c<="9":
            digito+=1
    if minuscula ==0 or mayuscula==0 or digito==0:
        return False
    return True
