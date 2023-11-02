"""You are given a list of person names. Your task is to find out the three most frequent and three least frequent names."""


names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']   #created list with person names  

print('Name List=',names)      #here we will see the list of persons 

LengthOfItems=[]     #created empty list for store the len of each element

#below empty lists created for store the equal length
Length5=[]  #item with length 5
Length6=[]  #item with length 6
Length7=[]  #item with length 7
Length8=[]  #item with length 8

#this loop is for storing the item length in their allocated list
for i in names:
    LengthOfItems.append(len(i))
    if(len(i)==5):
       Length5.append(i)
    elif(len(i)==6):
        Length6.append(i)
    elif(len(i)==7):
        Length7.append(i)
    elif(len(i)==8):
        Length8.append(i)

print(LengthOfItems)    #here we see the list of length with each item


#now we print the three most frequent name lenghts
print("The three most frequent name lenghts are:")
print(len(Length5),"names of length 5:",Length5)
print(len(Length6),"names of length 5:",Length6)
print(len(Length8),"names of length 5:",Length8)

#now we print the three least frequent name lenghts
print("The three least frequent name lenghts are:")
print(len(Length7),"names of length 5:",Length7)
print(len(Length8),"names of length 5:",Length8)
print(len(Length6),"names of length 5:",Length6)