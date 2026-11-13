arr = [1,2,3,4,5,6,7,8,9]
start = int(input("enter the starting value"))
end = int(input("enter the ending value"))
left = start
right = end
while left < right:
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left += 1
    right -= 1
print(arr)
