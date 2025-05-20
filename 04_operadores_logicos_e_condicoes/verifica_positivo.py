def eh_positivo(numero):
    return numero > 0 

def eh_negativo(numero):
    return numero < 0 

def test():
    # Testes para a função eh_positivo
    assert eh_positivo(1)
    assert eh_positivo(2)
    assert eh_positivo(10)
    assert not eh_positivo(0)
    assert not eh_positivo(-1)
    assert not eh_positivo(-10)

    # Testes para a função eh_negativo
    assert eh_negativo(-1)
    assert eh_negativo(-2)
    assert eh_negativo(-10)
    assert not eh_negativo(0)
    assert not eh_negativo(1)
    assert not eh_negativo(10)

test()
