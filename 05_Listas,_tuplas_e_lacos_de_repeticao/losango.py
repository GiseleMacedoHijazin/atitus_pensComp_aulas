def desenha_losango(altura):
    if altura % 2 == 0:
        altura += 1

    meio = altura // 2
    linhas = []

    for linha in range(altura):
        if linha <= meio:
            espacos = meio - linha
            estrelas = linha * 2 + 1
        else:
            espacos = linha - meio
            estrelas = altura - (linha - meio) * 2

        linhas.append(' ' * espacos + '#' * estrelas)

    return linhas
