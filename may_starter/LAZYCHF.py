
def lazy_chef(x,m,d):
    upper_limit = x + d 
    actual_time = x * m  
    
    if actual_time < upper_limit:
        return actual_time
    else:
        return upper_limit

print(lazy_chef(2,2,3))