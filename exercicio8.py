def mes_ano(opcao):
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }
    return meses.get(opcao)

escolha = int(input("Escolha um numero de 1-12 e veja o mês referente ao numero: "))

print(mes_ano(escolha))
