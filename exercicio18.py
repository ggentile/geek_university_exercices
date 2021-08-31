while input("Deseja calcular o valor da associação paralela dos resistores? ") != "nao":
    r1 = int(input("Selecionar o valor do primeiro resistor: "))
    r2 = int(input("Selecionar o valor do segundo resistor: "))
    calcula = (r1 * r2) / (r1 + r2)
    print(f"O resultado é: {calcula}")
