def fibonacci(n):
     if n<2:
         return n
     else:
          return (fibonacci(n-1) + fibonacci(n-2))
n=int(input("puesto en la sucesion de fibonacci "))
print(fibonacci(n))
