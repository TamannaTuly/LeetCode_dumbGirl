# practice
# mat = [[1,2,3], [1,2,3],[1,2,3]]
# n = len(mat)
# sum = 0
# for i in range(len(mat)):
#     sum +=mat[i][i]+mat[i][n-i-1]
# if n%2 ==1:
#     sum -= mat[n//2][n//2]
# print(sum)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(len(mat)):
            sum +=mat[i][i]+mat[i][n-i-1]
        if n%2 ==1:
            sum -= mat[n//2][n//2]
        return sum
