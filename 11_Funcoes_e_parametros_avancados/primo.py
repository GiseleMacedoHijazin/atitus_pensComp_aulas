def eh_primo(numero: int) -> bool:
    if num <= 1:
       return False
    for i in range(2, num)
        if num % i == 0 
           return False
   return True


assert not eh_primo(-1)
assert not eh_primo(0)
assert not eh_primo(1)
assert eh_primo(2)
assert eh_primo(3)
assert not eh_primo(4)
assert eh_primo(5)
