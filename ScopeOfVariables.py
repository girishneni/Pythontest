
# coding: utf-8

# In[3]:

#Scope of global variable
def f():
    s='i love SFO'
    print(s)
    s='i love NY in summer'
f();


# In[6]:

def f():
   
    s='i love SFO'
    print(s)
s='i love NY in summer'
f();
print(s)


# In[9]:

def f():
    print(s)
    s='i love SFO'
    print(s)
s='i love NY in summer'
f();


# In[10]:

def f():
    global s
    print(s)
    s='i love SFO'
    print(s)
s='i love NY in summer'
f();



# In[11]:

def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)

a,b,x,y = 1,15,3,4
foo(17,4)
print(a,b,x,y)


# In[ ]:



