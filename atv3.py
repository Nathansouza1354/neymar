def eh_primo(n): 
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
    
    def primos_ate_100():
        contador_primos= 0
        
        print("numero primos de 1 a 100:")
        for numero in range(1,101):
            if eh_primo(numero):
                print(numero,end=" ")
            contador_primos += 1
            
            print(f"\n\nTotal de numeros primos encontrados: {contador_primos}")

    primos_ate_100()