def calcular_idade():
    while True:
        nome = input("Digite seu nome completo: ")
        try:
            ano = int(input("Digite o ano de nascimento (1922 a 2025): "))
            if 1922 <= ano <= 2025:
                print(f"\n{nome}, você completou ou completará {2025 - ano} anos em 2025.")
                break
            else:
                print("Ano inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

calcular_idade()
