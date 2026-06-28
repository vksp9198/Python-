# print the fibonacci series
# 0,1,2,3,5,8,13,21,
def fibo(n):
    if n <=1:
        return n
    return fibo(n-1) + fibo(n-2)
    
print(fibo(2))


