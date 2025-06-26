#Crie um programa que receba o peso (kg) e a altura (m) de uma pessoa e calcule o IMC.  
#Classifique o resultado de acordo com a faixa:  
#Abaixo do peso (< 18.5)  Add commentMore actions
#Peso normal (18.5 a 24.9)  
#Sobrepeso (25 a 29.9)  
#Obesidade (>= 30)

peso = float(input("digite o peso: "))
altura = float(input("digite a altura: "))

kg = peso/altura
if kg  > 18.5:
    print("abaixo do peso.")
elif kg <= 18.5 >= 24.9:
    print("peso normal.")
elif kg <= 24.9 >= 30:
    print("obesidade.")
