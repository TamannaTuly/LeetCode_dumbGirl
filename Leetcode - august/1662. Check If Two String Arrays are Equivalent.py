# practice
# word1 = ["abc", "d", "defg"]
# word2 = ["abcddefg"]
# s1 = ''
# s2 = ''
# for i in range(len(word1)):
#     s1 += word1[i]
# print(s1)
# for j in range(len(word2)):
#     s2 += word2[j]
# print(s2)
# if s1 == s2:
#     print("true")
# else:
#     print("false")


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''
        s2 = ''
        for i in range(len(word1)):
            s1 += word1[i]
        for j in range(len(word2)):
            s2 += word2[j]
        if s1 == s2:
            return True
        else:
            return False