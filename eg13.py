"""Create a class name Number with the following methods."""


# importing reduce from functool to work with reduce module
from functools import reduce

# class creation
class Number:
    def __init__(self, numbers):  # constructor for assign number list in number variable
        self.numbers = numbers

    def get(self):  # get method is returning list of numbers
        return self.numbers

    # this method gives function from argument to work with map method
    def change_original_values(self, function):
        # map method is changing all values and we convert those values them into list
        map_values = list(map(function, self.numbers))
        return map_values  # returning the list of changed values

    # this method gives function from argument to work with filter method
    def filter_values(self, filter_function):
        # filter method is filters values and we convert those values in list
        filtered_values = list(filter(filter_function, self.numbers))
        return filtered_values  # returning the list of filtred values

    # this method gives function from argument to work with reduce method
    def compound_the_numbers(self, reduce_function):
        # reduce method will gives single value
        reduce_values = reduce(reduce_function, self.numbers)
        return reduce_values  # returning that single value

    def sort_numbers(self):  # this function is for only sort the list of number
        return sorted(self.numbers)


if __name__ == "__main__":  # this checking the current module is __main__ or not

    numbers = [2, 5, 1, 66, 22, 11, 10]  # list initialization

    # object creation of Number and pssing the list as argument
    num = Number(numbers)

    print("Numbers=", num.get())  # getting the numbers of list

    # lambda function for making double values in list
    def make_double(x): return x+x
    # calling function and passing above lamda function
    print("New double values:", num.change_original_values(function=make_double))

    # lambda function for filter out odd numbers in list
    def odd_number(x): return x % 2 == 1
    # calling function and passing above lamda function
    print("Filtered odd values:", num.filter_values(filter_function=odd_number))

    # lambda function for return compound value of list
    def compound_number(a, b): return a+b
    # calling function and passing above lamda function
    print("Compounded value:", num.compound_the_numbers(reduce_function=compound_number))

    # it calling the sort method to display sorted list
    print("Sorted list:", num.sort_numbers())
