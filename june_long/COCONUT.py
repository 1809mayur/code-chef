

t = int(input())

for i in range(t):
    xa,xb,XA,XB = [int(i)  for i in input().split()]

    quant1 = round(XA // xa)
    quant2 = round(XB// xb)

    if (XA/xa) > quant1:
        quant1 = quant1 + 1
    
    if (XB/xb) > quant2 :
        quant2 += 1

    print(quant1+quant2)

