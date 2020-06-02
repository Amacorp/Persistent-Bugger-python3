import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
    
    
    or
    
    
    
def persistence(n):
    count = 0
    while n >= 9:
        count +=1
        new = [int(i) for i in str(n)]
        n = 1
        for x in new:
            n*=x
    return count
print(persistence(99))

or


from operator import mul

def persistence(n, res=0):
    return persistence(reduce(mul, map(int, str(n))), res+1) if n > 9 else res
