nums = [4,2,5,9,7,4,8]

max1 = max(nums)
nums.remove(max1)
max2 = max(nums)
min1 = min(nums)
nums.remove(min1)
min2 = min(nums)
print(max2)
print(max1)
print(min2)
print(min1)
result = (max2*max1)-(min2*min1)
print(result)