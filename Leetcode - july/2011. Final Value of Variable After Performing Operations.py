# practice 2 to 11
# test = ["++X", "X--", "X--"]
# j=0
# for i in range(len(test)):
#     if test[i] == "++X" or test[i] == "X++":
#         j += 1
#     elif test[i] == "--X" or test[i] == "X--":
#         j -= 1
#     else:
#         print(j)
# print(j)

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        j = 0
        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] == "X++":
                j +=1
            elif operations[i] == "--X" or operations[i] == "X--":
                j -=1
        return j

