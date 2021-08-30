def estado(option):
    estados = {
        1: "MG",
        2: "SP",
        3: "RJ",
        4: "MS", }
    return estados.get(option)


states = ["MG - 1", "SP - 2", "RJ - 3", "MS - 4"]

valor = int(input("Insira o valor do produto: "))
print(states)
opcao = int(input("Selecione o estado de envio: "))
print(estado(opcao))

if opcao == 1:
    imposto = valor * 0.07
    print(f"O valor do imposto a ser pago em Minas Gerais é: {imposto}")
elif opcao == 2:
    imposto = valor * 0.12
    print(f"O valor do imposto a ser pago em São Paulo é: {imposto}")
elif opcao == 3:
    imposto = valor * 0.15
    print(f"O valor do imposto a ser pago no Rio de Janeiro é: {imposto}")
else:
    imposto = valor * 0.08
    print(f"O valor do imposto a ser pago no Mato Grosso é: {imposto}")
