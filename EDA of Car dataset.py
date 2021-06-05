#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


A = pd.read_csv("/users/ranjeetgaikwad/desktop/data science class/Cars93.csv")


# In[4]:


A.head()


# In[68]:


A.info()


# # Exploratory Data Analysis(EDA)

# In[11]:


#Univariate Analysis

cat = []
con = []
for i in A.columns:
    if(A[i].dtypes == "object"):
        cat.append(i)
    else:
        con.append(i)


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sb


# In[14]:


for i in A.columns:
    if(A[i].dtypes == "object"):
        sb.boxplot(A[i],A.Price) #Boxplot between categorical and continuous columns
        plt.xlabel(i)
        plt.ylabel('Price')
        plt.show()
    else:
        plt.scatter(A[i],A.Price) #Scatter plot between continuous and continuous columns
        plt.xlabel('Price')
        plt.ylabel(i)
        plt.show()


# In[15]:


cat


# In[16]:


con


# In[21]:


import seaborn as sb
import matplotlib.pyplot as plt


# In[29]:


for i in con:
    sb.distplot(A[i])
    plt.show()


# In[33]:


plt.figure(figsize=(40,19))
plt.subplot(3,3,1)
sb.distplot(A[['MPG.highway']])
plt.subplot(3,3,2)
sb.distplot(A.EngineSize)
plt.subplot(3,3,3)
sb.distplot(A.Horsepower)
plt.subplot(3,3,4)
sb.distplot(A[['Fuel.tank.capacity']])
plt.subplot(3,3,5)
sb.distplot(A.Weight)


# In[34]:


A['Price'].hist()


# In[37]:


sb.countplot(A.AirBags)


# In[39]:


sb.countplot(A.Cylinders)


# In[41]:


A["Type"].value_counts()


# In[42]:


A["Type"].value_counts().plot(kind = "barh")


# In[43]:


A["Type"].value_counts().plot(kind = "bar")


# In[44]:


A["Type"].value_counts().plot(kind = "pie")


# In[73]:


# Bivariate
#con vs con

plt.scatter(A.Price, A.EngineSize, c = "black")
plt.xticks(range(0, 80, 5))
plt.yticks(range(0, 6, 1))
plt.xlabel("Price")
plt.ylabel("EngineSize")
plt.title("Price avs Engine Scatterplot")


# In[72]:


plt.scatter(A.Price, A.Horsepower, c = "red")


# In[75]:


# cat vs con

sb.boxplot(A.Cylinders, A.Price)


# In[81]:


#cat vs cat 

pd.crosstab(A.Model, A.Type)


# In[82]:


#Multivariate Analysis

sb.pairplot(A)


# # Missing value Treatment 

# In[83]:


A.isna().sum()


# In[84]:


B = pd.DataFrame(A.isna().sum(), columns=["missing_values"])


# In[86]:


B[B.missing_values>0]


# In[88]:


#function of fill the missing values

def replacer(df):
    Q = pd.DataFrame(df.isna().sum())
    Q.columns = ["CT"]
    w = list(Q[Q.CT>0].index)     #list of colummns with missing values
    
    cat = []                      #distinguishing between in categorical and continuous  
    con = []
    for i in w:
        if(df[i].dtypes == "object"):
            cat.append(i)
        else:
            con.append(i)
            
    for i in con:                 #filling in the missing values
        replacer = df[i].mean()
        df[i] = df[i].fillna(replacer)
        
    for i in cat:
        replacer = pd.DataFrame(df[i].value_counts()).index[0]
        df[i] = df[i].fillna(replacer)


# In[89]:


replacer(A)


# In[91]:


B = pd.DataFrame(A.isna().sum(), columns = ["check"]) 


# In[92]:


B


# In[93]:


sb.pairplot(A)


# In[94]:


A.isna().sum()


# In[ ]:




