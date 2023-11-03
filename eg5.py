"""You are given a list of numbers and your task is to find out the pairs that have sum equals n (provided during input)."""


Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]  # Given List
n = 12  # input for check sum of two num
Pair = []

for i in Numbers:
    for j in range(len(Numbers)):
        if (i+Numbers[j] == n):
            # it store the two number whose sum is n as list
            Pair.append([i, Numbers[j]])


DuplicatePair = []  # list for add duplicate pair
temp = []  # list for add pair without duplicate
for i in Pair:
    if i not in temp:
        temp.append(i)  # storing elements without duplicate
    elif i not in DuplicatePair:
        DuplicatePair.append(i)

final = []
for i in temp:
    final.append(sorted(i))  # it store the sorted pair in final list

# then it will remove the duplicate pair again by below loop
duplicatePairs = []
result = []
for i in final:
    if i not in result:
        result.append(i)
    elif i not in duplicatePairs:
        duplicatePairs.append(i)

print(result)  # shows the element pair whose sum is = n,without come twice
