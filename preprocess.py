
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('obvious.csv')


# In[3]:


df['text'][0]


# In[4]:


import re
remove_hashtags = re.compile(r'#\w+\s?')
remove_friendtag = re.compile(r'@\w+\s?')


# In[28]:


data=[]
length=[]
#df['tweet'] = df['text']
for txt in df['text']:
    txt = remove_hashtags.sub('',txt)
    
    if 'http:' not in txt and txt[:2]!='RT' and '\u' not in txt:
        txt = remove_friendtag.sub('',txt)
        txt = ' '.join(txt.split())
        if len(txt.split())>1:
            data.append(txt)
            length.append(len(txt.split()))
            


# In[29]:


df['tweet'] = pd.Series(data)


# In[30]:


df['tweet'].to_csv('procpos.csv',index_label=False)

