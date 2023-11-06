"""Print the following patterns. In the patterns"""

n=3
for i in range(n,1,-1):      #loop is reversing from n
    for j in range(i,0,-1):  #loop is reversing from value on n
        print ("*",end=" ")  #printing * by first inner loop

    for j in range (2*(n-i)):  #loop is executes as by decrese value of n by i to 2
        print(" ",end=" ")     #then prints space on that place

    for j in range(i,0,-1):   #loop reversing from i to 0
        print ("*",end=" ")   #thwn prints the * on remaining place
    print()                   #makes new line after finish one execution of loop

for i in range(n):
    for j in range(i+1):       #loop is executes by increse value of i as 1
        print ("*",end=" ")     #then prints * with space

    for j in range(2*(n-i-1)): #loop is executes by reducing n from i and 1
        print(" ",end=" ")      #then prints space on those place

    for j in range(i+1):        #then loop executes by incrsing i to 1
        print ("*",end=" ")     #then prints * with space
    print()                     #makes new line after finish one execution of loop


#_____________________________________________________________________________________


n = 3   
for i in range(n-1): 
   for j in range(i, n): 
      print(' ', end=' ')  #it prints the space at first 3 by reducing to n
   for j in range(i):
      print('*', end=' ')  #it prints start(*) after above loop finished on required place
   for j in range(i+1): 
      print('*', end=' ')  #and on required place it print * by incresing 1 in i
   print()                 #takes new line after finish one execution of root loop

#half dimond will be printed now
#below code for print remaining half dimond

for i in range(n): 
   for j in range(i+1):  
      print(' ', end=' ') 
   for j in range(i, n-1):
      print('*', end=' ')
   for j in range(i, n):
      print('*', end=' ')   #it fills * on remaining place just reverse above loop code
   print()                  #takes new line after finish one execution of root loop



#_____________________________________________________________________________________


n=5
for i in range(n): 
    for j in range (i+1) :
        if ( i==n-1 or j==0 or j==i):  #cheking the inner loop is satisfied as outer loop by incresing the value of i
            print ( '* ', end ='')      #it prints * with the space after codition true
        else :
            print( '  ', end ='')       #else it prints the space 

    print ()                             #makes new line after finish one execution of loop


#_____________________________________________________________________________________


n=5                                  #number of * user want
#both loops iterates over given n
for i in range(n):
    for j in range(n):
      if i == 0 or i == n - 1 or j == 0 or j == n - 1: #cheking the inner loop with the i and j which are equal to  zero or not
        print("* ", end="")                             #it prints * with the space after codition true
      else:
        print("  ", end="")                              #else it prints the space 
    print()                                              #makes new line after finish one execution of loop



#_____________________________________________________________________________________


one = 1    #first position
line = 5   #how many rows will be in traingle
stop = 2   #to take a break with each row

#this loop iterate over number of rows 
for i in range(line):
    for column in range(1, stop):   #this loop excutes till value 1 to stop value
        print(one, end=' ')        #it prints the value with space
        one += 1                   #value will be incresed by one after every execution
    print()                        #makes new line after finish one execution of loop
    stop += 1                     #value of of stop will be increse for make 1 digit long in next row
