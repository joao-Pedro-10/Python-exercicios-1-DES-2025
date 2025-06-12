alunos = ["Alice, "Bruno, "Carla"]
dias = ["seg", "ter", "qua", "qui"]
reservas = [["ausente" for _ in dias] for _ in alunos]
print("preencha com 'S' para presença e 'X' para a ausência:")

for i, aluno in enumerate (alunos) :
    print(f"\nAlunos:{alunos}")
    for j, dia in enumerate(dias) :
    entrada = input(f" {dia}:")
     if entrada.uper() == 'S' :
        reservas[i] [i] = "presente"

print("\ntabela de reservas: ") 
print(f"{'aluno:<10'}{' .join ([f'{d:<10)'for d in dias])}")
for i, aluno enumerate (alunos):
    print("{aluno:<10}{''. join([f'{res:<10}'for res in reservas [i]])}")