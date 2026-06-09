num = [2,3,7,5,3,11,4]
target  = 9

# basic Approach   Time complexity = O(n2)
# for i in range(len(num)):
#     # print(i)
#     for j in range(i+1 , len(num)):
#         # print(j)
#         if num[i] + num[j] == target:
#             print([i,j])
#     break

# Dictionary Appraoch --- Time complexity = O(n)
# Recommended approach
seen = {}
for i , data in enumerate(num):
    need = target - data
    if need in seen:
        print([seen[need] , i])
        break
    seen[data] = i




