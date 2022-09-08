import pickle
import pandas as pd
import numpy as np
import xgboost as xgb

df = pd.read_csv('static/data/stats_and_scores.csv', header = 0)
stats = pd.read_csv('static/data/kenpom.csv', header = 0)
xgb_spread = pickle.load(open('spread_model', 'rb'))
xgb_total = pickle.load(open('total_model', 'rb'))

avg_O = np.mean(stats.iloc[:, 3])
avg_D = np.mean(stats.iloc[:, 4])
avg_tempo = np.mean(stats.iloc[:, 5])

print('Enter Away Team:')
a = input()
print('Enter Home Team:')
h = input()
print('\n')

while (a != '' and h != ''):
	away = df[df['Team_away'] == a].iloc[0, 2:11]
	home = df[df['Team_home'] == h].iloc[0, 13:22]

	home_O = stats[stats['Team'] == h].iloc[0,3] + (.014 * stats[stats['Team'] == h].iloc[0,3])
	home_D = stats[stats['Team'] == h].iloc[0,4] - (.014 * stats[stats['Team'] == h].iloc[0,4])
	away_O = stats[stats['Team'] == a].iloc[0,3] - (.014 * stats[stats['Team'] == a].iloc[0,3])
	away_D = stats[stats['Team'] == a].iloc[0,4] + (.014 * stats[stats['Team'] == a].iloc[0,4])

	home_pythag = home_O ** 10.25 / (home_O ** 10.25 + home_D ** 10.25)
	away_pythag = away_O ** 10.25 / (away_O ** 10.25 + away_D ** 10.25)

	prob_home_win = (home_pythag - (home_pythag * away_pythag)) / (home_pythag + away_pythag - (2 * home_pythag * away_pythag))

	home_tempo_perc = stats[stats['Team'] == h].iloc[0,5] / avg_tempo
	away_tempo_perc = stats[stats['Team'] == a].iloc[0,5] / avg_tempo
	expected_tempo = home_tempo_perc * away_tempo_perc * avg_tempo

	home_O_adj = home_O / avg_O
	home_D_adj = home_D / avg_D
	away_O_adj = away_O / avg_O
	away_D_adj = away_D / avg_D

	home_score = home_O_adj * away_D_adj * avg_O * (expected_tempo / 100)
	away_score = away_O_adj * home_D_adj * avg_O * (expected_tempo / 100)

	new = pd.DataFrame(pd.concat((away, home), axis = 0)).T
	new = new.apply(pd.to_numeric)

	xg_spread_pred = xgb_spread.predict(new)
	xg_total_pred = xgb_total.predict(new)

	print('Probability' + ' ' + h + ' Wins: ' + str(prob_home_win))
	print('Probability' + ' ' + a + ' Wins: ' + str(1 - prob_home_win))
	print('Kenpom Predicted Score: ' + a + ' ' + str(away_score) + ', ' + h + ' ' + str(home_score))
	print('Kenpom Predicted Spread: ' + str(away_score - home_score))
	print('XGBoost Predicted Spread: ' + str(xg_spread_pred[0]))
	print('Kenpom Predicted Total: ' + str(away_score+home_score))
	print('XGBoost Predicted Total: ' + str(xg_total_pred[0]) + '\n')

	print('Enter Away Team:')
	a = input()
	print('Enter Home Team:')
	h = input()
	print('\n')