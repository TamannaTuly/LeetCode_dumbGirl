# practice
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazineKeyCount = Counter(magazine) # counter means if a = 'abb' then counter(a) = ({'a' : 1, 'b' : 2})
        print(magazineKeyCount)

        for val in ransomNote:

            if val in magazineKeyCount and magazineKeyCount[val] > 0:
                print(magazineKeyCount)
                print(magazineKeyCount[val])
                # drop one count for val
                magazineKeyCount[val] -= 1
            else:
                # No such letter exists in magazine
                return False
        return True
