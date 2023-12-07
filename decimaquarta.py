idades=[]
while True:
    idade=int(input("Coloque sua idade ou digite zero para parar: "))
    idades.append(idade)
    
    if idade == 0:
        idades.pop()
        print("PROGRAMA PARADO!")
        media= sum(idades)/len(idades)
        print(f"A média das idades é {media}")
        if media >= 0 and media <= 25:
            print("Idade de pessoas jovens!")
        if media > 25 and media <= 60:
            print("Idade de pessoas adultas!")
        if media > 60:
            print("Idade de pessoas velhas!")


