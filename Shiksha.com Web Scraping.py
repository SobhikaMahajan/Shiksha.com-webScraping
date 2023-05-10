#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import html.parser


# In[2]:


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}


# In[3]:


webpage=requests.get('https://www.shiksha.com/mba/colleges/mba-colleges-india', headers=headers).text


# In[4]:


soup =BeautifulSoup(webpage,'lxml')


# In[5]:


print(soup.prettify())


# In[6]:


scraped_clg=soup.find_all('div',class_="c8ff")
scraped_clg


# In[7]:


clgs=[]
for clg in scraped_clg:
    clg=clg.get_text().replace('\n'," ")
    clg.strip(" ")
    clgs.append(clg)
clgs


# In[8]:


scraped_loc=soup.find_all('span',class_="_5588")
scraped_loc


# In[9]:


locs=[]
for loc in scraped_loc:
    loc=loc.get_text().replace('\n'," ")
    loc.strip(" ")
    locs.append(loc)
locs


# In[10]:


scraped_ratings=soup.find_all('a',class_="_68c4")
scraped_ratings


# In[11]:


rate=[]
for ra in scraped_ratings:
    ra=ra.get_text().replace('\n'," ")
    ra.strip(" ")
    rate.append(ra)
rate


# In[12]:


scraped_exam=soup.find_all('ul',class_="_0954")
scraped_exam


# In[13]:


exam=[]
for ex in scraped_exam:
    ex=ex.get_text().replace('\n'," ")
    ex.strip(" ")
    exam.append(ex)
exam


# In[14]:


data=pd.DataFrame()
data['College Name']=clgs
data['Location']=locs
data['Ratings']=rate
data['Exam']=exam
data


# In[15]:


data.to_csv('Shiksha.com.csv')


# In[ ]:




