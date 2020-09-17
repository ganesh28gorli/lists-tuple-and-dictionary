#!/usr/bin/env python
# coding: utf-8

# #write a code snippets in phyton to perferm the following 
# 1.assigning elements to different lists
# 2.accessing elements from a tuple
# 3.deleting different dictionary elements

# In[1]:


#assiging elements to different lists


# In[2]:


thislist = ["apple","banana","mango","cherry" ]


# In[3]:


#we can also create lists using list() method:
animals = list(("lion","tiger","goat","sheep","elephant"))


# In[4]:


#append() method ois used to add items 
thislist.append("orange")
print(thislist)


# In[5]:


#insert() method is used to add an item at specified index
animals.insert(2,"horse")
print(animals)


# In[7]:


# to change a item value(replacing)
animals[1] = "dog"
print(animals)


# In[8]:


#accessing elements from a tuple


# In[9]:


thistuple=("red","yellow","white","black","blue")


# In[15]:


# to access a elements from a tuple of specific index
print(thistuple[1])
print(thislist[-2])


# In[12]:


# accessing elements from 1 index to another index
print(thistuple[1:4])


# In[13]:


#accessing using loop
for x in thistuple:
    print(x)


# In[16]:


#deleting different dictionary elements


# In[21]:


dict={"brand":"ford",
      "model":"mustag",
      "year":1964 
     }


# In[23]:


print(dict)


# In[24]:


#pop() method removes the item eith specific key name
dict.pop("model")
print(dict)


# In[25]:


#del key word removes the item with specific key name
del dict["brand"]
print(dict)

