"""You are given a list of numbers and your task is to find out the pairss that have sum equals n (provided during input)."""


numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]    #Given List
n=12        #input for check sum of two pair
pairs=[]    #it will store pair whose sum is n

for number in numbers:
    for item in range(len(numbers)):
        if(number+numbers[item]==n):
            pairs.append([number,numbers[item]])  #it store the two number whose sum is n as list


duplicate_pairs=[]       #list for store duplicate pairs
final_pairs=[]           #list for add pairs without duplicate
for pair in pairs:
    if pair not in final_pairs:
        final_pairs.append(pair)     #storing pairs without duplicate
    elif pair not in duplicate_pairs:
        duplicate_pairs.append(pair)

sorted_pairs=[]        
for pair in final_pairs:
    sorted_pairs.append(sorted(pair))  #it store the sorted pairs in final list
   
#then it will remove the duplicate pairs again by below loop
filter_duplicate_pairs=[]         
result=[]
for pair in sorted_pairs:
    if pair not in result:
        result.append(pair)          #storing pairs without duplicate
    elif pair not in filter_duplicate_pairs:
        filter_duplicate_pairs.append(pair)

print(result)  #shows the element pairs whose sum is = n,without come twice