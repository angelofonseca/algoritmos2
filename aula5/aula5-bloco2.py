def acesso_direto(vetor, hora):
    return vetor[hora]


def existeTemperatura(vetor, valorBuscado):
    for i in range(len(vetor)):
        if valorBuscado == vetor[i]:
            return i
    return -1


def maior_e_menor(vetor):
    menor_valor = vetor[0]
    maior_valor = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] < menor_valor:
            menor_valor = vetor[i]
        if vetor[i] > maior_valor:
            maior_valor = vetor[i]
    return maior_valor, menor_valor


print(maior_e_menor(vetor))
