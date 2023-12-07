neber=int(input("Quantos números que seguem a sequência de fibonacci você quer? "))
ver=0
fibo=[]
teste=0
teste1=1
while ver < neber:
    num=teste+teste1
    fibo.append(num)
    teste=teste1
    teste1=num
    ver+=1
print(fibo, end=" ")

