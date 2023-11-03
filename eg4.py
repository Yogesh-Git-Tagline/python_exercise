"""Create a recursive function which returns the n-th Fibonacci number. [Fibonacci
sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]"""


# def Fibbonaci_fun(n):
#    if n <= 1:
#        return n
#    else:
#        return Fibbonaci_fun(n-1) + Fibbonaci_fun(n-2) #adding number with previous number by calling function itself

# end = 60
# for i in range(end):
#     print(Fibbonaci_fun(i))

"""
Above program not able to find 60th term, so i used dictionary to store each sum of pervious two terms
"""

store = {0: 0, 1: 1}  #this store-dictionary used to store each sum of pervious two terms

def Fibbonaci_fun(n):
    if n in store:  
        return store[n]
    store[n] = Fibbonaci_fun(n - 1) + Fibbonaci_fun(n - 2)  #adding number with previous number by calling function itself and will update store_dictionary
    return store[n]

FibonaciSeries=[]   #list for append the comming fibonacci number
end=60

for i in range(60+1):
    element=Fibbonaci_fun(i)       #it sending the element one by one as an argument
    FibonaciSeries.append(element) #it adding comming fibonacci element in list 

print(store)   #it print the item with their fibbonaci number
print(FibonaciSeries)  #it will shows the fibonacci number till user number

