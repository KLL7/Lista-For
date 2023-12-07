temps=[]
while True:
    temp=float(input("Coloque suas temperaturas (Celsius) e digite zero para parar o programa: "))
    temps.append(temp)

    if temp==0:
        temps.pop()
        print("PROGRAMA PARADO!")
        maior= max(temps)
        menor= min(temps)
        media=int(sum(temps)/len(temps))
        print(f"A maior temperatura registrada foi {maior}°C, a menor temperatura foi {menor}°C, e a média de suas temperaturas foi {media}°C.")