# practice
# address = "1.1.1.1"
# t = address.replace(".","[.]")
# print(t)
# print(address)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        t = address.replace(".","[.]")
        return t