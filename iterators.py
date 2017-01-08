
# coding: utf-8

# In[20]:

#iterator
#keyword iter
#iteraction called by next()
i=0
x=[1,2,3,4]
for i in x:
    print(i)


# In[21]:

y=iter(x)
next(y)


# In[22]:

next(y)


# In[23]:

next(y)


# In[25]:

str=['abc','xyz','def']
my_str=iter(str)
next(my_str)


# In[26]:

next(my_str)


# In[27]:

next(my_str)


# In[28]:

next(my_str)


# In[29]:

iter(str)=[1,2,3,4]


# In[ ]:



