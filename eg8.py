"""You are given a list of numbers and your task is to sort the list without any inbuilt method of python."""

#Given list
numbers = [2, 5, 6, 1, 3, 8, 9, 10,45,67,34]

#both loops iterate over numbers-list
for i in range(len(numbers)):           #this loop iterating by length of number list
    for j in range(i+1,len(numbers)):   #this loop iterating by incresing value of i to len of list
        if(numbers[i]>numbers[j]):      #it comparing first item is grater or not with next item
            temp=numbers[i]             #if it grater then,it will assign that num in temp varible
            numbers[i]=numbers[j]       
            numbers[j]=temp             #grater item will be replaced by smaller item
        
print(numbers)    #finally we can see sorted number list without using built in method