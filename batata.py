def main():
    nome=""
    idade=0
    opçao=0
    while True:
        print("**MENU PRINCIPAL**")
        print("1.Cadastra usuario")
        print("2.ver dados cadastrados")
        print("3.sair do sistema")
        print("****************")
        opçao=int(input("escolha uma opção:"))
        if opçao==1:
            nome=input("seu nome:")
            idade=int(input("sua idade:"))
            print("dados cadastrados com sucesso!")
        elif opçao==2:
            if nome=="" or idade==0:
                print("nenhum dado cadastrados")
            else:
                print("dados cadastradis com sucesso!")
                print(f"nome:{nome}")
                print(f"idade{idade}")
        elif opçao==3:
            print("encerrando o sistemas...")
            break
        else:
            print("opçao invalida")


if __name__=="__main__":
    main()