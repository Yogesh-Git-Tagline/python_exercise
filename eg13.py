"""Create a class name Number with the following methods."""


from functools import reduce  #importing reduce from functool to work with reduce module

#class creation
class Number:
    def __init__(self,numbers):  #constructor for assign number list in number variable
        self.numbers=numbers   

    def get(self):              #get method is returning list of numbers
        return self.numbers
    
    def change_original_values(self,func): #this method gives function from argument to work with map method
        mp=list(map(func,self.numbers))   #map method is changing all values and we convert those values them into list
        return mp                         #returning the list of changed values

    def filter_values(self,filter_func):    #this method gives function from argument to work with filter method
        fil=list(filter(filter_func,self.numbers))  #filter method is filters values and we convert those values in list
        return fil                                #returning the list of filtred values

    def compound_the_numbers(self,reduce_func):   #this method gives function from argument to work with reduce method
        red=reduce(reduce_func,self.numbers)    #reduce method will gives single value
        return red                              #returning that single value
 
    def sort(self):                             #this function is for only sort the list of number
        return sorted(self.numbers)

if __name__ == "__main__":                        #this checking the current module is __main__ or not
    
    numbers = [2, 5, 1, 66, 22, 11, 10]             #list initialization

    n1=Number(numbers)                          #object creation of Number and pssing the list as argument

    print("Numbers=",n1.get())                  #getting the numbers of list

    double=lambda x:x+x                         #lambda function for making double values in list
    print("New double values:",n1.change_original_values(func=double)) #calling function and passing above lamda function

    oddnum=lambda x:x%2==1                       #lambda function for filter out odd numbers in list
    print("Filtered odd values:",n1.filter_values(filter_func=oddnum)) #calling function and passing above lamda function

    comp=lambda a,b:a+b                         #lambda function for return compound value of list
    print("Compounded value:",n1.compound_the_numbers(reduce_func=comp))  #calling function and passing above lamda function

    print("Sorted list:",n1.sort())             #it calling the sort method to display sorted list