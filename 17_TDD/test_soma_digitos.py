
def soma_str(s: str) -> int:
    return sum(int(char) for char in s if char.isdigit())

def test():
    assert soma_str("") == 0
    assert soma_str("a") == 0
    assert soma_str("4") == 4
    assert soma_str("5ab6") == 11  # 5+6
    assert soma_str("3 -4 z5") == 12  # 3+4+5, ignore o sinal
    assert soma_str("11a2z3") == 7  # 1+1+2+3
