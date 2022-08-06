# practice
# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# shuffle  = [None]*len(s)
#
# for i in range(len(indices)):
#     shuffle[indices[i]] = s[i]
#
# t = ''.join(shuffle)
# print(t)

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle  = [None]*len(s)
        for i in range(len(indices)):
            shuffle[indices[i]] = s[i]
        t = ''.join(shuffle)
        return t