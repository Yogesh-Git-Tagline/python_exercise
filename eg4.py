"""Create a recursive function which returns the n-th Fibonacci number. [Fibonacci
sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]"""

store = {0: 0, 1: 1}  #this dictionary is for store sum of pervious two terms

def fibbonaci_function(item):
    if item in store:  
        return store[item]
    store[item] = fibbonaci_function(item - 1) + fibbonaci_function(item - 2)  #adding number with previous number by calling function itself and will update store_dictionary
    return store[item]

term=60                                     #given term we want to find fibbonaci number on it

for element in range(term+1):
    item=fibbonaci_function(element)       #it sending the elemenet one by one as an argument

print(store[term])                          #it will shows the fibonacci number of provided term

#-------------------------------------------------------------------------

"""Create a recursion function that calculate the sum of numbers present in the list."""

def calculate_sum(numbers):
   if len(numbers) == 1:        #checking the length of list
        return numbers[0]       #it returning last value when length of list is 1
   else:
        return numbers[0] + calculate_sum(numbers[1:]) #it adding 0th index of list with passing list except 0th index value to add it with 0th index

numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]   #given list
print(calculate_sum(numbers))               #calling and passing list to function


