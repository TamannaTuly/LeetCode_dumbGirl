s = "leetcode"
# list1 = []
# list1[:0] = s

for i in range(len(s)):
    c = s.count(s[i])
    print(c)
    if c == 1:
        ind = s[c]
        break
    else:
        ind = -1
print(ind)


# print(list1)
# for i in range(len(list1)):
#     c = list1.count(list1[i])
#     if c == 1 :
#         ind = list1.index(list1[i])
#         break
#     else:
#         ind = -1
# print(ind)




