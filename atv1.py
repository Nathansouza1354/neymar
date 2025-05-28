def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primos = []
for num in range(1, 101):
    if eh_primo(num):
        primos.append(num)

print("Números primos entre 1 e 100:")
print(primos)
print(f"Total de primos encontrados: {len(primos)}")
