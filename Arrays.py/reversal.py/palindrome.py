arr = [1,2,3,2,1]
left=0
is_valid = True
right = len(arr) -1
while left < right:
    if arr[left] != arr[right]:
        is_valid = False
        break
    left += 1
    right -= 1
if is_valid == True:
    print("palindrome")
else:
    print("not palindrome")

       