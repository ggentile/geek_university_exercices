v1 = []
v2 = []
produto = []
soma = []

for numeros in range(5):
    valor = int(input("Selecione 5 valores para o primeiro vetor: "))
    v1.append(valor)
for numeros in range(5):
    valor = int(input("Selecione 5 valores para o outro vetor: "))
    v2.append(valor)
for i in range(0, len(v1)):
    produto.append(v1[i] * v2[i])
for i in range(0, len(v1)):
    soma.append(v1[i] + v2[i])

set1 = set(v1)
set2 = set(v2)
diferenca = set1.difference(set2)
set_uniao = set(v1).union(v2)
lista_uniao = list(set_uniao)

set_intersecao = set(v1).intersection(v2)
lista_intersecao = list(set_intersecao)

print(v1)
print(v2)
print(f"A soma dos valores das duas listas é: {soma}")
print(f"O produto dos valores das duas listas é: {produto}")
print(f"A diferença de valores nas duas listas é: {diferenca}")
print(f"A interseção de valores nas duas listas é: {lista_intersecao}")
print(f"A uniao de valores nas duas listas é: {lista_uniao}")
