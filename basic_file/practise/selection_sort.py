# nums = [102, 56, 34, 99, 89, 101, 10]

# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)):
#         if nums [i]>nums[j]:
#             nums[i],nums[j]=nums[j],nums[i]

# a=len(nums)
# b=nums[a//2]
# print(b)

nums=[102, 56, 34, 99, 89, 101, 10, 54]

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] >nums[j]:
            nums[i],nums[j]=nums[j],nums[i]

a=len(nums)
b=nums[(a//2)-1]
c=nums[a//2]

a=b+c
a=a/2
print(a)




