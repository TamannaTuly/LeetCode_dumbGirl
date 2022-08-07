# practice
# nums = [6]
# index = [0]
#
# target = []
#
# for i in range(len(index)):
#     target.insert(index[i], nums[i])
# print(target)

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(index)):
            target.insert(index[i],nums[i])
        return target