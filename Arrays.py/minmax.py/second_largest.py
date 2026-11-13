n = int(input("enter the array size"))
arr = []
for i in range(n):
    nums = int(input())
    arr.append(nums)
if (len(arr) < 2):
    print(-1)
else:
    min = arr[0]
    max = arr[0]
    for i in range(0,len(arr)-1):
        if arr[i+1] > max:
            max = arr[i+1]
        elif arr[i+1] < min:
            min = arr[i+1]
    if max == min:
        print(-1)
    else:
        second_max = min
        for i in range(0,len(arr)):
            if arr[i] < max and arr[i] > second_max:
                second_max = arr[i]
        print(second_max)
