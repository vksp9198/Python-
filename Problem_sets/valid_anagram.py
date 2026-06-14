# # program: check if both strings are anagram. 
# s = "listen"
# t = "silent"

#method - I
# def is_anagram(s,t):
#     return sorted(s) == sorted(t)
# print(is_anagram("listen" , "silent"))   

#method - II [hash map/ dictionary]

# def is_anagram(s,t):
#     if len(s) != len(t):
#         return False
    
#     count = {} 
#     print(count)
#     for ch in s:
#         count[ch] = count.get(ch,0) + 1

#     for ch in t:
#         if ch not in count:
#             return False
#         count[ch] -= 1
        
#         if count[ch] < 0:
#             return False
#     return True

# print(is_anagram("listen" , "vikase"))

# Buil-in method for anagram
from collections import Counter
def is_anagram(s,t):
    Counter(s) == Counter(t)
    return True
print(is_anagram('listen' , 'silent'))
