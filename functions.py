
# coding: utf-8

# In[3]:

#functions

# syntax: def nameOfFunction():
            #our logic




# In[5]:

#function with no input parameter and no return value
def say_hello():
    print('hello')


# In[6]:

say_hello()


# In[7]:

def func_noreturn():
    print("this function does not have a argument and a return value ")


# In[8]:

func_noreturn()


# In[12]:

#function with argument
def say_hello(name):
    print("Hello %s"% (name))


# In[13]:

say_hello("world")


# In[14]:

say_hello("girish")


# In[16]:

#Functions with input parameters and return values
def sum(n1,n2):
    return n1+n2


# In[17]:

sum(2,5)


# In[18]:

sum(78,90)


# In[19]:

sum('a','b')


# In[20]:

sum(('ab','ba'),(1,2,3,4))


# In[21]:

sum(-1,6)


# In[22]:

result=sum(20,40)
print("The sum of two no's is :", result)


# In[ ]:



