# first get all the possible tuples with length of n.
# then check for the AND operator over tuples if AND operator over each element of tuple is zero then increament our counting.

from itertools import product
from functools import reduce
from operator import iand

t = int(input())  # test cases.

for i in range(t):
    n,m = [int(i) for i in input().split()]   # taking an n and m as an input.
    p = 2 ** m

    # with the use of product we get all possible tuples with length n.
    tuple_ls = reduce(iand,list(product(range(0,p),repeat=n)))
    print(tuple_ls)

# finding whether AND over each element of tuple is zero or not.
# count = 0
# for i in tuple_ls:
#     ans = reduce(iand,i) 
#     if ans == 0:
#         count += 1
# print(count)



    
