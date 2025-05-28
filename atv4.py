pessoas = []

while True:
    nome = input("Informe o nome da pessoa: ")
    idade = int(input("Informe a idade da pessoa: "))
    pessoas.append((nome, idade))

    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar != 'S':
        break

total = len(pessoas)
media_idade = sum(p[1] for p in pessoas) / total
mais_velha = max(pessoas, key=lambda p: p[1])

print(f"\nQuantidade de pessoas cadastradas: {total}")
print(f"Média de idade: {media_idade:.2f}")
print(f"A pessoa mais velha é {mais_velha[0]}, com {mais_velha[1]} anos.")