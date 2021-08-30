def my_switch(option):
    options = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    return options.get(option)

opcao = int(input("Insira um número de 1-7 e veja o dia da semana correspondente: "))
print(my_switch(opcao))
