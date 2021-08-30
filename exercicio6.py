import math

nota1 = float(input("digite uma nota: "))
nota2 = float(input("digite a outra nota: "))

if nota1 >=0 and nota1 <= 10 and nota2 >=0 and nota2 <=10:
    print(f"A média das notas é {(nota1 + nota2)/ 2}")
else:
    print("Insira uma nota válida entre 0 - 10")