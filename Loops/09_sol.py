# Problem : 
# List uniqeness checker = Check if all elements in a
# list are unique. if a duplicate is found.
# exit the loop and print the duplicate.


List = [1, 2 ,3, 4, 5,9, 6 ,7,4,5 ]
unique_item = set()
# print(unique_item)

# for elements in List:
#     print(elements)
#     if List.count(elements) != 1:    Method - I
#         print(elements)
#         break

for elements in List:
    if elements in unique_item:
        print("Duplicate = ", elements)
        # break
    unique_item.add(elements) 
