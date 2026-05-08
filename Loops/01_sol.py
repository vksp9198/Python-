# Problem : count how many are positive in given list 
list = [1, 3, 23, -3, 9 , 6, -3,-4 ,5,-8]
count = 0
for num in list:
    if num > 0:
        count = count + 1
print("total positive number in list is : ", count)