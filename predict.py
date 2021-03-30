import pickle
import pandas as pd
import xgboost as xgb

df = pd.read_csv('stats_and_scores.csv', header = 0)
xgb_spread = pickle.load(open('spread_model', 'rb'))
xgb_total = pickle.load(open('total_model', 'rb'))

print('Enter Away Team:')
a = input()
print('Enter Home Team:')
h = input()

while (a != '' and h != ''):
	away = df[df['Team_away']==a].iloc[0, 2:11]
	home = df[df['Team_home'] ==h].iloc[0, 13:22]

	new = pd.DataFrame(pd.concat((away, home), axis = 0)).T
	new = new.apply(pd.to_numeric)

	spread_pred = xgb_spread.predict(new)
	total_pred = xgb_total.predict(new)
	print(spread_pred)
	print(total_pred)
	print('Enter Away Team:')
	a = input()
	print('Enter Home Team:')
	h = input()