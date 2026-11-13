n =[1,2,3,4,5,6,7]
k = int(input("enter the input of k value to rotate array"))
k= k % len(n)
left = 0
right = len(n) - 1
while left < right:
    temp = n[left]
    n[left] = n[right]
    n[right] = temp
    left += 1
    right -= 1
left = 0
right = k-1
while left < right:
    temp = n[left]
    n[left] = n[right]
    n[right] = temp
    left += 1
    right -= 1
left = k
right = len(n) - 1
while left < right:
    temp = n[left]
    n[left] = n[right]
    n[right] = temp
    left += 1
    right -= 1
print(n)