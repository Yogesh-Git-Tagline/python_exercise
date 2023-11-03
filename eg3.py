"""You are given a list of sentences. Create a word tree from each sentence and find how many times the word is appeared in other word trees."""

#list created with sentences
sentences = ["My name is Ram", "He is a good person", "You should be careful while coding",
             "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen"]


SplitSentences = []
for i in sentences:
    SplitSentences.append(i.split())  #spliting the word from each item of list

MergeItems = []
for i in SplitSentences:
    for element in i:
        MergeItems.append(element)    #store the each item from splited list

print(SplitSentences)      #printing the splited sentences with list

TempList = []           #temporary list for store items without duplicate items
for i in MergeItems:
    if i not in TempList:
        TempList.append(i) #remove the duplicate items using this loop and store the in another list

OccurenceItem = []      #OccurenceItem list for store the occurence of each item from TempList
for i in TempList:
    OccurenceItem.append(MergeItems.count(i))  #this process is for store the each item occurence in list

WordDict = dict(zip(TempList, OccurenceItem))  #it combining two list with help of zip() and convert them into dictionary

print("Number of time each word appears:")
print(WordDict)        #finally we see the appearance of each word in senteces list in dictionary(key:value) format
