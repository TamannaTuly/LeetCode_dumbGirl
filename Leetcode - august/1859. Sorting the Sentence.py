# practice
# s = "is2 sentence4 This1 a3"
# temp= s.split()
# word={}
# ans=''
# for i in temp:
#     # print(word[i[-1]])
#     # print(i[:-1])
#     word[i[-1]] = i[:-1]
#     # print(word[i[-1]])
#     print(word)
# for i in sorted(word):
#     print(sorted(word))
#     ans=ans+''.join(word[i])+' '
# ans=ans[:-1]
# print(ans)

class Solution:
    def sortSentence(self, s: str) -> str:
        temp= s.split()
        word={}
        ans=''
        for i in temp:
            word[i[-1]]= i[:-1]
        for i in sorted(word):
            ans=ans+''.join(word[i])+' '
        ans=ans[:-1]
        return ans

