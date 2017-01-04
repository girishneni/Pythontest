
# coding: utf-8

# In[1]:

#dictionaries
dict1={"key1":"value1","key2":"value2","key3":"value3"}


# In[2]:

print(dict1)


# In[4]:

list(dict1.keys())


# In[5]:

list(dict1.values())


# In[6]:

my_map={"a1":123,"a2":['a','b','c'], "a3":{1,2,4,5},"a4":'abcd'}
print(my_map)


# In[10]:

list(my_map.keys())


# In[11]:

sorted(my_map.keys())


# In[13]:

print(my_map['a2'])


# In[15]:

print(my_map['a2'][0])


# In[16]:

print(my_map['a2'][0].isupper())


# In[17]:

print(my_map['a2'][0].islower())


# In[18]:

print(my_map['a2'][0].upper())


# In[19]:

print(my_map)


# In[23]:

print(my_map['a3'])


# In[24]:

print(my_map['a4'])


# In[27]:

print(my_map['a4'][1:])


# In[28]:

print(my_map['a4'][0:1])


# In[38]:

print(my_map['a4'])


# In[39]:

#nested dictionaries
my_nest={'key1':{'nestkey1':'1234', 'nestkey2':'abcd'},'key2':[1,'s','a',2]}


# In[40]:

print(my_nest)


# In[42]:

my_nest['key1']


# In[45]:

my_nest['key1']['nestkey1']


# In[46]:

my_nest['key1']['nestkey1'][3]


# In[48]:

my_nest['key1']['nestkey1'][4]


# In[49]:

my_nest['key1']['nestkey1'][:2]


# In[50]:

my_nest['key1']['nestkey1'][1::2]


# In[52]:

print(my_nest.items())


# In[54]:

print(my_nest.keys())


# In[55]:

list(my_nest.keys())


# In[ ]:



