# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.

plataforme = int(input("digite que horas voce quer acessar a plataforma: "))
if plataforma < 9:
    print("acesso negado. ")
elif plataforma > 21:
    print("acesso negado.")
else:
    print("acesso permitido. ")
