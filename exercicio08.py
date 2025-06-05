# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00
distancia = int(input("digite a distancia"))

if distancia <=50:
    print("$5,00")
elif 51 <= distancia <=150:
    print("$15,00")
elif distancia > 150:
    print("$25,00")

