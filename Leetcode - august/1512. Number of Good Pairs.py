# practice
# nums = [1,1,1,1]
# counter = 0
# for i in range(len(nums)-1):
#     for j in range(1,len(nums)):
#         if i<j:
#             if nums[i] == nums[j]:
#                 counter += 1
# print(counter)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if i<j:
                    if nums[i] == nums[j]:
                        counter += 1
        return counter