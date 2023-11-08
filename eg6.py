"""Find how many number of times the substring occuranceurs in the given string."""

my_string = "PQRQRQRQQRQ"    #given string
substring = "QRQ"         #sub string

occurrence = 0   #initially it 0 but substring is found in given string then it will increase by 1 

#both loops are iterate over lenght given string
for i in range(len(my_string)):
    for j in range(len(my_string)):
        if my_string[i:j+1] == substring: #string checking every part of itself till full part
            occurrence +=1       #when any string part is found which is equal to substring then ,
                                #it will increase occurence by 1

print(occurrence)   #finally we can see the number of substring occurrence