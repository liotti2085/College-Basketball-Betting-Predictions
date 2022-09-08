import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error as MSE
import pickle

# Load the data

df = pd.read_csv('static/data/stats_and_scores.csv', header = 0)
df = df.dropna()
X, spread, total = df.iloc[:, :-2], df.iloc[:, -2], df.iloc[:, -1] 

X = X.drop(['Date', 'Team_away', ' Conf_away', 'Team_home', ' Conf_home', 'Away_Team', 'Home_Team', 'Away_Score', 'Home_Score'], axis = 1)

# Test Train Split
train_X, test_X, train_spread, test_spread, train_total, test_total = train_test_split(
	X, spread, total, test_size = 0.3, random_state = 123)

# Instantiation
xgb_spread = xgb.XGBRegressor(objective = 'reg:squarederror',
							  booster = 'gbtree')#,
							  # eta = .05,
							  # gamma = 2,
							  # max_depth = 4,
							  # min_child_weight = 5,
						   #    n_estimators = 10)

#xgb_total = xgb.XGBRegressor(objective = 'reg:squarederror',
#							  booster = 'gbtree')#,
							  # eta = .3,
							  # max_depth = 4,
							  # min_child_weight = 1,
						   #    n_estimators = 10)

params = dict(eta = [.05, .1, .15, .2, .25, .3],
			  max_depth = [4, 5, 6, 7, 8, 9, 10],
			  min_child_weight = [1, 2, 3, 4, 5],
			  gamma = [0, 1, 2, 3, 4, 5])

clf_spread = GridSearchCV(xgb_spread, params)
# clf_total = GridSearchCV(xgb_total, params)
search_spread = clf_spread.fit(train_X, train_spread)
# search_total = clf_total.fit(train_X, train_total)
print(search_spread.best_params_)
# print(search_total.best_params_)

xgb_spread.set_params(**search_spread.best_params_)
# xgb_total.set_params(**search_total.best_params_)

# Fitting Models
xgb_spread.fit(train_X, train_spread)
# xgb_total.fit(train_X, train_total)

# Predicting
spread_pred = xgb_spread.predict(test_X)
# total_pred = xgb_total.predict(test_X)

# RMSE
spread_RMSE = np.sqrt(MSE(test_spread, spread_pred))
# total_RMSE = np.sqrt(MSE(test_total, total_pred))
print(spread_RMSE)
# print(total_RMSE)

pickle.dump(xgb_spread, open('spread_model', 'wb'))
# pickle.dump(xgb_total, open('total_model', 'wb'))