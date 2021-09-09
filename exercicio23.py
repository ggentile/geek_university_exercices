numeros_pares = []
numeros_impares = []

for values in range(6):
    num = int(input("Selecione 6 números: "))
    if num % 2 == 0:
        numeros_pares.append(num)
        soma_pares = numeros_pares.copy()
    else:
        numeros_impares.append(num)
        soma_impares = numeros_impares.copy()

print(f"Os numeros pares digitados foram: {numeros_pares}")
print(f"Os numeros impares digitados foram: {numeros_impares}")
print(f"A soma dos numeros pares é: {sum(soma_pares)}")
print(f"A soma dos numeros impares é: {sum(soma_impares)}")
