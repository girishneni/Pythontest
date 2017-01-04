
# coding: utf-8

# In[5]:

#sets basics

a=set()
print(a)


# In[6]:

a.add(1,1,1)


# In[7]:

a.add(1)
a.add(2)
a.add(-1)
a.add(-2)
print(a)


# In[8]:

a.add(-1)
a.add(-1)
print(a)


# In[10]:

a.add('a')
a.add('b')
print(a)


# In[14]:

a1=set({'a','b'})
print(a1)


# In[15]:

a1.add('c')
a1.add('d')
print(a1)


# In[16]:

print("a set:",a)
print("a1 set:", a1)


# In[17]:

a1.add(1)

a1.add(-2)


# In[18]:

print("a set:",a)
print("a1 set:", a1)


# In[19]:

#set operations

#copy

a2=a.copy()
print(a2)


# In[21]:

a3=a1.copy()
print(a3)


# In[22]:

#clear
a3.clear()
print(a3)


# In[24]:

a3=set({1,-6,'r','h'})
print(a3)


# In[25]:

a3.clear()
print(a3)


# In[29]:

#differnce
print(a)
print(a1)


# In[32]:

a.difference(a1)
print(a)


# In[33]:

x=set({1,2,3,4})
y=x.copy()


# In[34]:

x.difference(y)
print(x)


# In[35]:

y.add(5)
y.add(6)


# In[36]:

x.difference(y)


# In[37]:

print(x)


# In[38]:

print(y)


# In[39]:

x.difference(y)


# In[40]:

y.remove(5)


# In[41]:

y.remove(6)


# In[42]:

print(y)


# In[44]:

x.difference(y)


# In[45]:

y.add(5)
y.add(6)
y.add(-1)
y.add(-4)


# In[50]:

print(y.difference_update(x))


# In[51]:

set1={1,2,3}
set2={1,4,5}
print(set1)
print(set2)


# In[53]:

print(set1.difference(set2))


# In[54]:

print(a)
print(a1)


# In[55]:

print(a.difference(a1))


# In[56]:

print(set1.difference_update(set2))


# In[57]:

print(a.difference_update(a1))


# In[58]:

print(a1.difference_update(a))


# In[59]:

#discard

a1.discard(1)
print(a1)


# In[60]:

a.discard(2)
print(a)


# In[62]:

a.add(2)
a.add('a')
a.add('c')
a.add(3)
print(a)
print(a1)


# In[63]:

#union of sets
print(a.union(a1))


# In[65]:

print(a1.union(a))


# In[64]:

#intersection

print(a.intersection(a1))


# In[66]:

print(a1.intersection(a))


# In[68]:

#Symmetric difference

print(a.symmetric_difference(a1))


# In[69]:

print(a1.symmetric_difference(a))


# In[76]:

#update
a1.update(a)
print(a1)


# In[72]:


set2


# In[73]:

set1


# In[75]:

set1.update(set2)
print(set1)


# In[77]:

#subset

a.issubset(a1)


# In[79]:

a1.issubset(a)


# In[81]:

#superset
a1.issuperset(a)


# In[82]:

a.issuperset(a1)


# In[84]:

#Boolean
#contains only true or false Or 1 or 0

1>2


# In[85]:

2>1


# In[86]:

0>0


# In[87]:

0==0


# In[88]:

1<10


# In[90]:

'a'>'b'


# In[91]:

'z'>'b'


# In[ ]:



