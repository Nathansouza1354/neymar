alunos=[]

for i in range(5):
    nome=input("nome do aluno:")
    av1=float(input("digite a nota:"))
    av2=float(input("digite a nota:"))

    media=(av1+av2)/2

    alunos.append({
        "nome":nome,
        "av1":av1,
        "av2":av2,
        "media":media
    })
print("---resultado final---")

for aluno in alunos:
    print(f"{aluno['nome']} - av1:{aluno['av1']} | av2:{aluno['av2']} | media:{aluno['media']:.2f}") 

