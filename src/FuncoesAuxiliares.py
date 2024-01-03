def find_combinations(nums, target, current_combination, result_set, bag_size_final):
    if target == 0 or (not nums and target>0 and target<bag_size_final):
        result_set.append(current_combination[:])
        return
    if target < 0 or not nums:
        return

    # Include the current number
    current_combination.append(nums[0])
    find_combinations(nums[1:], target - nums[0][1], current_combination, result_set, bag_size_final)
    current_combination.pop()

    # Exclude the current number
    find_combinations(nums[1:], target, current_combination, result_set, bag_size_final)

def removeExcesso(lista, tamanho, combinacoes):
    elementosExcesso = []
    for combinacao in combinacoes:
        somaElementos = 0
        for elemento in combinacao:
            somaElementos += elemento[1]
        for e in lista:
            if e not in combinacao and e[1] + somaElementos <= tamanho:
                elementosExcesso.append(combinacao)
                break

    for remover in elementosExcesso:
        combinacoes.remove(remover)

def generate_combinations(nums, bag_size):
    
    # Verifica se o veículo aguenta todas as entregas de uma vez
    somaTotal = 0
    for e in nums:
        somaTotal += e[1]
    if somaTotal < bag_size:
        return [nums[:]]

    result_set = []
    find_combinations(nums, bag_size, [], result_set, bag_size)
    return result_set
