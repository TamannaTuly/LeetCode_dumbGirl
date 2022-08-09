# practice
# nums = [4,5,6,7,8,9]
# diff = 2
# count = 0
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         for k in range(len(nums)):
#             if (i < j < k) and (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
#                 count += 1
# print(count)

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i < j < k) and (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                        count += 1
        return count