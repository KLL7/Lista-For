nome=input("Coloque seu nome (mínimo de três letras): ")
while len(nome)<3:
    print("Nome com menos 3 letras!")
    nome=input("Coloque seu nome (mínimo de três letras) novamente: ")

idade=int(input("Coloque sua idade (Entre 0 e 150): "))
while idade<0 or idade>150:
    print("Idade está errada!")
    idade=int(input("Coloque a idade novamente: "))

sal=float(input("Coloque o seu salário: "))
while sal<=0:
    print("Salário negativo ou zero!")
    sal=float(input("Coloque o salário novamente: "))

sexo=input("Selecione seu sexo 'f' (feminino) ou 'm' (masculino): ")
while sexo not in ['f', 'm']:
    print("Sexo não correspodente!: ")
    sexo=input("Selecione seu sexo novamente: ")

estcivil=input("Coloque seu estado civil atual 's' Solteiro, 'c' Casado , 'v' Viuvo e 'd' Divorciado: ")
while estcivil not in ['s', 'c', 'v', 'd']:
    print("Estado civil não reconhecido: ")
    estcivil=input("Coloque seu estado civil atual 's' Solteiro, 'c' Casado , 'v' Viuvo e 'd' Divorciado (NOVAMENTE): ")

print(f"Seu nome: {nome}, sua idade: {idade}, seu salário: {sal}, seu sexo: {sexo} e seu estado civil: {estcivil}.")
