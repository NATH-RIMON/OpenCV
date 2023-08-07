# nums = [-1,0,3,5,9,12]

# target = 9
# first_index=0
# last_index= len(nums)-1
# target_index=0


# while first_index<=last_index:

#     mid=(first_index+last_index) //2

#     if nums[mid]==target:
#         target_index= mid
#         break
        
#     elif nums[mid]<target:
#         first_index=mid+1
        
        

#     elif nums[mid]>target:
#         last_index=mid-1

# print("Target Index is :" ,target_index)

#Second problem

nums = [-1,0,3,5,9,12]

target = 200
first_index=0
last_index= len(nums)-1
target_index=-1


while first_index<=last_index:

    mid=(first_index+last_index) //2

    if nums[mid]==target:
        target_index= mid
        break
        
    elif nums[mid]<target:
        first_index=mid+1
        
        

    elif nums[mid]>target:
        last_index=mid-1

    

print("Target Index is :" ,target_index)

