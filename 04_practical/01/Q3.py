# Head recursion that counts from n to 0
def count_down(n):
    if n>=0:
        print(n)
        count_down(n-1)
        
print("Count down to 0")
count_down(5)
