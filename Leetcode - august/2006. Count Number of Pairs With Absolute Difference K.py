# nums = [3,2,1,5,4]
# numsCopy = nums.copy()
# k = 2
# res = 0
# for i in range(len(nums)):
#     for j in range(len(numsCopy)):
#         if i < j and (abs(nums[i]-numsCopy[j]) == k):
#             res += 1
#         else:
#             res += 0
# print(res)

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        numsCopy = nums.copy()
        res = 0
        for i in range(len(nums)):
            for j in range(len(numsCopy)):
                if i < j and (abs(nums[i]-numsCopy[j]) == k):
                    res += 1
                else:
                    res += 0
        return res

