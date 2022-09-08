import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
from flask import Flask, abort, jsonify, request, render_template
import os

logo_folder = os.path.join('static', 'logos')

xgb_spread = pickle.load(open('spread_model', 'rb'))
xgb_total = pickle.load(open('total_model', 'rb'))
stats = pd.read_csv('static/data/kenpom.csv', header = 0)
df = pd.read_csv('static/data/stats_and_scores.csv', header = 0)

avg_O = np.mean(stats.iloc[:, 3])
avg_D = np.mean(stats.iloc[:, 4])
avg_tempo = np.mean(stats.iloc[:, 5])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = logo_folder

@app.route('/', methods = ['GET', 'POST'])
def make_predict():
	teams = np.unique(stats['Team'])
	if request.method == 'POST':
		away_request = request.form.get('away')
		home_request = request.form.get('home')

		file_chars = [' ', '.', "'"]
		away_logo = os.path.join(app.config['UPLOAD_FOLDER'], away_request.replace(' ', '').replace('.', '').
		replace("'", '') + '.png')
		home_logo = os.path.join(app.config['UPLOAD_FOLDER'], home_request.replace(' ', '').replace('.', '').
		replace("'", '') + '.png')

		home_O = stats[stats['Team'] == home_request].iloc[0,3] + (.014 * stats[stats['Team'] == home_request].iloc[0,3])
		home_D = stats[stats['Team'] == home_request].iloc[0,4] - (.014 * stats[stats['Team'] == home_request].iloc[0,4])
		away_O = stats[stats['Team'] == away_request].iloc[0,3] - (.014 * stats[stats['Team'] == away_request].iloc[0,3])
		away_D = stats[stats['Team'] == away_request].iloc[0,4] + (.014 * stats[stats['Team'] == away_request].iloc[0,4])

		home_pythag = home_O ** 10.25 / (home_O ** 10.25 + home_D ** 10.25)
		away_pythag = away_O ** 10.25 / (away_O ** 10.25 + away_D ** 10.25)

		prob_home_win = (home_pythag - (home_pythag * away_pythag)) / (home_pythag + away_pythag - (2 * home_pythag * away_pythag))
		prob_away_win = 1 - prob_home_win

		if (prob_home_win < .5):
			home_odds = '+' + str(round(((1 / prob_home_win) - 1) * 100))
		else:
			home_odds = str(round((prob_home_win / (1 - prob_home_win)) * -100))

		if (prob_away_win < .5):
			away_odds = '+' + str(round(((1 / prob_away_win) - 1) * 100))
		else:
			away_odds = str(round((prob_away_win / (1 - prob_away_win)) * -100))

		prob_away_win = round(prob_away_win, 2)
		prob_home_win = round(prob_home_win, 2)

		home_tempo_perc = stats[stats['Team'] == home_request].iloc[0,5] / avg_tempo
		away_tempo_perc = stats[stats['Team'] == away_request].iloc[0,5] / avg_tempo
		expected_tempo = home_tempo_perc * away_tempo_perc * avg_tempo

		home_O_adj = home_O / avg_O
		home_D_adj = home_D / avg_D
		away_O_adj = away_O / avg_O
		away_D_adj = away_D / avg_D

		home_score = home_O_adj * away_D_adj * avg_O * (expected_tempo / 100)
		away_score = away_O_adj * home_D_adj * avg_O * (expected_tempo / 100)
		ken_total = round(home_score + away_score, 2)
		home_score = round(home_score, 2)
		away_score = round(away_score, 2)

		away = df[df['Team_away'] == away_request].iloc[0, 2:11]
		home = df[df['Team_home'] == home_request].iloc[0, 13:22]

		new = pd.DataFrame(pd.concat((away, home), axis = 0)).T
		new = new.apply(pd.to_numeric)

		xg_spread_pred = xgb_spread.predict(new)
		xg_total_pred = xgb_total.predict(new)

		xg_spread_pred = round(xg_spread_pred[0], 2)
		xg_total_pred = round(xg_total_pred[0], 2)
		ken_spread = round(away_score - home_score, 2)

	else:
		xg_spread_pred = ''
		xg_total_pred = ''
		ken_spread = ''
		prob_home_win = ''
		prob_away_win = ''
		away_score = ''
		home_score = ''
		ken_total = ''
		home_odds = ''
		away_odds = ''
		away_request = ''
		home_request = ''
		away_logo = ''
		home_logo = ''

	return render_template('webapp.html', output_1=str(xg_spread_pred),
										  output_2=str(ken_spread),
										  output_3=str(prob_away_win),
										  output_4=str(prob_home_win),
										  output_5=str(away_score),
										  output_6=str(home_score),
										  output_7=str(ken_total),
										  output_8=home_odds,
										  output_9=away_odds,
										  output_10 = xg_total_pred,
										  away=away_request,
										  home=home_request,
										  away_logo = away_logo,
										  home_logo = home_logo,
										  teams=teams)

if __name__ == '__main__':
	app.run(port = 9000, debug = True)