def eh_primo(numero: int) -> bool:
    if num <= 1:
       return False
    for i in range(2, num)
        if num % i == 0 
           return False
   return True

    
def lista_primos(val: int) -> list:
    primos = []
    for x in range (val + 1):
        if eh_primo(x):
            primos.append(x)
    return primos

assert lista_primos(10) == [2, 3, 5, 7]
assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
