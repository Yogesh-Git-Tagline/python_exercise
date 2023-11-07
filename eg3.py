"""You are given a list of sentences. Create a word tree from each sentence and find how many times the word is appeared in other word trees."""
from collections import Counter   #including collections.Counter to count each word in list

#list created with sentences
sentences = ["My name is Ram", "He is a good person", "You should be careful while coding",
             "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen"]

split_sentences = []
for sentence in sentences:
    split_sentences.append(sentence.split())  #spliting each sentence of list

merge_items = []
for sentence in split_sentences:
        merge_items.extend(sentence)    #store the each item from splited list

print(split_sentences)      #printing the splited sentences with list

result=Counter(merge_items)        #collections.Counter to count each word from merge_item list
print("Number of time each word appears:")
print(result)   #finally we see the appearance of each word in senteces list in counter(key:value) format