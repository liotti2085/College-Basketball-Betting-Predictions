# College-Basketball-Betting
Machine Learning model for predicting college basketball spreads and totals 

scorescrape.py-scrapes scores from NCAA.com
kenscrape.py-scrapes stats from kenpom.com
fixnames.py-fixes names so they match and can be merged easily
processing.py-merges the 2 datasets 
kenpom_model.py-XGBoost model and tuning
predict.py-predict new spreads and totals without having to retrain the model
