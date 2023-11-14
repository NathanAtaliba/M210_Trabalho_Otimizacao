import numpy as np

def simplex_solver(c, A, b):
    # Adicionar variáveis de folga ao sistema de equações
    A = np.hstack((A, np.eye(len(b))))
    c = np.concatenate((c, np.zeros(len(b))))

    # Inicializar a tabela Simplex
    tableau = np.vstack((np.concatenate(([0], -c)), np.column_stack((b, A))))
    
    while any(tableau[0, 1:] < 0):
        # Escolher a coluna de entrada (índice da variável que entra na base)
        entering_col = np.where(tableau[0, 1:] < 0)[0][0] + 1
        
        # Calcular as razões entre os termos independentes e os elementos positivos da coluna de entrada
        ratios = tableau[1:, 0] / tableau[1:, entering_col]
        
        # Escolher a linha de saída (índice do termo independente que sai da base)
        leaving_row = np.argmin(ratios) + 1
        
        # Atualizar a tabela Simplex
        pivot_element = tableau[leaving_row, entering_col]
        tableau[leaving_row, 1:] /= pivot_element
        for i in range(len(tableau)):
            if i != leaving_row:
                tableau[i, 1:] -= tableau[i, entering_col] * tableau[leaving_row, 1:]
        tableau[0, :] -= tableau[0, entering_col] * tableau[leaving_row, :]
    
    # Extrair resultados
    optimal_solution = tableau[0, 0]
    shadow_prices = -tableau[0, 1:]
    
    return optimal_solution, shadow_prices

# Exemplo de uso
c = np.array([3, 2])  # Coeficientes da função objetivo -> 3A + 2B
A = np.array([[1, 2], [2, 1]])  # Coeficientes das restrições -> (1A + 2B) e (2A + 1B)  
b = np.array([4, 5])  # Termos independentes das restrições -> 4 e 5

#PPL:
# MAXIMIZE: 3A + 2B
# 1A + 2B < 4
# 2A + 1B < 5

optimal_solution, shadow_prices = simplex_solver(c, A, b)

print("Ponto ótimo:", optimal_solution)
print("Lucro ótimo:", -optimal_solution)  # Como é um problema de maximização, multiplicamos por -1
print("Preço-sombra de cada restrição:", shadow_prices)