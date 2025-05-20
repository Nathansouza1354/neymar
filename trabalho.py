pessoas=[]
for i in range(3):
    while True:
        nome=input("Nome da pessoa:")
      
        if nome.isalpha():
            break
        else:
            print("invalido,digite novamente")
    while True:
        filme=input("digite nome do filme:")
        if filme.isalpha():
            break
        else:
            print("invalido,digite novamente")

    while True:
        nota=float(input("Digite sua nota:"))
        if 0<=nota<=10:
           break
        else:
            print("Numero invalido,digite novamente")

    pessoas.append({
        "nome":nome,
        "filme":filme,
        "nota":nota
    })
print("\n---dados---")
for pessoa in pessoas:
    print(f"{pessoa['nome']} - nome do filme:{pessoa['filme']} | nota:{pessoa['nota']:.2f}")