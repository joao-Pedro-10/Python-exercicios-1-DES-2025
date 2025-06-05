# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no 
# local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se 
# estiver acima do limite.

umidade = int(input("digite a umidade total."))

if umidade < 110:
    print("a temperatura esta boa.")
else:
    print("ALERTA TEMPERATURA ULTRAPASSOU O LIMITE.")