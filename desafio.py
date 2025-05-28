import datetime

participantes = []
ano_atual = datetime.datetime.now().year

for i in range(5):
    print(f"\nCadastro do participante {i + 1}:")

    
    while True:
        nome = input("Nome completo: ").strip()
        if nome:
            break
        print("O nome completo não pode ser vazio.")

   
    while True:
        palestra = input("Nome da palestra: ").strip()
        if palestra:
            break
        print("O nome da palestra não pode ser vazio.")

 
    while True:
        try:
            ano_nascimento = int(input("Ano de nascimento: "))
            if 1900 <= ano_nascimento <= ano_atual:
                break
            else:
                print(f"O ano deve estar entre 1900 e {ano_atual}.")
        except ValueError:
            print("Digite um ano válido (somente números).")

    idade = ano_atual - ano_nascimento
    participantes.append({
        "nome": nome,
        "palestra": palestra,
        "idade": idade
    })


print("\nLista de Participantes:")
for p in participantes:
    print(f"Nome: {p['nome']}")
    print(f"Palestra: {p['palestra']}")
    print(f"Idade: {p['idade']} anos\n")
