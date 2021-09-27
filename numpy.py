#!/usr/bin/env python
# coding: utf-8

# **welcome to numpy**
# 

# In[1]:


import numpy as np


# In[2]:


myarr=np.array([[1,2,3,4]],np.int8)


# In[3]:


myarr[0,1]


# In[ ]:





# In[4]:


myarr[0,1]=45


# In[5]:


myarr


# In[6]:


myarr.dtype


# #more array creation methods:in numpy

# In[7]:


listarray=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[8]:


listarray


# In[9]:


listarray[1,3]


# In[10]:


listarray.dtype


# In[11]:


listarray.shape


# In[12]:


listarray.size


# In[13]:


#intrinsic property of array creation in numpy


# In[14]:


zeroes=np.zeros((2,2),np.int32)


# In[15]:


zeroes


# In[16]:


zeroes.shape


# In[17]:


zeroes.dtype


# In[18]:


rng=np.arange(15)


# In[19]:


rng


# In[20]:


lspace=np.linspace(1,50,4)


# In[21]:


lspace


# In[22]:


arr_1=np.empty((2,2))


# In[23]:


print(arr_1)


# In[24]:


ide=np.identity(2)


# In[25]:


ide


# In[26]:


ide.dtype


# In[27]:


ide.shape


# In[28]:


arr_2=np.arange(75)


# In[29]:


arr_2


# In[30]:


arr=arr_2.reshape(3,25)


# In[31]:


arr


# In[32]:


arr_3=arr.ravel()


# In[33]:


arr_3.shape


# In[34]:


arr_3


# In[35]:


arr_2


# In[36]:


arr


# In[37]:


x=[[1,2,3],[4,5,6],[7,1,0]]


# In[38]:


myarr_2=np.array(x)


# In[39]:


myarr_2


# #axis 0 be taken as the row axis

# In[40]:


arr_2.sum(axis=0)


# In[41]:


arr_2


# In[42]:


myarr_2


# In[43]:


myarr_2.sum(axis=0)


# In[44]:


sum=myarr_2.sum(axis=0)


# In[45]:


sum


# In[46]:


sum_1=myarr_2.sum(axis=1)


# In[47]:


sum_1


# **T attributes is used to transpose a given matrix

# In[48]:


sum_1.T


# In[49]:


myarr_2.T


# In[50]:


for item in arr_2:
    print(item)


# In[51]:


for item in myarr_2:
    print(item)


# In[52]:


for item in myarr_2.flat:
    print(item)


# In[53]:


myarr_2.ndim


# In[54]:


myarr_2.size


# In[55]:


myarr_2.shape


# In[56]:


myarr_2.nbytes


# In[57]:


myarr_4=np.array([1,2,3,655,7777])


# In[58]:


myarr_4.argmax()


# In[59]:


myarr_4.argmin()


# argmax() and argmin() are used to return the maximum and minimum element indices

# argsort() is used to sort the array

# In[60]:


myarr_4


# In[61]:


myarr_4.ndim


# In[62]:


myarr_4[3]=-1


# In[63]:


myarr_4


# In[64]:


myarr_4[0]


# In[65]:


myarr_2.argmin()


# In[66]:


myarr_2.argmax()


# In[67]:


myarr_2.argsort()


# In[68]:


myarr_2.argmax(axis=0)


# In[69]:


myarr_2


# In[70]:


myarr_2.argmin(axis=0)


# In[71]:


myarr_2.argmin(axis=1)


# In[72]:


myarr_2.argmax(axis=1)


# In[73]:


arr_3=myarr_2.ravel()


# In[74]:


arr_3


# In[75]:


arr_3.reshape((9))


# #performing arithematic operations in numpy

# In[76]:


arr_2


# In[77]:


myarr_2


# In[78]:


arr_3


# In[79]:


arr_4=np.array([[1,2,3],[6,7,8],[9,10,11]])


# In[80]:


arr_4


# In[81]:


myarr_2+arr_4


# In[82]:


myarr_2*arr_4


# In[83]:


np.sqrt(myarr_2)


# In[84]:


np.sqrt(arr_4)


# In[85]:


myarr_2.sum()


# In[86]:


myarr_2.sum(axis=0)


# In[87]:


myarr_2.sum(axis=1)


# In[88]:


myarr_2.max()


# In[89]:


myarr_2.min()


# #counting the non zero digits we use count_nozero() method

# In[90]:


np.count_nonzero(myarr_2)


# In[91]:


myarr_2.nbytes


# In[92]:


myarr_2.dtype


# In[93]:


import sys


# In[94]:


py_ar=[1,2,3,4]


# In[95]:


np_ar=np.array(py_ar)


# In[96]:


np_ar


# In[97]:


sys.getsizeof(py_ar)*len(py_ar)


# In[98]:


np_ar.itemsize*np_ar.size


# In[ ]:





# In[ ]:




