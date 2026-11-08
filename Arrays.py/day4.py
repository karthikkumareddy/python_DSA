# nums = [10,20,30,40,50]
# target = int(input("Enter yor target number"))
# for i in range(0,len(nums)-1):
#     if (nums[i] == target):
#         print(i)
nums = [10,20,30,40]
target = int(input("enter your target number"))
found_index = -1
for i in range(len(nums)):
    if (nums[i] == target):
        found_index = i

print(found_index)