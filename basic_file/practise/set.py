# A = {1, 2, 3}
# B = {3, 4, 5}

# C = A.union(B) - A.intersection(B)

# print(C) 

nums = [1, 2, 3, 1]

if len(nums) != len(set(nums)):
    print("YES")
else:
    print("NO")

nums = [1, 2, 3]

if len(nums) != len(set(nums)):
    print("YES")
else:
    print("NO")
