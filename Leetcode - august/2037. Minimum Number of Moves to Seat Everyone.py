# seats = [3, 1, 5]
# students = [2, 7, 4]
# seats.sort()
# students.sort()
# matInitial = []
# matFinal = []
#
#
# for i in range(len(seats)):
#     countFinal = 0
#     for j in range(len(students)):
#         countInitial = 0
#         if seats[i] == students[j]:
#             countInitial = 0
#             matInitial.append(countInitial)
#         elif seats[i] > students[j]:
#             countInitial = seats[i] - students[j]
#             matInitial.append(countInitial)
#         elif seats[i] < students[j]:
#             countInitial = students[j]-seats[i]
#             matInitial.append(countInitial)
#         else:
#             countInitial = 0
#             matInitial.append(countInitial)
#     countFinal = min(matInitial)
#     matFinal.append(countFinal)
# print(sum(matFinal))

# result = 0
# for i in range(len(seats)):
#     result +=abs(seats[i]-students[i])
# print(result)

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        result = 0
        for i in range(len(seats)):
            result +=abs(seats[i]-students[i])
        return result