'''Create a list of 10 numbers and show the 5 different operations options to the user on screen. 
    The  5 different operations are as following,
 A. Length of the list
 B. Display first 3 numbers
 C. Display sum of odd numbers
 D. Number of duplicate numbers
 E. Display list without duplicate numbers'''


numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]  # given list

print("A. Length of the list")
print("B. Display first 3 numbers")
print("C. Display sum of odd numbers")
print("D. Number of duplicate numbers")
print("E. Display list without duplicate numbers")
choice = input("Select Your Choice(A/B/C/D/E):") # here user selects the choice(what he want to get


if (choice == 'A'):
    print(len(numbers))  # on choice-A,user will get length of numbers list

if (choice == 'B'):
    print(numbers[0:3])  # on choice-B user will get first 3 numbers

if (choice == 'C'):
    oddsum = [i for i in numbers if i % 2 == 1]
    print(sum(oddsum))  # on choice-C user will get sum of odd numbers

if (choice == 'D'):
    Items = []
    DuplicateItems = []

    for i in numbers:
        if i not in Items:
            Items.append(i)
        elif i not in DuplicateItems:
            DuplicateItems.append(i)
    print(DuplicateItems)  # on choice-D user will get number of duplicate numbers

if (choice == 'E'):
    Items = []
    for i in numbers:
        if i not in Items:
            Items.append(i)
    print(Items)  # on choice-E user can Display list without duplicate numbers
