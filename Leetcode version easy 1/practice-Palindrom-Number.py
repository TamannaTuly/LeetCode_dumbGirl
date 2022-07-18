number = int(input("x="))

temp = number
rest = 0

while number>0:
    # print("number"+str(number))
    dig = number%10
    rest=rest*10+dig
    number = number//10
    # print("number" + str(number))
    # print("temp"+str(temp))
    # print("rest"+str(rest))
    if temp==rest:
        print("its a palindrome")
    else:
        print("its not a palindrome")



# explanation :
# 1st loop :  number 121
#             temp 121
#             dig 1
#             rest 1
#             number 12
# 2nd loop :  number 12
#             temp 121
#             dig 2
#             rest 12 (1*10+2)
#             number 1
# 3rd loop :  number 1
#             temp 121
#             dig 1
#             rest 121 (12*10+1)
#             number 0
# 4th loop :  will not run as number is not greater than 0