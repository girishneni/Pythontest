
# coding: utf-8

# In[1]:

#classes
#objects:attribute reference and instantiation

class MyClass:
    i=12345
    
    def f(self):
        return "HELLO Welcome to python"
    


# In[30]:

x=MyClass()
print(x.f())


# In[31]:

class Complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
        


# In[32]:

x= Complex(1,-1.5)
x.real,x.image


# In[34]:

class Dog:
    def __init__(self,breed):
        self.breed=breed
    
sam=Dog(breed='Lab')
frank=Dog(breed='Pugg')



# In[35]:

sam.breed


# In[36]:

frank.breed


# In[23]:

class Dog():
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed = 'Lab')
frank = Dog(breed = 'Huskie')


# In[37]:

frank.breed


# In[24]:

sam.breed


# In[38]:

class Dog:
    
    species='mammal'
    
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
        


# In[39]:

sam= Dog('lab','sam')
frank=Dog('Pugg','frank')
bill=Dog('Huskie','bill')


# In[40]:

sam.breed


# In[41]:

sam.name
frank.breed


# In[42]:

frank.name


# In[43]:

bill.breed


# In[59]:

class Circle(object):
    pi=3.14
    
    def __init__(self,radius=1):
        self.radius=radius
    
    def area(self):
        return self.radius*self.radius*Circle.pi
        
    def setRadius(self,radius):
        self.radius=radius
        
    def getRadius(self):
        return self.radius
        


# In[60]:

c=Circle()
c.setRadius(2)
c.getRadius()
print(c.area())


# In[61]:

c = Circle()
c.setRadius(2)
print('Radius is: ', c.getRadius())
print('Area is: :', c.area())


# In[62]:

print(c.area())


# In[65]:

c.setRadius(3)
print("radius:",c.getRadius(),"area:",c.area())


# In[ ]:



