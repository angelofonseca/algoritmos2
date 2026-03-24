const lista = [
    { pergunta: 'maior de idade', resposta: true },
    { pergunta: 'conta ativa', resposta: true },
    // { pergunta: 'tem cartão de crédito', resposta: true },
    // { pergunta: 'tem cartão de debito', resposta: true },
];

const gerarCombinacoes = (condicoes) => {
    let resultado = [[]];

    for (const condicao of condicoes) {
        const novosCasos = [];

        for (const caso of resultado) {
            novosCasos.push([...caso, { ...condicao, resposta: true }]);
            novosCasos.push([...caso, { ...condicao, resposta: false }]);
        }
        resultado = novosCasos;
    }

    return resultado;
};
console.log('Número de casos:', gerarCombinacoes(lista).length);
console.log('Combinações:', gerarCombinacoes(lista));