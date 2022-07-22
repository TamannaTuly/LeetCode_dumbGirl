list1 = [1,2]
list2 = [0]

# one way of sorting:
# list3 = sorted(list2+list1)
#
# print(list3)


# second way:
res = []
i = j = 0

while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        res.append(list1[i])
        i += 1
    else:
        res.append(list2[j])
        j += 1
res = res + list1[i:] + list2[j:]
print(res)
