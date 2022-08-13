# practice
# allowed = "ab"
# w = ["ad", "bd", "aaab", "baa", "badab"]
# count = 0
#
# for word in w:
#     flag = True
#     print(word)
#     for c in word:
#         print(c)
#         if c not in allowed:
#             flag = False
#     if flag == True:
#         count += 1
# print(count)

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for c in word:
                if c not in allowed:
                    flag = False
            if flag == True:
                count += 1
        return count

