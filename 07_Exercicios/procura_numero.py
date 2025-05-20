def encontra_numero (lista: list, numero: int) -> bool:
   for linha in lista:
       for elemento in linha:
           if elemento == numero:
              return True
    return False 
  
lista = [ [7, 12, 21], [4, 90, 63], [25, 33, 41] ]
