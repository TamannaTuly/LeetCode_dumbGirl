# practice 3 to 5
#
# n = [1,2,1]
# num = n+n
# print(num)


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final_nums = nums+nums
        return final_nums