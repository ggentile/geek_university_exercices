from random import randint

matrix = []

for linha in range(5):
    linha = []
    for coluna in range(5):
        linha.append(randint(1, 10))
    matrix.append(linha)

select = int(input("Selecione um valor para encontrar na matrix: "))

for linha in matrix:
    for value in linha:
        if select in linha:
            x = linha.append(value)
            y = matrix.index(linha)
            element = (value, y, x)
            print(element)
            break
        else:
            print("The element does not exist in the matrix")
