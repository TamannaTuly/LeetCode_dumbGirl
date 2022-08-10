arr = [1,4,2,5,3]
# cal = 0
# for i in range(len(arr)):
#     cal = cal+arr[i]
# if len(arr)%2 != 0:
#     cal = cal + sum(arr)
# if l
# print(cal)
# res = 0
# for i in range(1, len(arr) + 1):
#     sub = 0
#     s = i
#     e = (len(arr) + 1) - i
#     n = s * e
#
#     if n % 2 == 0:
#         sub = n // 2
#     else:
#         sub = (n // 2) + 1
#     res += sub * arr[i - 1]
# print(res)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(1, len(arr) + 1):
            sub = 0
            s = i
            e = (len(arr) + 1) - i
            n = s * e
            if n % 2 == 0:
                sub = n // 2
            else:
                sub = (n // 2) + 1
            res += sub * arr[i - 1]
        return res