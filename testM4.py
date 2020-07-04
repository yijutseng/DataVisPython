

# Load library for visualization
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# In[2]:


# Load library for data precessing
import pandas as pd  


# ## Set figure size

# In[3]:


plt.rcParams['figure.figsize'] = [15, 10]


df = pd.read_csv('Data/PRSA_Data_Shunyi_20130301-20170228.csv') 
df.head()




# In[6]:


# Remove NaN by .dropna()
sns.distplot(df['PM2.5'].dropna())
 

# In[7]:


sns.distplot(df['PM10'].dropna())
 



# In[8]:


# Parse String To DateTime
df['DateTime']=pd.to_datetime(df['year'].map(str) +
                              '/'+df['month'].map(str) +
                              '/'+df['day'].map(str) +
                              ' '+df['hour'].map(str)+':'+'00',
                              format='%Y/%m/%d %H:%M')
df[['year','month','day','hour','DateTime']]




# In[9]:

plt.close()
sns.lineplot(x=df['DateTime'], y=df['PM2.5'])
 





df2017=df.loc[((df['year']==2017) & (df['month']<=6))]
sns.lineplot(df2017['DateTime'], df2017['PM2.5'])
 



sns.lineplot(df2017['DateTime'], df2017['PM2.5'])
plt.axhline(y=df2017['PM2.5'].mean(skipna=True), 
            color='g', linestyle='-')
plt.axhline(y=df2017['PM2.5'].mean(skipna=True)+
            2*df2017['PM2.5'].std(), 
            color='y', linestyle=':')
plt.axhline(y=df2017['PM2.5'].mean(skipna=True)-
            2*df2017['PM2.5'].std(), 
            color='y', linestyle=':')
plt.axhline(y=df2017['PM2.5'].mean(skipna=True)+
            3*df2017['PM2.5'].std(), 
            color='r', linestyle=':')
plt.axhline(y=df2017['PM2.5'].mean(skipna=True)-
            3*df2017['PM2.5'].std(), 
            color='r', linestyle=':')
 




plt.close()
sns.scatterplot(df['PM2.5'],df['PM10'])
 



sns.regplot(df['PM2.5'],df['PM10'])
 



sns.pairplot(df2017)
 




wddf=df.groupby('wd').size().reset_index(name='size')
wddf





plt.pie(x=wddf['size'],labels=wddf['wd'])
 




sns.barplot(x=wddf['wd'],y=wddf['size'])
 


# In[18]:


wddf_sorted = wddf.sort_values('size')
sns.barplot(x=wddf_sorted['wd'],y=wddf_sorted['size'])
 


# In[19]:


wddf_sorted = wddf.sort_values('size', ascending=False)
sns.barplot(x=wddf_sorted['wd'],y=wddf_sorted['size'])
 



# In[20]:


df2017[['year','PM2.5']]


# In[21]:


sns.boxplot( x=df["year"], y=df["PM2.5"] )
 


# In[22]:


sns.scatterplot(df['PM2.5'],df['PM10'])
 



# In[24]:


sns.scatterplot(df['PM2.5'],df['PM10'],size=df['WSPM'])
 


# In[26]:


sns.scatterplot(df['PM2.5'],df['PM10'],size=df['WSPM'],sizes=(20, 200))
 



# In[65]:


df2017_wide=df2017[['DateTime','PM2.5','PM10','SO2','NO2']]
df2017_wide=df2017_wide.set_index('DateTime')
df2017_wide



# In[66]:


df2017_wide.mean()


# In[67]:


df2017_wide.std()


# In[68]:


nor_df2017_wide=(df2017_wide-df2017_wide.mean())/df2017_wide.std()
nor_df2017_wide



# In[79]:


nor_df2017_long=pd.melt(nor_df2017_wide.reset_index(),id_vars='DateTime')
nor_df2017_long


# In[74]:


sns.boxplot(x=nor_df2017_long["variable"], y=nor_df2017_long["value"])
 


# In[20]:


nor_df2017_wide = nor_df2017_wide.transpose()
nor_df2017_wide



# In[21]:


ax = sns.heatmap(nor_df2017_wide)
 



# In[22]:


import calmap
df2017_cal=df2017[['DateTime','PM2.5']]
df2017_cal


# In[23]:


df2017_cal=df2017_cal.resample('D', on='DateTime').mean()
df2017_cal


# In[24]:


calmap.yearplot(df2017_cal['PM2.5'], year=2017)
 


# In[25]:


import squarify 
df = pd.DataFrame({'nb_people':[8,3,4,2], 
                   'group':["group A", "group B", "group C", "group D"] })
df


# In[26]:


squarify.plot(sizes=df['nb_people'], 
              label=df['group'], alpha=.8 )
plt.axis('off')
 


# In[27]:


plt.plot([1,2,3])
 


# In[28]:


plt.plot([1,2,3],color="red")
 




# In[29]:


plt.plot([1,2,3],color="red")
 


# In[30]:


plt.plot([1,2,3],color="red", marker=11)
 


# In[31]:


plt.plot([1,2,3],color="red", marker=11)
 


# In[32]:


plt.plot([1,2,3],color="red", 
         marker=11, linestyle='dotted')
 




plt.plot([1,2,3],color="red", 
         marker=11, linestyle='dotted')
plt.xlabel('some x')
plt.ylabel('some y')
 




plt.plot([1,2,3],color="red", 
         marker=11, linestyle='dotted')
plt.xlabel('some x')
plt.ylabel('some y')
plt.title('some title')
 




plt.plot([1,2,3],color="red", 
         marker=11, linestyle='dotted')
plt.xlabel('some x')
plt.ylabel('some y')
plt.title('some title')
plt.savefig('saved_fig.png')




