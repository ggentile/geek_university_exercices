altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Você está abaixo do peso")

elif 18.6 <= imc <= 24.9:
    print("Você está saudável")

elif 25 <= imc <= 29.9:
    print("Você está acima do peso")

elif 30 <= imc <= 34.9:
    print("Você tem obesidade grau I")

elif 35 <= imc <= 39.9:
    print("Você tem obesidade grau II")

else:
    print("Você tem obesidade grau III")
