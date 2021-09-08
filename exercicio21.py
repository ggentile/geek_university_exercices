x = []
y = []
produto_escalar = []

for n in range(5):
    input_x = int(input("Insira o primeiro valor: "))
    input_y = int(input("Insira o segundo  valor: "))
    x.append(input_x)
    y.append(input_y)
print(x)
print(y)

for x, y in zip(x, y):
    produto_escalar.append(x*y)

print(f"O valor do produto escalar desses números é {sum(produto_escalar)}")
