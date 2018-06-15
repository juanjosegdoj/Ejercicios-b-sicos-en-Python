def factorial(tamaño):
    fact=1
    for i in range(1,tamaño+1):
        fact=fact*i
    return fact
tamaño=int(input("::::::"))
cantidad=factorial(tamaño)/(factorial(tamaño-2)*factorial(2))
print(cantidad)
