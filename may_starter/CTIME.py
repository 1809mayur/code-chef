


t = int(input())
    
for i in range(t):
    n,k,f = list(map(int,input().strip().split()))
    Sum = 0
    arr = []
    for each in range(n):
        s,e = list(map(int,input().strip().split()))
        arr.append([s,e])

    for i in range(len(arr)-1):
        val1 = arr[i][1]
        val2 = arr[i+1][0]

        diff = val1 - val2

        if diff:
            Sum += diff
            
        if arr[i+1][1] > f:
            Sum += arr[i+1][1] - f 
        
    if Sum >= k:
        print("YES")   
    else:
        print("NO")



        

    
