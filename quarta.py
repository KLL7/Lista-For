cidade1=80000
cidade2=200000
anos=0
aumento1=cidade1*0.3



while cidade1 < cidade2:
    cidade1+=cidade1*0.3
    cidade2+=cidade2*0.15
    anos+=anos+1

else:
    print(f"Vai demorar {anos} anos e a cidade vai ter {cidade1} habitantes.")