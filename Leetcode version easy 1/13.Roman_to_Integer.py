class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        initial_value = 0
        for i in range (len(s)):
            if i>0 and roman_value[s[i]]>roman_value[s[i-1]]:
                initial_value += roman_value[s[i]]-2*roman_value[s[i-1]]
            else:
                initial_value += roman_value[s[i]]
        return initial_value