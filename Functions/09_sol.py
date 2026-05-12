# Problem : write a Generator function that yield even number upto specific limit 

def even_generator(limit):
    for num in range(2, limit + 1, 2):       # Original method
        yield num
    

for num in even_generator(10):
    print(num)



# def even_generator(limit):
#     for num in range(2, limit + 1, 2):
#         print(num)            //method - I
# even_generator(10)