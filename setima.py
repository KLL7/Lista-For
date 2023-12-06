lista=[]
quantidade=1
num= 1
número=float(input(f"Coloque {num} número: "))
lista.append(número)
while quantidade < 5:
    num+=1
    número=float(input(f"Coloque o {num} número: "))
    lista.append(número)
    quantidade+=+1

else:
    print(f'O maior número é: {max(lista)}')