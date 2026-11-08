nums = [10,20,5,40] 
max_value = nums[0]
min_value = nums[0]
for i in range(0,len(nums)-1):
    if max_value < nums[i+1]:
        max_value = nums[i+1]
    elif min_value > nums[i+1]:
        min_value = nums[i+1]
print(max_value)
print(min_value)

