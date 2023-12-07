# Trabalho para disciplina M210 - Method Simplex

# Importação de bibliotecas 
import numpy as np

# Obter as dimensões do problema
num_variables = int(input("Digite o número de variáveis: "))  
num_constraints = int(input("Digite o número de restrições: ")) 

# Solicitar os coeficientes da função objetivo
funcObj = [] # MAXIMIZE

for i in range(num_variables):
    coefficient = float(input(f"Digite o coeficiente da variável x{i+1} na função objetivo: "))
    funcObj.append(-coefficient)

funcObj = np.array(funcObj)

# Solicitar os coeficientes das restrições
restric = [] # array para restrições

for i in range(num_constraints):
    row = []
    for j in range(num_variables):
        coefficient = float(input(f"Digite o coeficiente da variável x{j+1} na restrição {i+1}: "))
        row.append(coefficient)
    restric.append(row)

restric = np.array(restric)

# Solicitar os termos constantes das restrições
const = [] # array para constantes

for i in range(num_constraints):
    constant = float(input(f"Digite o termo constante na restrição {i+1}: "))
    const.append(constant)

const = np.array(const)

# MOSTRANDO AS RESTRIÇÕES
print(restric, const)

def simplex(funcObj, restricoes, constantes):

    # Quantidade de variáveis e constantes
    n_vars = len(funcObj)
    n_cons = len(constantes)

    # Adicionando as variáveis às constantes em um vetor 
    restricoes = np.hstack([restricoes, np.eye(n_cons)])
    funcObj = np.hstack([funcObj, np.zeros(n_cons)])
    
    # Cria um tableau inicial
    tableau = np.vstack([np.hstack([restricoes, constantes.reshape(-1, 1)]), np.hstack([funcObj, 0])])

    # Iteração até que o método encontre a solução ótima
    while True:
        # Checando se a solução é ótima
        if np.all(tableau[-1, :-1] >= 0):
            break

        # Encontrando a coluna pivô
        pivot_col = np.argmin(tableau[-1, :-1])

        # Encontrando a linha pivô
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        ratios[ratios < 0] = np.inf
        pivot_row = np.argmin(ratios)

        # Operação que utiliza os valores pivô
        pivot_val = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_val
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i] -= tableau[pivot_row] * tableau[i, pivot_col]

    # Extraindo a solução 
    solucao = np.zeros(n_vars)
    for i in range(n_vars):
        col = tableau[:, i]
        if (col == 0).sum() == n_cons:
            row = np.where(col[:-1] == 1)[0][0]
            solucao[i] = tableau[row, -1]

    # Preço sombra
    precoSombra = tableau[-1, n_vars:-1]

    return solucao, tableau[-1, -1], precoSombra


# Chamada da função simplex para resolver o problema de programação linear 
solucao, valorOtimo, precoSombra = simplex(funcObj, restric, const)

# Imprimindo os resultados solicitados
print(f'A solução Ótima: {solucao}')
print(f'O lucro Ótimo: {valorOtimo}')
print(f'O preços Sombra: {precoSombra}')
