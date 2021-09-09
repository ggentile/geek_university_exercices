vetor = []

for _ in range(10):
    valor = int(input("Insira um número: "))
    v = set(vetor)
    if valor not in v:
        vetor.append(valor)
    else:
        while True:
            valor = int(input("Insira um numero que não seja repetido: "))
            if valor not in v:
                vetor.append(valor)
                break
print(vetor)
print(v)
