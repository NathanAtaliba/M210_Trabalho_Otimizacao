# M210_Trabalho_Otimizacao
Repositorio criado para trabalho de otimização

# INTEGRANTES:
Nathan Santos Ataliba, 1663 , GEC

Gabriel Guerzoni , 235 , GES

Marcos Guerra Soares, 332 , GES
# LOGICA:

   O método Simplex é um algoritmo utilizado para resolver problemas de programação linear, que são problemas de otimização nos quais se busca maximizar ou minimizar uma função linear sujeita a um conjunto de restrições lineares. Aqui estão os passos básicos para utilizar o método Simplex:


## Formule o Problema:

    Defina a função objetivo que você deseja maximizar ou minimizar.
    Estabeleça as restrições do problema na forma de equações lineares.

## Forma Padrão:
    Certifique-se de que o problema está na forma padrão, o que significa que a função objetivo é de maximização, todas as variáveis são não negativas e as restrições são todas do tipo ≤.

## Crie a Tabela Simplex Inicial:

    Escreva as equações das restrições e a função objetivo em uma tabela. Adicione variáveis de folga, se necessário.

## Escolha a Variável de Entrada:

    Identifique a variável de decisão que entrará na base. Essa escolha geralmente é feita com base no coeficiente mais negativo na função objetivo.

## Escolha a Variável de Saída:

    Determine qual variável de folga ou de excesso deixará a base. Isso é feito considerando as restrições e garantindo que a solução continue sendo factível.

# Atualize a Tabela Simplex:

    Utilize operações elementares para atualizar a tabela. As operações mais comuns são pivotamento e escalonamento.

# Verifique o Critério de Parada:

    Verifique se a solução atual é ótima ou se deve continuar o processo. O critério de parada geralmente envolve todos os coeficientes da função objetivo sendo não negativos.

## Iteração:

    Se a solução não for ótima, repita os passos 4 a 7 até atingir a solução ótima.

## Interpretação da Solução:

    Após alcançar a solução ótima, interprete os resultados em termos do problema original.

# TESTES:

## MAXIMIZE:
    Z = 5x1 + 7x2

## RESTRIÇÕES:
    primeira -> 3x1 <= 250
    segunda -> 1.5x2 <= 100
    terceira -> 0.25x1 + 0.5x2 <= 50

## SOLUÇÃO RETORNADA:
    Solução Ótima: [83.33333333 58.33333333]
    Lucro Ótimo: 825.0
    Preços Sombra: [ 0.5  0.  14. ]
