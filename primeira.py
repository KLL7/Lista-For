nota=float(input("Coloca a nota aí: "))

while nota<0 or nota>10:
    print("inválido")
    nota=float(input("Coloca a nota aí denovo: "))
else:
    print("nota salva!")