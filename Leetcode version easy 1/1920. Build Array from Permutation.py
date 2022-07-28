# practice from 2 to 8
# nums = [5,0,1,2,3,4]
# ans =[]
# for i in range((len(nums))):
#     ansr= nums[nums[i]]
#     ans.append(ansr)
#
# print(ans)

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        i = 0
        ansr =[]
        for i in range(len(nums)):
            ans = nums[nums[i]]
            ansr.append(ans)
        return ansr