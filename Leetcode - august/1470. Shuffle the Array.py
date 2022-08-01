#practice from line 2 to 8
# nums = [1,2,3,4,4,3,2,1]
# final_nums = []
# n = 4
# for i in range(n):
#     final_nums.append(nums[i])
#     final_nums.append(nums[i+n])
# print(final_nums)

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final_nums = []
        for i in range(n):
            final_nums.append(nums[i])
            final_nums.append(nums[i+n])
        return final_nums