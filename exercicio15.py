notas = []

while input("Deseja inserir notas para cálculo da sua média? ") == "sim":
    recebe_nota = int(input(f"Qual o valor da {len(notas) + 1}ª nota? "))
    notas.append(recebe_nota)
if notas == 0:
    print("Você não inseriu nenhuma nota para cáculo")
else:
    media = sum(notas) / len(notas)
    print(f"A sua média final baseado nas notas inseridas será: {media}")
