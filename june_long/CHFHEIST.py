

def get_hijack_money(D,d,p,q):
    i = 0
    count = 1
    while i < D:

        if i < d:
            money = p * d 
            i += d 
        else:
            if (i+d) < D:
                money += (p + count * q) * d  
                count += 1
                i += d
            else:
                money += (p + count * q) * (i+d-D)
                break
    return money

def main():
    t = int(input())
    for i in range(t):
        D,d,p,q = [int(i) for i in input().split()]
        res = get_hijack_money(D,d,p,q)
        print(res)

main()


