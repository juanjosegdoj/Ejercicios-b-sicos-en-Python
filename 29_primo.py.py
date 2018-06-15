import math
def es_primo(n):
    if n <= 1:
        return False
    elif n == 2.0:
        return True
    elif n % 2 == 0:
        return False
    for i in range (3, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
print(es_primo(11))
