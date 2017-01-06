
# coding: utf-8

# In[6]:

#control statements
#if-else and if-elif statements
if(True):
    print("true")
else:
    print("false")


# In[8]:

if(False):
    print("true")
else:
    print("false")


# In[10]:

a=100
b=200
c=300

if(a==b):
    print("both are equal")
else:
    print("both are unequal")


# In[12]:

if(a<b):
    print("b is greater")
else:
    print("a is greater")


# In[13]:

if(c>a):
    print("c is greater")
else:
    print("a is greater")


# In[16]:

def validate(value):
    if(value=='abc'):
        print("it is abc")
    else:
        print("error")
    


# In[17]:

validate("abc")


# In[18]:

validate("bca")


# In[19]:

#if-elif statment
print(a,b,c)


# In[20]:

if(a>b):
    print("a is greater")
elif(b>c):
    print("b is greater")
else:
    print("c is greater")


# In[36]:

def greater(a1,b1,c1):
     if(a1>b1):
        print("a1 is greater")
        elif(b1>c1):
            print("b1 is greater")
        else:
            print("c1 is greater")


# In[45]:

def greater(a1,b1,c1):
    if(a1>b1):
        print("a1 is greater:",a1)
    elif(b1>c1):
        print("b1 is greater:",b1)
    else:
        print("c1 is greater:",c1)


# In[44]:

greater(20,60,10)


# In[46]:

greater(20,30,70)


# In[47]:

greater(10,10,10)


# In[48]:

greater(20,20,20)


# In[49]:

def greater(a1,b1,c1):
    if(a1>b1):
        print("a1 is greater:",a1)
    elif(b1>c1):
        print("b1 is greater:",b1)
    elif(c1>a1):
        print("c1 is greater:",c1)
    else:
        print("all no's are equal")


# In[50]:

greater(10,20,30)


# In[51]:

greater(10,10,10)


# In[52]:

greater(45,80,15)


# In[ ]:



