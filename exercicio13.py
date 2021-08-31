numeros = []
number = 0

for _ in range(10):
    n = int(input("digite um numero: "))
    numeros.append(n)
    maior = max(numeros)
    menor = min(numeros)
print(f"O maior valor é {maior} e o menor valor é {menor}")
