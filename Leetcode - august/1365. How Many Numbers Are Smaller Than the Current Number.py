# practice
# nums = [6,5,4,8]
# res = nums.copy()
# countMat = []
#
# for i in range(len(nums)):
#     c = 0
#     for j in range(len(res)):
#         if i != j and nums[i] > res[j]:
#             c +=1
#         # else:
#         #     c = 0
#     countMat.append(c)
# print(countMat)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        countMat = []
        for i in range(len(nums)):
            calc = 0
            for j in range(len(res)):
                if i != j and nums[i] > res[j]:
                    calc +=1
            countMat.append(calc)
        return countMat