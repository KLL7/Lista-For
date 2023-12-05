nome=input("Seu nome: ")
senha=input("Sua senha: ")

while nome==senha:
    print("Sua senha é igual ao seu nome!")
    senha=input("Digite sua senha novamente: ")
else:
    print(f"Bem vindo {nome}!")
