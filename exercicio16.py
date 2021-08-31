numero = int(input("Insira um numero inteiro: "))
n = 0
somador = []

for n in range (1000):
    n += 1
    if numero % n == 0:
        print(f"Esse numero é divisível por: {n}")
        somador.append(n)


b = sum(somador)
print(f"A soma dos valores será: {b}")