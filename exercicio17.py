#Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula: F = C × 1.8 + 32

temperatura_celsius = float(input("digite a temperatura em C: "))

temperatura_fahrenheit = temperatura_celsius * 1,8 + 32 
print(f"{temperatura_celsius}ºC é igual a {temperatura_fahrenheit}ºF")