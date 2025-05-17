funcionarios=[]

for i in range(1):
    nome=input("nome do funcionario:")
    horas=float(input("digite as horas:"))
    dias=float(input("digite os dias:"))
    valorphora=float(input("digite o valor:"))

    pagamento=(horas*valorphora)*dias

    funcionarios.append({
        "nome":nome,
        "horas":horas,
        "dias" :dias,
        "valorphora":valorphora,
        "pagamento":pagamento
    })
print("---valor a ser pago---")
for funcionario in funcionarios:
    print(f"{funcionario['nome']} - horas{funcionario['horas']} | dias:{funcionario['dias']} |valorphora{funcionario['valorphora']}| pagamento:{funcionario['pagamento']:.2f}")
          