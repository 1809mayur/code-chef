

def plagiarism(n,m,l):
    
    hashmap = dict()  #store attempts in quize.
    for i in l:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    ans = []
    for key in hashmap:
        if key <= n:
            if hashmap[key] > 1:
                ans.append(key)

    return ans

print(plagiarism(5,10,[2,5,2,5,2,4,10,10,10]))
