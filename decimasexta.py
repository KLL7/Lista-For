num=int(input("Coloque o máximo de números primos: "))
while num < 2:
    num=int(input("Coloque o máximo de números primos novamente: "))
list=[]

for i in range(0, num+1):
    div=0
    for var in range(1, i+1):
        if i%var == 0:
            div+=1
    if div == 2:
        list.append(i)

print(list)
print(f"No total foram {len(list)} números primos!")
