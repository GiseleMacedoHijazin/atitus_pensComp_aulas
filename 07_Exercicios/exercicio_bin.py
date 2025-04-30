def dec_to_bin(n)
    if n == 0 
        return '0'
    binario = ''
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    return binario


def bin_to_dec(n):
    decimal = ''
    potencia = len(n) - 1
    for char in n:
        decimal = decimal + int(char) * (2 ** potencia)
        potencia =-1
    return decimal
    

assert dec_to_bin(0) == '0'
assert dec_to_bin(1) == '1'
assert dec_to_bin(2) == '10'
assert dec_to_bin(3) == '11'
assert dec_to_bin(4) == '100'
assert dec_to_bin(10) == '1010'

assert bin_to_dec('0') == 0
assert bin_to_dec('1') == 1
assert bin_to_dec('10') == 2
assert bin_to_dec('11') == 3
assert bin_to_dec('100') == 4
assert bin_to_dec('1010') == 10
