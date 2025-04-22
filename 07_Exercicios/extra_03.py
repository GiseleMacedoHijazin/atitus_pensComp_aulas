def real_para_dolar(valor):
    tx_conversao = 5.20 
    conversao = valor / tx_conversao
    print(f"O valor informado será convertido usando a taxa de {tx_conversao}: {valor} / {tx_conversao} = {conversao}")
    return conversao

valor = float(input("Informe um valor para converter: "))
real_para_dolar(valor)

def test():
    assert real_para_dolar(500, 5.20) == 96.23
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33333333333333
