#!/usr/bin/env python
# coding: utf-8

# # hello, my name is Mohamed Sobhi. I'm student in faculty of navigation science and space technology in Bin Seuf university.
# 
# ## this is my first program in my course (space science applications with python) 
# 
# ### my program is how to calculate position and velocity of Earth and calculate the distance between the earth and the sun.
# 

# In[1]:


# Import the libraries
import spiceypy
import datetime
import math


# In[2]:


#get today's date
Date_today = datetime.datetime.today()


# In[3]:


Date_today


# In[4]:


type(Date_today)


# In[5]:


DATE_TODAY = Date_today.strftime('%Y-%m-%dT00:00:00')


# In[6]:


type(DATE_TODAY)


# In[7]:


#We need to load it first
spiceypy.furnsh('naif0012.tls')


# In[8]:


# convert the utc string to the corresponding ET
ET = spiceypy.utc2et(DATE_TODAY)


# In[9]:


type(ET)


# In[10]:


ET


# In[11]:


#We need to load it first
spiceypy.furnsh('de432s.bsp')


# In[12]:


# Now compute  the position and velocity
# The first 3 values are the x, y, z components in km. The last 3 values are the corresponding velocity components in km/s.

Earth_State_Sun, Earth_Sun_Light_Time = spiceypy.spkgeo(targ=399, et=ET, 
                                                            ref='ECLIPJ2000', obs=10)


# In[13]:


print(Earth_State_Sun)


# In[14]:


print(Earth_Sun_Light_Time)


# In[15]:


Earth_Sun_Dinstance = math.sqrt(Earth_State_Sun[0]**2.0                              + Earth_State_Sun[1]**2.0                              + Earth_State_Sun[2]**2.0)


# In[16]:


Earth_Sun_Dinstance_AU = spiceypy.convrt(Earth_Sun_Dinstance, 'km', 'AU')


print('Current distance between the Earth and the Sun in AU:', Earth_Sun_Dinstance_AU)


# In[17]:



velocity = math.sqrt(Earth_State_Sun[3]**2.0                                   + Earth_State_Sun[4]**2.0                                   + Earth_State_Sun[5]**2.0)


print('Current orbital speed of the Earth around the Sun in km/s:', velocity)


# In[18]:


spiceypy.furnsh('gm_de431.tpc')
_, GM_SUN = spiceypy.bodvcd(bodyid=10, item='GM', maxn=1)


V_Func = lambda gm, r: math.sqrt(gm/r)
velocity_Theory = V_Func(GM_SUN[0], Earth_Sun_Dinstance)


print('Theoretical orbital speed of the Earth around the Sun in km/s:', velocity_Theory)


# In[ ]:




