
# coding: utf-8

# In[2]:

#inheritance
class Animal:
    
    def __init__(self):
        print('animal created')
    
    def whoAmI(self):
        print('Animal')
    
    def eat(self):
        print('eating')


# In[3]:

d=Animal()


# In[4]:

d.whoAmI()


# In[6]:

d.eat()


# In[7]:

class Dog(Animal):
    def __init__(self):
        print('Dog created')
    
    def whoAmI(self):
        print('Dog')
    
    def bark(self):
        print('woof')


# In[23]:

class Cat(Animal):
    def __init__(self):
        print('Cat created')
    
    def whoAmI(self):
        print('Cat')
    
    def bark(self):
        print('Meaww')
        
    def diff(self):
        print('I am different')
    
    


# In[9]:

c=Cat()


# In[10]:

c.bark()


# In[11]:

c.eat()


# In[12]:

d=Dog()


# In[13]:

d.eat()


# In[14]:

d.bark()


# In[16]:

c.bark()


# In[26]:

class Multipleinherit(Dog,Cat):
    pass
    


# In[27]:

m=Multipleinherit()


# In[28]:

m.bark()


# In[29]:

m.diff()

