saldo_disponivel = 1000  
while True:
    valor = int(input("Informe o valor a ser sacado (em reais): "))
    if valor > saldo_disponivel:
        print("Saldo insuficiente. Não é possível sacar esse valor.")
    
    else:
        notas = [100, 50, 20, 10, 5, 2]
        resultado = {}
        

        for nota in notas:
            qtd = valor // nota
            if qtd > 0:
                resultado[nota] = qtd
                valor %= nota
        
        print("\nNotas fornecidas:")
        for nota, qtd in resultado.items():
            print(f"{qtd} nota(s) de R$ {nota}")
           
