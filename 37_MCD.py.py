def MCD(a,b):
    if a/b==0:
        return ("el MCD es ",b)
    else:
        r=abs(a-b)
        if b%r==0:
            return
    return("todavia no soy capaz")
print(MCD(21,7))
