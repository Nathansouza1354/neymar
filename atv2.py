listadecompras=[]

quantidade=int(input("quantdeitensdesejado:"))

for i in range(quantidade):
    item=input(f"digite o item {i+1}:")
    listadecompras.append(item)

listadecompras.sort()

print("\nSua lista em ordem alfabetica:")
for item in listadecompras:
    print(f"-{item}")