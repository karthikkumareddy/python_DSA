n = int(input("enter the array size"))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
min = arr[0]
max=arr[0]
max_index = 0
min_index = 0
for i in range(0,len(arr)-1):
    if arr[i+1] > max:
        max = arr[i+1]
        max_index = i+1
    elif arr[i+1] < min:
        min = arr[i+1]
        min_index = i+1
    difference = max - min
print(f"{max} and index value is {max_index}")
print(f"{min} and index value is {min_index}")
print(difference)