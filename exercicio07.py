# Uma empresa quer avaliar seus colaboradores com base em três metas atingidas.
# O programa deve calcular a média das três avaliações e exibir:

# Aprovado (>=7)
# Em treinamento (>=5 e <7)
# Reprovado (<5)
media1 = float(input("digite a primeira media: "))
media2 = float(input("digite a segunda media: "))
media3 = float(input("digite a terceira media: "))

media = media1 or media2 or media3 

print(f"media: {media:.2}")

if media >= 7:
    print("aprovado")
elif media >= 5:
    print("em treinamento")
else:
    print("reprovado")


