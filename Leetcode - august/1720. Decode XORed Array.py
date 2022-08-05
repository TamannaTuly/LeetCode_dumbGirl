# practiced but could not succeed
# encoded =[6,2,7,3]
# first = 4
# arr = [first]
# for i in range(0,len(encoded)):
#     testNum = abs(encoded[i]- arr[i])
#     arr.append(testNum)
#
# print(arr)
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(0,len(encoded)):
            arr.append(encoded[i] ^ arr[i])
        return arr