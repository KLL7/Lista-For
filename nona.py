lista=[]
pares=0
impares=0
quantidade=1
number= 1
número=int(input(f"Coloque {number} número: "))
lista.append(número)
while quantidade < 10:
    number+=1
    número=int(input(f"Coloque o {number} número: "))
    lista.append(número)
    quantidade+=1
lista.pop(0)
for i in range(número):
    teste= i%2
    if teste==0:
        pares+=1
    else:
        impares+=1
print(f"Entre seus números {pares} são pares e {impares} são impares.")


