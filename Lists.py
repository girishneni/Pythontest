
# coding: utf-8

# In[1]:

#lists
#creating a basic list
list=[1,2,3,4]
print(list)


# In[3]:

list2=["giri", "geetha", "nihal"]
print(list2)


# In[4]:

list= set(['a','b'])
print(list)


# In[5]:

print(len(list2))


# In[6]:

print(len(list))


# In[7]:

print(list2[1])


# In[10]:

print(list2[1:])


# In[13]:

list3=[1,'f','hi',7,'hjd',9,10]
print(list3)


# In[14]:

print(len(list3))


# In[15]:

list3[2:]


# In[16]:

print(list3)


# In[17]:

print(list3[3:])


# In[18]:

print(list3[:2])


# In[19]:

print(list3[2:4])


# In[20]:

#adding a new element into the list
list3= list3+[1991]


# In[21]:

print(list3)


# In[22]:

print(len(list3))


# In[23]:

print(list3*2)


# In[25]:

print(list3*4)


# In[35]:

list4=['a','c','b','d']
print(list4)


# In[39]:

list4.append(4)
print(list4)


# In[40]:

list4.pop(0)


# In[41]:

print(list4.pop(1))


# In[44]:

#built in functions
#reverse
print(list4.reverse())


# In[45]:

print(list4)


# In[47]:

print(list4.reverse())


# In[48]:

list4.reverse()


# In[49]:

print(list4)


# In[50]:

list4.reverse()
print(list4)


# In[52]:

myList=[10,40,586,27,4]
myList.sort()
print(myList)


# In[56]:

nestlist=[list2,myList]
print(nestlist)


# In[57]:

print(nestlist[0][0])


# In[59]:

print(nestlist[0])


# In[60]:

print(nestlist[1])


# In[62]:

print(nestlist[1][1])

print(nestlist)
# In[66]:

print(nestlist)


# In[68]:

nestlist=[list2,myList]


# In[69]:

print(nestlist)


# In[74]:

print(nestlist.count(1))


# In[75]:

list4=[1,2,3,4,5,67]
print(list4)


# In[79]:

print(list4.count(5))


# In[89]:

list4.append(8)


# In[90]:

print(list4)


# In[91]:

print(list4.count(8))


# In[92]:

#list.remove(inserted element)
print(list4.remove(8))


# In[93]:

print(list4)


# In[94]:

list4.remove(3)
print(list4)


# In[95]:

#to remove using the index use the del command
del list4[0]
print(list4)


# In[98]:

list4[1:4]=['a','b','c']
print(list4)


# In[101]:

#Buitlin functions
list6=[1,2,3,4,5,6,7,8,9,10]
print(max(list6))
print(min(list6))
print(sum(list6))


# In[ ]:



