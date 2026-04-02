nome = input("Nome do aluno: ")
turma = input("Turma: ")
materia = input("Matéria: ")

notas = []
continuar = "s"

while continuar.lower() == "s":
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    continuar = input("Deseja inserir outra nota? (s/n): ")

soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade

if media >= 5:
    status = "Parabens você fez o minímo"
if media >= 6:
    status = "Vai ter que fazer exame:()"    
else:
    status = "não fez nem o mínimo..."

print("\n--- Relatório: {materia} ---")
print(f"Aluno: {nome} | Turma: {turma}")
print(f"Média Final: {media:.2f}")
print(f"Status: {status}")