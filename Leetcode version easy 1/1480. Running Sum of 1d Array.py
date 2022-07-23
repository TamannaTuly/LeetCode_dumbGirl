#practice :
#given
nums = [1, 2, 3, 4]
# res = []
# i = 0
# for i in range(len(nums)):
#     sum = nums[i]
#     returnSum = res[i]
#     test = sum+returnSum
#     print(sum)
#     print(test)
#     res.append(test)
# print(res)

for i in range(1, len(nums)):
    print(i)
    nums[i] += nums[i-1]
print(nums)
