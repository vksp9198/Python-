# problem : find the Sum of even number in given range(n= 14)  
n = 10
sumEven = 0 
for num in range(1, n+1):
    if num % 2 == 0:
        sumEven = sumEven + num
print("Sum of even number is = ", sumEven)

     
# output : Sum of even number is =  30 