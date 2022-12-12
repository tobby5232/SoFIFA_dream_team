# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 19:11:33 2022

@author: ch406
"""

#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import numpy as np
from colour import Color
sns.set_style('darkgrid')

fp="WhoScoreRanting.json"

with open(fp,encoding="utf-8") as file:
    data1=file.read()
    
file_dic=json.loads(data1)
file_dic=file_dic["playerTableStats"]

player_df=pd.DataFrame(file_dic)
#Pick column to analysis
player_df=player_df[["name","rating","positionText",
                     "goal","assistTotal","minsPlayed",
                     "teamName"]]
# print(player_df.info())
# print(player_df.describe())

#%%
#List top 20 best player
TopPlayer_df=player_df.sort_values(by=["rating"],ascending=False)
TopPlayer_df=TopPlayer_df[["name","teamName","rating","positionText"]]
TopPlayer_df.rename(columns = {'name':'Name','teamName':'Nation',
                               'rating':'Rating','positionText':'Position'}, inplace = True)
print(TopPlayer_df.info())
print(TopPlayer_df.head(20))

#Simplfy team name
country_short =  TopPlayer_df['Nation'].str.extract('(^\w{3})', expand=False).str.upper()
TopPlayer_df['name_nationality'] = TopPlayer_df['Name'] +' (' + country_short + ')'
TopPlayer_df=TopPlayer_df.head(20).sort_values(by=["Rating"],ascending=True)

#Draw top 20 best player
#Color 漸層色
red = Color("blue")
colors = list(red.range_to(Color("green"),20))
colors = [color.rgb for color in colors]

fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)
plt.barh(TopPlayer_df['name_nationality'], TopPlayer_df['Rating'], color=colors)
plt.title("Top 20 players",size=15)
plt.show()

#%%
#Plot distribution and density plot
fig, ax = plt.subplots(figsize=(12, 5), tight_layout=True)
sns.histplot(player_df['rating'],kde=True,binwidth=0.1,
             line_kws={'lw': 2})
bins = np.arange(player_df['rating'].min(), 
                 player_df['rating'].max(), 0.3)
plt.xticks(bins)
plt.xlabel("Rating",size=10)
plt.ylabel("Count",size=10)
plt.title("Player rating distribution",size=15)
plt.show()


#%%
#Clean data fram as df_team_rating(Simplfy team name & group by nation)
df_team_rating = player_df.copy()
df_team_rating["teamName"]=country_short

#Group by "teamName"
df_team_rating=df_team_rating.groupby("teamName").mean()
df_team_rating=df_team_rating.sort_values(by=["rating"],ascending=False)
print(df_team_rating.info())
print(df_team_rating.head(50))
print("All player average rating: %.2f" %df_team_rating["rating"].mean())
print("Rating std: %.2f" %df_team_rating["rating"].std())
print("Rating mid: %.2f" %df_team_rating["rating"].median())
print("Rating first quartile: %.2f" %df_team_rating["rating"].quantile(.25))
print("Rating second quartile: %.2f" %df_team_rating["rating"].quantile(.5))
print("Rating second quartile: %.2f" %df_team_rating["rating"].quantile(.55))
print("Rating fourth quartile: %.2f" %df_team_rating["rating"].quantile(1))
# [6.15,6.5,6.575,6.72,7.1]

#%%
#Seperate team in different level by rating
bins=[6.15,6.5,6.575,6.72,7.1]
labels = ['Poor', 'Bad', 'Good', 'Great']
colors = ['red','orange','lightgreen','darkgreen']
df_team_ranting_group = pd.DataFrame({'rating':df_team_rating["rating"],
                                      'level': pd.cut(df_team_rating["rating"],
                                                      bins=bins, labels=labels),
                                      'colors':pd.cut(df_team_rating["rating"],
                                                      bins=bins, labels=colors)})
# print(df_team_ranting_group)
#Draw bar chart by team average rating
fig, ax = plt.subplots(figsize=(12, 5), tight_layout=True)
labels=list(df_team_rating.index)
xticks = range(32)
plt.xticks(xticks, labels)
p1=plt.bar(xticks,df_team_ranting_group["rating"],
           color=df_team_ranting_group['colors'],
           label=df_team_ranting_group['level'])
plt.axis([-1,32,6.1,7.05])
plt.bar_label(p1,fmt='%.2f',padding=10,label_type='edge')
plt.xlabel("Countary",size=10)
plt.ylabel("Rating",size=10)
plt.title("Team average rating",size=15)
#Avoid legend repeating
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(),fontsize=15,title='Team perform',title_fontsize=18)
plt.show()

#%%
#Get best player at each position
print("Total player for each position :\n",player_df.groupby("positionText").count()["name"])

df_BestPlayer = player_df.copy()
#playtime over 270 mins
df_BestPlayer=df_BestPlayer[df_BestPlayer['minsPlayed']>=270]

df_BestPlayer=df_BestPlayer.sort_values(by=["rating"],ascending=False)
df_BestPlayer =df_BestPlayer.groupby("positionText")

df_goalKeeper=df_BestPlayer.get_group("Goalkeeper").reset_index()
print(df_goalKeeper.head())
df_Defender=df_BestPlayer.get_group("Defender").reset_index()
print(df_Defender.head())
df_Midfielder=df_BestPlayer.get_group("Midfielder").reset_index()
print(df_Midfielder.head())
df_Forward=df_BestPlayer.get_group("Forward").reset_index()
print(df_Forward.head())

#Print best rating player in each position
goalKeeper=df_goalKeeper.at[0,"name"]
print(goalKeeper)

Defender=[]
for i in range(4):
    Defender.append(df_Defender.at[i,"name"])
    print(Defender[i])
    
Midfielder=[]
for i in range(3):
    Midfielder.append(df_Midfielder.at[i,"name"])
    print(Midfielder[i])
    
Forward=[]
for i in range(3):
    Forward.append(df_Forward.at[i,"name"])
    print(Forward[i])

