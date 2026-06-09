# Problem : first non-repeated character(Return the index of the first unique character)
s = 'leetcode'

for i, ch in enumerate(s):
    if s.count(ch) == 1:
        print(f"Index of first unique character ({ch}) = {i}")
        break