cidade1=float(input("Coloque o valor da cidade A: "))
cidade2=float(input("Coloque o valor da cidade B: "))
taxa1=float(input("Coloque a taxa de crescimento da cidade A: "))
taxa1+=taxa1/100


taxa2=float(input("Coloque a taxa de crescimento da cidade B: "))
while taxa2 >= taxa1:
    print("A taxa da cidade B precisa ser menor que a taxa da cidade A!")
    taxa2=float(input("Coloque a taxa de crescimento da cidade B novamente: "))

taxa2+=taxa2/100

anos=0

while cidade1 < cidade2:
    cidade1+=cidade1*taxa1
    cidade2+=cidade2*taxa2
    anos+=anos+1

else:
    print(f"Vai demorar {anos} anos e a cidade vai ter {cidade1} habitantes.")