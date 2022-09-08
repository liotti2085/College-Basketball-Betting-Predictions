from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup
from time import sleep
from random import randint
import pandas as pd

def xstr(x):
	if x is None:
		return ''
	return str(x)

start_date = '2021-10-01'
end_date = '2022-04-04'
daterange = pd.date_range(start=start_date, end=end_date)
string = 'https://www.ncaa.com/scoreboard/basketball-men/d1/{}/{}/{}/all-conf'

dates = []
away_teams = []
away_scores =[]
home_teams = []
home_scores =[]

for date in daterange:
	url = string.format(date.year, "{0:0>2}".format(date.month), "{0:0>2}".format(date.day))
	day = "{}-{}-{}".format(date.year, "{0:0>2}".format(date.month), "{0:0>2}".format(date.day))

	# open connection, grab page
	try:		
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
			
	except HTTPError as e:
		continue

	else:
		# html parsing
		page_soup = soup(page_html, "html.parser")

		if (page_soup.find('div', attrs = {'class' : 'gamePod_content'}).text == "No games"):
			continue

		#game_pods = page_soup.find_all('ul', attrs = {'class' : 'gamePod-game-teams'})
		game_pods = page_soup.find_all('div', attrs = {'class' : 'gamePod gamePod-type-game status-final'})
		sleep(randint(1,3))

		for container in game_pods:
			if (container.find('a', attrs = {'href' : '/game/5769061'})):
				continue
			dates.append(day)

			team_pods = container.find('ul')

			away_team = team_pods.findChildren('span', attrs = {'class' : 'gamePod-game-team-name'})[0].text
			away_teams.append(away_team)

			away_score = team_pods.findChildren('span', attrs = {'class' : 'gamePod-game-team-score'})[0].text
			away_scores.append(away_score)

			home_team = team_pods.findChildren('span', attrs = {'class' : 'gamePod-game-team-name'})[1].text
			home_teams.append(home_team)

			home_score = team_pods.findChildren('span', attrs = {'class' : 'gamePod-game-team-score'})[1].text
			home_scores.append(home_score)

scores = pd.DataFrame({
	'Date' : dates,
	'Away_Team' : away_teams,
	'Away_Score' : away_scores,
	'Home_Team' : home_teams,
	'Home_Score' : home_scores,
	})

scores.to_csv('scores.csv', index = False)

