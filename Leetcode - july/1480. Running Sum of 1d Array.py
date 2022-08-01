#practice :
#given
nums = [1, 2, 3, 9]

# solution 1 :
for i in range(1, len(nums)):
    print(i)
    nums[i] += nums[i-1]
print(nums)


