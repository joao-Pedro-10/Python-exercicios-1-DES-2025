#Peça a idade do usuário e diga se ele pode se cadastrar em um site:
#Permitido: 13 anos ou mais

idade = int(input("digite sua idade."))

if idade >=13:
    print("acesso permitido. ")
elif idade <13:
    print("acesso negado. ")