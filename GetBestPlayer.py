# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:41:28 2022

@author: ch406
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('darkgrid')

# nation_position, club_position, player_positions
df = pd.read_csv('players_22.csv', low_memory=False)

# selecting column
df = df[['short_name', 'age', 'nationality_name', 'overall', 'potential',
         'club_name', 'value_eur', 'wage_eur', 'player_positions']]
print(df.info())

# selecting only one position
df['player_positions'] = df['player_positions'].str.split(',', expand=True)[0]
# print(df[['short_name', 'nationality_name', 'overall','club_name', 'player_positions']].head())
# dropping nan
df.dropna(inplace=True)
print(df.info())

players_missing_worldcup = ['K. Benzema', 'S. Mané', 'S. Agüero', 'Sergio Ramos', 'P. Pogba',
                            'M. Reus', 'Diogo Jota', 'A. Harit', 'N. Kanté', 'G. Lo Celso', 'Piqué']

# dropping injured players
drop_index = df[df['short_name'].isin(players_missing_worldcup)].index
df.drop(drop_index, axis=0, inplace=True)
print(df.info())