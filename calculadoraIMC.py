def calcular_imc(peso, altura):
    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)
    return imc


def avaliar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25:
        return "Peso adequado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau 1"
    elif 35 <= imc < 40:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Extrema"


while True:
    print("\n** Allysson | Calculadora de IMC  **\n")

    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            if peso <= 0:
                print("Peso não pode ser negativo ou zerado. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido para o peso.")

    while True:
        altura_str = input("Digite sua altura em metros: ").replace(",", ".").replace(".",(""))
        try:
            altura = float(altura_str)
            if altura <= 0:
                print("Altura não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido para a altura.")

    imc = calcular_imc(peso, altura)
    classificacao = avaliar_imc(imc)

    print("***********************************\n")
    print(f"Seu IMC é: {imc:.2f}")
    print("")
    print(f"Classificação: {classificacao}")
    print("\n***********************************")



    escolha = input("Deseja calcular novamente? (s/n): ").lower()
    while escolha not in ("s", "n"):
        escolha = input("Por favor, digite 's' para sim ou 'n' para não: ").lower()
    if escolha == "n":
        print("\n***********************************")
        print("\nObrigado por usar a Allysson | Calculadora de IMC.\n\n Tenha um bom dia!")
        break
