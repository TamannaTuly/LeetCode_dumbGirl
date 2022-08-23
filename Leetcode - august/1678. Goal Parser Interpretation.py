# practice
# command = "G()()()()(al)"
# t = command.replace("()","o")
# s = t.replace("(al)","al")
# print(s)

class Solution:
    def interpret(self, command: str) -> str:
        t = command.replace("()", "o")
        s = t.replace("(al)", "al")
        return s
