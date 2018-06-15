vector=[11, 14, 15, 20, 13, 11, 4, 7, 1, 16]
print(vector)
elemBor=int(input("Ingrese número a borrar:  "))
if elemBor in vector:
      vector.remove(elemBor)
      print("Sin elemento:  ",vector)
