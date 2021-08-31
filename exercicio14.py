jogar = input("Deseja continuar adivinhando?")
while jogar != "nao":
    adivinha = int(input("Insira um numero de 100 a 999: "))
    if adivinha < 100 or adivinha > 999:
        print("Por favor insira um numero entre 100 a 999")
    else:
        for n in str(adivinha):
            print(n)
