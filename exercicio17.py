numero_inteiro = int(input("Por favor, inserior numero inteiro para valor do numero harmônico: "))
valor = []
harmonico = 1
denominador = 0

for i in range(numero_inteiro):
    denominador += 1
    h = (harmonico / denominador)
    valor.append(h)
    b = sum(valor)
print(b)
