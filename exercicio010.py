# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário

salario = float(input("digite o valor do salário: "))
parcela = float(input("digite o valor da parcela do financiamento: "))

if salario <= 3000:
    print("financiamento negado, salario abaixo do minimo exigido. ")
elif parcela > salario * 0.35:
    print("Financiamento negado, parcela acima de 35% do  salário.")
else:
    print("financiamento aprovado! ")
