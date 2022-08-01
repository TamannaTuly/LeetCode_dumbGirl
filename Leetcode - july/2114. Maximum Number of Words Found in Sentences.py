sentences = ["i am tuly", "he is minar t", "ok"]
# maxi = 0
# lenthi = len(sentences)
# for i in range(lenthi):
# 	maxi = max(maxi,len(sentences[i].split(" ")))
#
# print(maxi)
j = 0
for i in range(len(sentences)):
	print(sentences[i])
	print(j)
	print(len(sentences[i].split(" ")))
	j = max(j,(len(sentences[i].split(" "))))
	print(j)

print(j)
