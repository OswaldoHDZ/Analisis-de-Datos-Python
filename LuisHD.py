#!/usr/bin/env python
# coding: utf-8

# ### Salvando la discusión del Titanic

# In[10]:


import pandas as pd
import matplotlib

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Importación de datos

# In[37]:


data = pd.read_csv('datasets/titanic.csv')


# In[13]:


data.head(5)


# In[14]:


data = pd.read_csv('datasets/titanic.csv', usecols=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex','Age','Fare','Embarked'])


# In[15]:


data.head(5)


# In[16]:


data.tail(3)


# In[17]:


data.info()


# ### Limpieza de datos

# In[18]:


len(data)


# In[19]:


data.head(1)


# In[20]:


data['Name']


# In[21]:


type(data['Name'])


# In[22]:


data[['Name', 'Sex']]


# In[23]:


type(data[['Name', 'Sex']])


# In[24]:


data.loc[1]


# In[25]:


type(data.loc[1])


# In[26]:


data.loc[1].to_dict()


# In[38]:


data = data.dropna(subset=['Age', 'Embarked'])


# In[39]:


data.info()


# In[40]:


data['Fare'].max()


# In[42]:


data['Fare'].std()


# ## Análisis

# In[43]:


data['Age'].max()


# In[44]:


oldest_id = data['Age'].idxmax()


# In[45]:


oldest_id


# In[47]:


data.loc[630]


# In[48]:


data.loc[data['Age'].idxmax()]


# In[49]:


data.loc[data['Age'].idxmin()]


# In[51]:


data['Age'].mean()


# In[52]:


data['Fare'].sum()


# ### Encuentra a Jack y a Rose

# In[59]:


data['Sex'] == 'male'


# In[60]:


men = data[ data['Sex'] == 'male' ]


# In[62]:


men.head()


# In[64]:


women = data[ data['Sex'] == 'female' ]


# In[65]:


women.head()


# In[73]:


rose =  data[ data['Name'].str.contains('Rose', case=False) ]


# In[74]:


rose.head()


# In[75]:


data['Sex'].value_counts()


# In[76]:


data['Pclass'].value_counts()


# ### Gráficos

# In[78]:


data['Pclass'].value_counts().plot(kind='bar', color=['r', 'g','b'])


# In[87]:


survived = data[data['Survived'] == 1]['Sex'].value_counts()
dead = data[data['Survived'] == 0]['Sex'].value_counts()


# In[106]:


data[(data['Survived'] == 1) & (data['Age'] == 37)]


# In[88]:


survived


# In[90]:


dead


# In[91]:


survived_vs_dead = pd.DataFrame([survived, dead])


# In[92]:


survived_vs_dead


# In[95]:


survived_vs_dead.index = ['Survived', 'Dead']


# In[96]:


survived_vs_dead


# In[98]:


survived_vs_dead.plot(kind='bar', stacked=True)


# In[100]:


def show_survived_vs_dead(column):
    survived = data[data['Survived'] == 1][column].value_counts()
    dead = data[data['Survived'] == 0][column].value_counts()
    survived_vs_dead = pd.DataFrame([survived, dead])
    survived_vs_dead.index = ['Survived', 'Dead']
    survived_vs_dead.plot(kind='bar', stacked=True)
    


# In[104]:


show_survived_vs_dead('Sex')


# In[ ]:




