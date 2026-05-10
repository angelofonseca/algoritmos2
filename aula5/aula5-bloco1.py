vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def inserirNoInicio(vetor, novoPaciente):
    count = 0
    for i in reversed(range(len(vetor) - 1)):
        count += 1
        vetor[i + 1] = vetor[i]
    vetor[0] = novoPaciente
    return vetor, count


def removerDaPosicao(vetor, indice):
    count = 0
    for i in range(indice, len(vetor) - 1):
        count += 1
        vetor[i] = vetor[i + 1]
    vetor[len(vetor) - 1] = None
    return vetor, count
