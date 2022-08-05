# practice
# nums = [1, 2, 3, 4]
# final_mat = []
#
# for i in range(0, len(nums), 2):
#     frequency = nums[i]
#     for j in range(frequency):
#         final_mat.append(nums[i+1])
# print(final_mat)
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        final_matrix = []
        for i in range(0, len(nums), 2):
            frequency = nums[i]
            for j in range(frequency):
                final_matrix.append(nums[i+1])
        return final_matrix
