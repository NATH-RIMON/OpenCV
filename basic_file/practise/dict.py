# nums =  [1,1,1,3]
# num_dict = {}

# for i in nums:
#     if i in num_dict:
#         print(True)  
#         break
#     else:
#         num_dict[i] = True

# else:
#     print(False) 

# nums = [2,7,11,15]
# target = 9

# num_dict = {}
# bool_ = False

# for i in nums:
#     sum_val = target-i
#     if sum_val in num_dict:
#         bool_ = True
#         break
#     num_dict[i] = True

# if bool_:
#     print("YES")
# else:
#     print("NO")

nums = [1, 2, 3, 1]
k = 3

num_dict = {}

for i, j in enumerate(nums):
    if j in num_dict and abs(i - num_dict[j]) <= k:
        print(True)
        break
    num_dict[j] = i
else:
    print(False)


