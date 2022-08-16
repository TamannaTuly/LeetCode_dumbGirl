# practice
# arr = [3,0,1,1,9,7]
# a = 7
# b = 2
# c = 3
# count = 0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         for k in range(j+1, len(arr)):
#             ma = abs(arr[i] - arr[j])
#             mb = abs(arr[j] - arr[k])
#             mc = abs(arr[i] - arr[k])
#             if ma <= a and mb <= b and mc <= c:
#                 count += 1
# print(count)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    ma = abs(arr[i] - arr[j])
                    mb = abs(arr[j] - arr[k])
                    mc = abs(arr[i] - arr[k])
                    if ma <= a and mb <= b and mc <= c:
                        count += 1
        return count