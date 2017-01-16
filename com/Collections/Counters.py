from collections import Counter
#it is a dictionary sub class for counting hashable objects

#for lists

list1=['ab','bc','ab','bc','ab','bc',1,2,3,4,5]
print(Counter(list1))

list1.pop(0)
print(Counter(list1))

# Counter with strings

strCount = 'aabbbccccddddde'
print(Counter(strCount))

str1='hello this is giri'
print(Counter(str1.split()))

str2='hi welcome to python, python is an interpreted language.'
words=str2.split()
print(Counter(words).most_common())

sentence = 'How many times does each word show up in this sentence, word times each word each time'
words = sentence.split()
print('word counter:', Counter(words).most_common())


list2=[2,3,2,3,3,3,3,2,4,5,6,3]
c=Counter(list2)
print(c.elements())
