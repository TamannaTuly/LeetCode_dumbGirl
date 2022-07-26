# practice

num = 14
sum =0
i = 0
while num !=0:
    if num % 2 == 0:
        sum = num/2
        num = sum
        # print(num)
        i += 1
        # print(i)
    elif num%2 != 0:
        sum = num-1
        num = sum
        # print(num)
        i += 1
        # print(i)
    else:
        i +=1
# i = i-1
print(i)
