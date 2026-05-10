matriz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def coordenada(vetor, linha, coluna, largura):
    valor = vetor[linha * largura + coluna]
    return valor


def contraste(vetor):
    for i in range(len(vetor)):
        novo_valor = vetor[i] * 1.2
        if novo_valor > 255:
            vetor[i] = 255
    return vetor


def inversao(vetor):
    esquerda = 0
    direita = len(vetor) - 1

    while esquerda < direita:
        aux = vetor[esquerda]
        vetor[esquerda] = vetor[direita]
        vetor[direita] = aux

        esquerda += 1
        direita -= 1

    return vetor


print(inversao(matriz))
