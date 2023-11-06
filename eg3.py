"""You are given a list of sentences. Create a word tree from each sentence and find how many times the word is appeared in other word trees."""

#list created with sentences
sentences = ["My name is Ram", "He is a good person", "You should be careful while coding",
             "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen"]


split_sentences = []
for sentence in sentences:
    split_sentences.append(sentence.split())  #spliting each sentence of list

merge_items = []
for sentence in split_sentences:
    for element in sentence:
        merge_items.append(element)    #store the each item from splited list

print(split_sentences)      #printing the splited sentences with list

items = []           #item list for store items without duplicate items
for item in merge_items:
    if item not in items:
        items.append(item) #remove the duplicate items using this loop and store the in another list

item_occurence = []      #item_occurence list for store the occurence of each item from TempList
for item in items:
    item_occurence.append(merge_items.count(item))  #this process is for store the each item occurence in list

result = dict(zip(items, item_occurence))  #it combining two list with help of zip() and convert them into dictionary

print("Number of time each word appears:")
print(result)    #finally we see the appearance of each word in senteces list in dictionary(key:value) format
