nums = [1,2,3,4]
sum_lis=[]
_lis=0
for i in nums:

    _lis += i 

    sum_lis.append(_lis)


print(sum_lis)


nums = [1,2,3,1,1,3]

for i in nums:
    for j in nums:
        if nums[i] == nums[j] and enumerate(i < j):
            count += 1





