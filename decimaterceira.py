num=int(input("Coloque seu número inteiro: "))
while not int(num) or num >16:
    print("O programa não consegue realizar operação com este número!")
    num=int(input("Coloque seu número inteiro e menor que 16: "))
ver=2
teste=1

while ver <= num:
    teste= teste*ver
    ver+=1
print(f"O seu numero {num}! é: ", teste)