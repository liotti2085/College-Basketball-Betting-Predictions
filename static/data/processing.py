import pandas as pd
import numpy as np
#from fuzzywuzzy import fuzz
#from fuzzywuzzy import process

stats = pd.read_csv("kenpom.csv", header = 0)
scores = pd.read_csv("temp.csv", header = 0)

dfjoin = pd.merge(stats, scores, left_on = 'Team', right_on = 'Home_Team')
dfjoin = pd.merge(stats, dfjoin, left_on = 'Team', right_on = 'Away_Team', suffixes = ('_away', '_home'))

dfjoin['Spread'] = dfjoin.apply(lambda row: row.Away_Score - row.Home_Score, axis = 1)
dfjoin['Total'] = dfjoin.apply(lambda row: row.Away_Score + row.Home_Score, axis = 1)

dfjoin.to_csv('stats_and_scores.csv', index = False)