fibo=[]
teste=0
teste1=1
num=0
while num < 500:
    num=teste+teste1
    fibo.append(num)
    teste=teste1
    teste1=num
print(fibo, end=" ")




