# practice
# candies = [2,3,5,1,3]
# extraCandies = 3
# bool_array = []
# max_candy = max(candies)
#
# for i in range(len(candies)):
#     per_kid_max_candy = candies[i]+extraCandies
#     # print(per_kid_max_candy)
#     if per_kid_max_candy >= max_candy:
#         bool_array.append("true")
#     else:
#         bool_array.append("false")
# print(bool_array)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        kids_max = []
        for i in range(len(candies)):
            per_kids_max_candy = candies[i] + extraCandies

            if per_kids_max_candy >= max_candy:
                kids_max.append(True)
            else:
                kids_max.append(False)
        return kids_max