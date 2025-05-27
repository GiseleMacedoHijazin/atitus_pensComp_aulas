def calcular_juros_compostos(principal, taxa, tempo):
    return principal * (1 + taxa) ** tempo


def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    if tempo == 0:
       return principal
    return calcular_juros_compostos_recursivo(principal, taxa, tempo - 1) * (1 + taxa)

p = 1000 #principal
i = 0.05 #taxa de juros 5%
t = 5 #tempo(anos)

resultado = calcular_juros_compostos_recursivo(p, i, t)
print(resultado)

 
def test():
    
    assert calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos(1000, 0.05, 0) == 1000

    assert calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003
    assert calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.894626777442
    assert calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000
