num=int(input("Coloque seu número: "))
ver=2
teste=1

while ver <= num:
    teste= teste*ver
    ver+=1
print(f"O seu numero {num}! é: ", teste)