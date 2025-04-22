def real_para_dolar(valor, tx_conversao):
    tx_conversao = 5.20
    valor = int(input("Informe um valor para converter")
                print(f"O valor informado será convertido usando a taxa de {tx_conversao}: {valor} / {tx_conversao}")

def test():
    assert real_para_dolar(500, 5.20) == 96.23
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33333333333333
