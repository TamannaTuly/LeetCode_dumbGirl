# practice
# items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
# ruleKey = "type"
# ruleValue = "phone"
#
# if ruleKey == "type":
#     index = 0
# elif ruleKey == "color":
#     index = 1
# else:
#     index = 2
# count = 0
# for i in items:
#     # print(items[index])
#     if i[index] == ruleValue:
#         count += 1
# print(count)

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2
        count = 0
        for i in items:
            if i[index] == ruleValue:
                count += 1
        return count
