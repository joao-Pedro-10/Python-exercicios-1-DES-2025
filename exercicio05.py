# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

consumo = int(input("digite como foi o consumo semanal:"))
if consumo < 100:
    print("consumo dentro do limite.")
elif consumo > 100:
    print("ultrapassou o limite.")