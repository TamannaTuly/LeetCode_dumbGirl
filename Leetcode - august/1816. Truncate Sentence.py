# practice
# s = "Hello how are you Contestant"
# k = 4
# list1 = s.split()
# listf =[]
# for i in range(k):
#     listf.append(list1[i])
# t = ' '.join(listf)
# print(t)

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list1 = s.split()
        listf = []
        for i in range(k):
            listf.append(list1[i])
        t = ' '.join(listf)
        return t





