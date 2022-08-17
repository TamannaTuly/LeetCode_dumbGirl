# practice
# nums = [1,2,3,4]
# k = 1
# count = 0
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i<j and ((i*j) % k)==0 and nums[i] == nums[j]:
#             count +=1
#
# print(count)

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and ((i * j) % k) == 0 and nums[i] == nums[j]:
                    count += 1
        return count



