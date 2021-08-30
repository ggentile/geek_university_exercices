import math

a = int(input("Selecione o coeficiente de a: "))
b = int(input("Selecione o coeficiente de b: "))
c = int(input("Selecione o coeficiente de c: "))

delta = (b ** 2) - (4 * a * c)

if a == 0:
    print("O Valor de a deve ser diferente de 0")
elif delta < 0:

    print("Sem raízes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'As duas raízes são {x1} e {x2}')
