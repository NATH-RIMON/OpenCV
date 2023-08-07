nums = [1, 2, 3, 4]
# new_nums = []

# for val in nums:
#     cal = val * 2
#     new_nums.append(cal)

new_nums = [val * 2 for val in nums if val != 3]

print(nums)
print(new_nums)
