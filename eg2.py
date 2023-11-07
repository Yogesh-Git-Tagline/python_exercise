
"""You are given a list of person names. Your task is to find out the three most frequent and three least frequent names."""

person_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']   #created list with person names  

print('Name List=',person_names)      #here we will see the list of persons 

length_of_items=[]     #created empty list for store the len of each element
item_frequency={}      #created for stor the item count with its length

for name in person_names:
    length_of_items.append(len(name))   #storing the length of each item in list

print("Name lengths:",length_of_items)

for item in length_of_items:
    item_frequency[item]=length_of_items.count(item)  #storing the item count with its length as key-value

def second_item(element): 
    return element[1]       #it returning sencond item i.e name count to sort frequent names

most_frequent_lengths=sorted(item_frequency.items(), key=second_item, reverse=True)[:3] #it sorting each item frequency based on value in reverse order

least_frequent_lengths=sorted(item_frequency.items(), key=second_item)[:3]  #it sorting each item frequency based on value 

most_frequent_names={}
least_frequent_names={}

#below loops are assigning th list of names as value with key of their length
for item in  most_frequent_lengths:
    most_frequent_names[item[0]]=[name for name in person_names if(len(name)==item[0])]

for item in  least_frequent_lengths:
    least_frequent_names[item[0]]=[name for name in person_names if(len(name)==item[0])]

#finally it shows three most and least frequent name in list format
print("The three most frequent name lengths are:")
for length, names in most_frequent_names.items():
    print(len(names),"names of length",length,":",names)

print("The three least frequent name lengths are:")
for length, names in least_frequent_names.items():
    print(len(names),"names of length",length,":",names)
