# cheking whether the chef is lucky or not.

def is_luckychef(x,y,n,k):
    pages_left = x - y 
    
    for i in range(n):  # for each notebook.
        p,c = tuple(map(int,input().strip().split()))

        if k <= c:
            if pages_left >= p:
                return 'LuckyChef'

    return 'UnluckyChef'


def main():
    t = int(input())  # test cases

    for i in range(t):
        x,y,k,n = tuple(map(int,input().strip().split()))
        # res = is_luckychef(x,y,n,k)
        # print(res)
        lucky = False
        pages_left = x - y 
        notebook = []
        for j in range(n):  # for each notebook.
            p,c = tuple(map(int,input().strip().split()))
            notebook.append([p,c])

        for page,price in notebook:
            if k <= c and page >= pages_left:
                print('LuckyChef')
                lucky = True
                break 
        else:
            print('UnluckyChef')
        


def main():
   def main():
        t = int(input())  # test cases

    for i in range(t):
        x,y,k,n = tuple(map(int,input().strip().split()))
        # res = is_luckychef(x,y,n,k)
        # print(res)
        lucky = False
        pages_left = x - y 
        notebook = []
        for j in range(n):  # for each notebook.
            p,c = tuple(map(int,input().strip().split()))
            notebook.append([p,c])

        for page,price in notebook:
            if k <= c and page >= pages_left:
                print('LuckyChef')
                lucky = True
                break 
        else:
            print('UnluckyChef')
        
 


if __name__ == '__main__':
    main()

