"""Here you are given two series input one is arithmetic progression (A.P.) and another one is geometric progression (G.P.). In which, one of the terms is wrong. Your task is to find out the wrong term and replace it with correct term."""


arithmetic_prog = [2, 5, 8, 12, 14, 17]                         #given arithmatic progression

#below loop is iterating from 1 index to last-second index of arithmatic list
for i in range(1, len(arithmetic_prog)-1):
    #it checking the substraction of second item with first item is not equal to the substraction of first item with list of first item reduce by 1
    if arithmetic_prog[i+1] - arithmetic_prog[i] != arithmetic_prog[i] - arithmetic_prog[i-1]:
        wrong_term = i+1                                     #wrong term is foundin list by incresing index by 1+1
        #then assign correct term with addition of ith term minus wrong term
        correct_term = arithmetic_prog[i] + arithmetic_prog[i] - arithmetic_prog[i-1] 
        print("Wrong term:", arithmetic_prog[wrong_term])   #wrong term will be printed here
        arithmetic_prog[wrong_term] = correct_term          #it modifying wrong term with correct term

print("correct term is:", arithmetic_prog)                  #finally we will see list with correct terms.

print()     #just for above and below code output display differently



geometric_prog = [3, 9, 27, 81, 244, 729]                         #given geometric progression

#below loop is iterating from 1 index to last-second index of arithmatic list
for i in range(1, len(geometric_prog)-1):
     #it checking the division of second item with first item is not equal to the division of first item with list of first item reduce by 1
    if geometric_prog[i+1]/geometric_prog[i] != geometric_prog[i]/geometric_prog[i-1]:
        wrong_term = i+1                                    #wrong term is foundin list by incresing index by 1+1
        #then assign correct term with multiplication of reduces term of i with first element of geometric progression
        correct_term = geometric_prog[i-1]*geometric_prog[1]
        print("Wrong term:", geometric_prog[wrong_term])        #wrong term will be printed here
        geometric_prog[wrong_term] = correct_term               #it modifying wrong term with correct term

print("Correct term is:", geometric_prog)                       #finally we will see list with correct terms.
