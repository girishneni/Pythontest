
# coding: utf-8

# In[1]:

#string with single quotes
s1='strings in python'
print(s1)


# In[3]:

#strings with double quotes
s2="This is the beginning"
print(s2)


# In[4]:

#multiple line strings
s3="""Hello welcome to the world of pyhton. 
phython is an simple language to learn.
it is an inpretation language"""
print(s3)


# In[5]:

#using the strings as arrays
var_teststring="strings in python"
print("print the first character:",var_teststring[0])


# In[6]:

print("printing the last character:",var_teststring[-1]) 


# In[7]:

#slicing
print(var_teststring[1:])


# In[9]:

print(var_teststring[0:7])


# In[13]:

print(var_teststring[-1:])


# In[15]:

print(var_teststring[1::2])


# In[16]:

#String Methods
print(var_teststring.upper())


# In[17]:

print(var_teststring.lower())


# In[18]:

print(var_teststring.capitalize())


# In[19]:

print(var_teststring.title())


# In[20]:

print(var_teststring.swapcase())


# In[21]:

#String Manipulations
print(' this is a test '.strip())


# In[24]:

print('this is a test'. strip('t') )


# In[25]:

print('this is a test'. strip('t'))


# In[27]:

print('test'.rstrip('t'))


# In[28]:

print('test'.lstrip('t'))


# In[30]:

print('test'.ljust(10,'t'))


# In[31]:

print('test'.rjust(10,'t'))


# In[34]:

print('test'.center(10,'s'))


# In[36]:

#find : printing the occurence of the index
print('test'.find('t'))


# In[37]:

print('girish'.find('i',2))


# In[38]:

print('girish'.find('t'))


# In[40]:

print('girishss'.rindex('s'))


# In[41]:

print("girishss".replace('s','i'))


# In[ ]:



