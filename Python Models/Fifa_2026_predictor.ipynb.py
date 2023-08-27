#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


player_data = pd.read_csv('FIFA22_official_player_data.csv')
player_data.head()


# In[3]:


player_data.info()
print(player_data.shape)


# In[4]:


team_data = pd.read_csv('FIFA - 2022.csv')
team_data.head()


# In[5]:


team_data.info()
print(team_data.shape)


# In[6]:


player_data['Nationality'].unique()


# In[7]:


l1 = team_data['Team'].tolist()
len(l1)


# In[8]:


player_data = player_data.replace('United States','USA')
player_data = player_data.replace('Korea Republic','South Korea')


# In[9]:


player_data['Nationality'].unique()


# In[10]:


player_data_1 = player_data[player_data['Nationality'].isin(l1)]


# In[11]:


player_data_1['Nationality'].unique()


# In[12]:


l1


# In[13]:


l2 = player_data_1['Nationality'].tolist()
l2


# In[14]:


team_data['Team'].nunique()


# In[15]:


player_data_1['Nationality'].nunique()


# In[16]:


for i in l1:
    if i not in l2:
        print(i)


# In[17]:


team_data[team_data['Team'] == 'USA']


# In[18]:


player_data[player_data['Nationality'] == 'South Korea']


# In[19]:


Team_Score = pd.DataFrame(columns=['Team_Name','Win_Loss_perc','Player_Score','Net_Score'])


# In[20]:


def Win_Loss_perc(team):
    data = team_data[team_data['Team'] == team]
    score = data['Win']*3 +data['Draw']*1
    score = score /(data['Games Played']*3)
    score = score * 50
    return score.iloc[0]


# In[21]:


def Player_Score(team):
    data = player_data_1[player_data_1['Nationality']==team]
    data = data.loc[:,'Crossing':'DefensiveAwareness'].select_dtypes(exclude = 'object')
    score = 0
    for index, row in data.iterrows():
        player_score = row.sum()
        score = score + (player_score/3400)
    score = score / data.shape[0]
    return round(score * 50,2)


# In[22]:


for index ,row in team_data.iterrows():
    wl = Win_Loss_perc(row['Team'])
    ps = Player_Score(row['Team'])
    net_score = (wl + ps)
    new_entry = {'Team_Name':row['Team'],'Win_Loss_perc':wl,'Player_Score':ps,'Net_Score':net_score}
    Team_Score.loc[index] = new_entry
Team_Score


# In[23]:


df = Team_Score.head(5)


# In[30]:


plt.bar(df['Team_Name'],df['Net_Score'],width=0.2,color='cyan',label = 'Total Team Score (max : 100)')
plt.bar(df['Team_Name'],df['Player_Score'],width=0.2,color='brown',label = 'All Team Player Stats basisScore (max : 50)')
plt.bar(df['Team_Name'],df['Win_Loss_perc'],width=0.2,color='red',label = 'Team Win,Loss and Draw Score (max : 50)')
plt.legend()
plt.xlabel('Teams')
plt.ylabel('Scores')
plt.title('Score ranking of Team on the basis of Player Stats and Teams Win-Loss Ratio')
plt.plot


# In[63]:


plt.style.use('ggplot')


x = range(len(df['Team_Name']))

plt.figure(figsize = (20,12))
plt.bar(x, df['Net_Score'], width=0.2, color='cyan', align='center', label='Total Team Score (max : 100)')
plt.bar([i + 0.2 for i in x], df['Player_Score'], width=0.2, color='brown', align='center', label='All Team Player Stats basis Score (max : 50)')
plt.bar([i + 0.4 for i in x], df['Win_Loss_perc'], width=0.2, color='red', align='center', label='Team Win, Loss, and Draw Score (max : 50)')

plt.xlabel('Teams',fontsize=40)
plt.ylabel('Scores',fontsize=40)
plt.title('Score ranking of Team on the basis of Player Stats and Teams Win-Loss Ratio',fontsize=40)
plt.xticks([i + 0.2 for i in x], df['Team_Name'],fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize = 15)
plt.show()
data1 = df.head(1)
print('As seen in the Graph which is based Stats of all Team Players and the past win loss ratio of all the teams\n The team that is predicted to win is',data1.loc[0,'Team_Name'])


# In[ ]:





# In[ ]:




