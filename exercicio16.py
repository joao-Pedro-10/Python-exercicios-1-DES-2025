#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%

salario = float(input("Digite o seu salário: "))
if salario <= 2000:
    print("você recebera 15%")
elif salario <= 5000:
    print("voce recebera 10%")
elif salario >= 5000:
    print("voce recebera 5%")