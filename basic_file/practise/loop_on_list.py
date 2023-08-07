nums = [1, 2, 6, 4]
length = len(nums)
for idx in range(0, length, 1):
    print(nums[idx])


# for val in nums:
#     print(val)

for idx, val in enumerate(nums):
   print("Index:", idx, "value:", val)

for i in range(len(nums)):
    if 4 == nums[i]:
        print("44 is in this list")


if 4 in nums:
    print("4 is in this list")
    
