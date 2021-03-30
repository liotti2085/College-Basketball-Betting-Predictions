import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error as MSE
import pickle

# Load the data
#kenpom = pd.read_csv('kenpom.csv', header = 0)
df = pd.read_csv('stats_and_scores.csv', header = 0)
X, spread, total = df.iloc[:, :-2], df.iloc[:, -2], df.iloc[:, -1] 

X = X.drop(['Date', 'Team_away', ' Conf_away', 'Team_home', ' Conf_home', 'Away_Team', 'Home_Team', 'Away_Score', 'Home_Score'], axis = 1)

# Test Train Split
train_X, test_X, train_Spread, test_Spread, train_total, test_total = train_test_split(
	X, spread, total, test_size = 0.3, random_state = 123)

# Instantiation
xgb_spread = xgb.XGBRegressor(objective = 'reg:squarederror',
							  booster = 'gbtree',
							  eta = .25,
							  max_depth = 4,
							  min_child_weight = 5,
						      n_estimators = 10)

#xgb_total = xgb.XGBRegressor(objective = 'reg:squarederror',
#							  booster = 'gbtree',
#							  eta = .3,
#							  max_depth = 4,
#							  min_child_weight = 1,
#						      n_estimators = 10)

#params = dict(eta = [.05, .1, .15, .2, .25, .3],
#			  max_depth = [4, 5, 6, 7, 8, 9, 10],
#			  min_child_weight = [1, 2, 3, 4, 5],
#			  gamma = [0, 1, 2, 3, 4, 5])

#clf = GridSearchCV(xgb_total, params)
#search = clf.fit(train_X, train_total)
#print(search.best_params_)

# Fitting Models
xgb_spread.fit(train_X, train_Spread)
#xgb_total.fit(train_X, train_total)

# Predicting
spread_pred = xgb_spread.predict(test_X)
#total_pred = xgb_total.predict(test_X)

# RMSE
spread_RMSE = np.sqrt(MSE(test_Spread, spread_pred))
#total_RMSE = np.sqrt(MSE(test_total, total_pred))
print(spread_RMSE)
#print(total_RMSE)

pickle.dump(xgb_spread, open('spread_model', 'wb'))
#pickle.dump(xgb_total, open('total_model', 'wb'))

#print('Enter Away Team:')
#a = input()
#print('Enter Home Team:')
#h = input()

#away = df[df['Team_away']==a].iloc[0, 2:11]
#home = df[df['Team_home'] ==h].iloc[0, 13:22]

#new = pd.DataFrame(pd.concat((away, home), axis = 0)).T
#new = new.apply(pd.to_numeric)
#print(new.dtypes)
#test_line = xgb_spread.predict(new)
#print(test_line)