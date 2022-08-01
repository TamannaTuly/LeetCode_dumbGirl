# will do it using stack
stringi = "(){][}"
openList = ['[', '{', '(']
closeList = [']', '}', ')']

stack =[]

for i in stringi:
    if i in openList :
        stack.append(i)
    else:
        pos = closeList.index(i)
        if (len(stack)>0) and (openList[pos] == stack[len(stack)-1]):
            # print("balanced")
            stack.pop()
        else:
            print("not balanced")
if len(stack)==0:
    print("balanced")
else:
    print("unb2")