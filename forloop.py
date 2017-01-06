
# coding: utf-8

# In[1]:

#for loop

list=[1,2,3,4,5]

for i in list:
    print(i)


# In[3]:

list1=['a','b','c','d','e']
for i in list1:
    print(i)


# In[10]:

list=[1,2,3,4,5]
list_sum=0
for i in list:
    list_sum+= i
    print(list_sum)


# In[13]:

list2 = [[2,4], (6,8)]
for i in list:
    print(i)


# In[21]:

dict = {'k':'va11', 'k2':'val2'}
for item in dict:
    print(dict.items())


# In[22]:

#looping 5 times:
for c in range(5):
    print("loop:",c)


# In[24]:

#looping over no of character's in a string
for char in "mystring":
    print(char)


# In[27]:

for element_index in range(len(list)):
    print(list[element_index])


# In[28]:

#looping for a subset of list of elements
for element in list[2:4]:
    print(list[element])


# In[31]:

# Nested Loops, loop inside loop
for outer_loop in range(5):
    for inner_loop in range(5):
         print('outer_loop-inner_loop', outer_loop, '-', inner_loop)
 		# Prints all the elements in new line
 


# In[32]:

for outerLoop in range(5):
    for innerLoop in range(3):
        print("outerLoop",outerLoop,"- innerloop",innerLoop)


# In[ ]:



