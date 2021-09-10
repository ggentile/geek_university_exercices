from random import randint

m1 = []
m2 = []

for linha in range(4):
    linha = []
    for coluna in range(4):
        linha.append(randint(0, 200))
    m1.append(linha)

for linha in range(4):
    linha = []
    for coluna in range(4):
        linha.append(randint(0, 200))
    m2.append(linha)

print(m1)
print(m2)

m3 = [[0,0,0,0] for _ in range(4)]

for linha in range(4):
    for coluna in range(4):
        if m1[linha][coluna] > m2[linha][coluna]:
            m3[linha][coluna] = m1[linha][coluna]
        else:
            m3[linha][coluna] = m2[linha][coluna]
print(m3)
