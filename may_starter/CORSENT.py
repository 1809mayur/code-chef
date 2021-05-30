from collections import  Counter

t = int(input())

a_mini = ord('a')
a_maxi = ord('m')
b_mini = ord('N')
b_maxi = ord('Z')

for i in range(t):
    s = str(input())

    checker = Counter(s)

    for i in checker:
        if checker[i] > 1:
            print("NO")
            break

    if s.isupper():
        print("NO")
        break

    if s.islower():
        print("NO")
        break 

    for i in s:
        if ord(i) not in range(a_mini,a_maxi+1):
            print("NO")
        
        if ord(i) not in range(b_mini,b_maxi+1):
            print("NO")


