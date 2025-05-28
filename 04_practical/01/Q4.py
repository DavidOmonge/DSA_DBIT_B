# Using tail recursion
def tail_sum(n, x=0):
    if n == 0:
        return x
    else:
        return tail_sum(n-1, x+n)
        
print(tail_sum(5))
