"""You are given a list of numbers and your task is to find out the pairss that have sum equals n (provided during input)."""


numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]    #Given List
n=12        #input for check sum of two pair
pairs=[]    #it will store pair whose sum is n

for number in numbers:
    for item in range(len(numbers)):
        if(number+numbers[item]==n):
            #now it checking pair is not exist inside pairs list
            if not [number,numbers[item]] in pairs and not [numbers[item],number] in pairs:         
                    pairs.append([number,numbers[item]])  #it store the two number whose sum is n as list

print(pairs)            #shows the element pairs whose sum is = n,without come twice"""
