import random

input("precione o enter para lançar o dado")

resultado = random.randint(1,6)

print(f" o dado rolou : {resultado}" );

if resultado >6:
    print("voce é muito bom")
elif resultado >=6 <=2:
    print("voce errou")

