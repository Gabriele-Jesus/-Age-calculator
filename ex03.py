nome = input("Digite seu nome completo: ")
ano_nascimento = input("Digite seu ano de nascimento: ")

while True:
    try:
        ano_nascimento = int(ano_nascimento)
        
        if 1922 <= ano_nascimento <= 2024:
            idade  = 2024 - ano_nascimento
            print(str(nome) + " você completou", idade,"anos de idade em 2024!")
            break
        else:
            print("O ano de nascimento não é válido, digite novamente!")
    except ValueError:
        print("Esse campo só aceita números, digite novamente")

    