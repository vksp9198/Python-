# Problem : contains duplicate -> return True if any value appears atleast twice.
nums = [1,7,5,3,7]

for i in nums:
    if nums.count(i) == 2:
        print(f"True ,{i} repeated twice")
        break

