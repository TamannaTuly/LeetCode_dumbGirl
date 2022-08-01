# practice 3 to 22

# num = 14
# sum =0
# i = 0
# while num !=0:
#     if num % 2 == 0:
#         sum = num/2
#         num = sum
#         # print(num)
#         i += 1
#         # print(i)
#     elif num%2 != 0:
#         sum = num-1
#         num = sum
#         # print(num)
#         i += 1
#         # print(i)
#     else:
#         i +=1
# # i = i-1
# print(i)


# solution :
class Solution:
    def numberOfSteps(self, num: int) -> int:
        final_num = 0
        i = 0

        while num != 0:
            if num % 2 == 0:
                final_num = num / 2
                num = final_num
                i += 1
            elif num % 2 != 0:
                final_num = num - 1
                num = final_num
                i += 1
            else:
                i += 1
        return i