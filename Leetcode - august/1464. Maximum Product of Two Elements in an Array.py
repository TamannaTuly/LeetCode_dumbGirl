# practice
# nums = [3,4,5,2]
# nums.sort()
# max1 = max(nums)
# maxInd = nums.index(max1)
# print(maxInd)
# nums.remove(max1)
# max2 = max(nums)
# res = (max1-1)*(max2-1)
# print(res)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        max1 = max(nums)
        maxInd = nums.index(max1)
        nums.remove(max1)
        max2 = max(nums)
        res = (max1-1)*(max2-1)
        return res