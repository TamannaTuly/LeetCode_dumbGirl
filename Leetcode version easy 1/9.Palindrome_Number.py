class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rest = 0
        while x > 0:
            foot_value = x % 10
            rest = rest * 10 + foot_value
            x = x // 10

        if temp == rest:
            return True
        else:
            return False
