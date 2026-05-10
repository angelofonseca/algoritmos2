def overflow():
    vetor = [None] * 5
    for i in range(6):
        if i > len(vetor) - 1:
            return "Erro: Overflow de Memória"
        vetor[i] = 10
    return vetor


def overflow2():
    vetor = [None] * 5
    for i in range(6):
        if i > len(vetor) - 1:
            print("Erro: Overflow de Memória")
            novo_vetor = [None] * 10
            for j in range(len(vetor)):
                novo_vetor[j] = vetor[j]
            vetor = novo_vetor

        vetor[i] = 10

    return vetor


def overflow3():
    vetor = [None] * 5
    tamanho = 0

    for i in range(6):
        if tamanho > len(vetor) - 1:
            print("Erro: Overflow de Memória")
            novo_vetor = [None] * (len(vetor) * 2)
            for j in range(tamanho):
                novo_vetor[j] = vetor[j]
            vetor = novo_vetor

        vetor[tamanho] = 10
        tamanho += 1

        print(f"Itens: {tamanho} | Capacidade Real: {len(vetor)}")

    return vetor
