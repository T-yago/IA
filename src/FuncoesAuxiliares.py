
"""
Função responsável por gerar todas as combinações de forma recursiva, sem nunca ultrapassar o peso máximo estabelecido
para o veículo.
"""
def find_combinations(idsEntregas, capacidade, combinacao_Atual, set_Resultado, capacidade_final):
    if capacidade == 0 or (not idsEntregas and capacidade>0 and capacidade<capacidade_final):
        set_Resultado.append(combinacao_Atual[:])
        return
    if capacidade < 0 or not idsEntregas:
        return

    # Include the current number
    combinacao_Atual.append(idsEntregas[0])
    find_combinations(idsEntregas[1:], capacidade - idsEntregas[0][1], combinacao_Atual, set_Resultado, capacidade_final)
    combinacao_Atual.pop()

    # Exclude the current number
    find_combinations(idsEntregas[1:], capacidade, combinacao_Atual, set_Resultado, capacidade_final)


"""
Remove todas as combinações em que poderia ser adicionado mais uma entrega ao conjunto sem exceder a capacidade máxima
"""
def removeExcesso(idsEntregas, capacidade, combinacoes):
    elementosExcesso = []
    for combinacao in combinacoes:
        somaElementos = 0
        for elemento in combinacao:
            somaElementos += elemento[1]
        for e in idsEntregas:
            if e not in combinacao and e[1] + somaElementos <= capacidade:
                elementosExcesso.append(combinacao)
                break

    for remover in elementosExcesso:
        combinacoes.remove(remover)


"""
Função que recebe como argumentos uma lista de listas de dois elementos em que o primeiro elemento é o id da entrega e o
segundo o peso associado à entrega, e um float que representa a capacidade máxima do veículo.

Esta retorna todas as combinações possíveis de entregas que são possíveis de levar na mesma viagem, sem ultrapassar nunca
a carga máxima do veículo.

Exemplo:

idsEntregas -> [[1, 4], [2, 5], [3, 3], [4, 2]]
capacidade -> 5

Resultado -> [[[1, 4]], [[2, 5]], [[3, 3], [4, 2]], [[3, 3]], [[4, 2]]]
"""
def generate_combinations(idsEntregas, capacidade):
    set_Resultado = []
    find_combinations(idsEntregas, capacidade, [], set_Resultado, capacidade)
    # removeExcesso(idsEntregas, capacidade, set_Resultado)
    return set_Resultado
