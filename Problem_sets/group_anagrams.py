# Group words that are anagrams
words = ["ate", "tea", "eat", "ten" ,"net", "set","est"]

groups = {}

for word in words:
    key = "".join(sorted(word))
    #print(key)
    
    if key not in groups:
        groups[key] = []
    groups[key].append(word)

# print(groups)

for key , data in groups.items():
    print(f"{key} : {data}")