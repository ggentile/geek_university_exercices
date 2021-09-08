a = []
b = []
c = []
tentativa = list(range(11))

for n in range(5):
    num1 = int(input("Insira um valor inteiro para a de 0-10: "))
    while num1 not in tentativa:
        num1 = int(input("O valor inteiro de a precisa ser de 0-10: "))
    num2 = int(input("Insira um valor inteiro para b de 0-10: "))
    while num2 not in tentativa:
        num2 = int(input("O valor inteiro de b precisa ser de 0-10: "))

    a.append(num1)
    b.append(num2)

for a, b in zip(a, b):
    c.append(a - b)

print(c)
