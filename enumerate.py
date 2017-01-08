
# coding: utf-8

# In[2]:

#enumerate
list=[1,2,3,4,5,6,7]
for num,item in enumerate(list):
    print(num,item)
    


# In[8]:

#doubt
def enumerater(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n+=1

