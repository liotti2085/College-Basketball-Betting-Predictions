from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import requests
import json
import re

url = 'https://www.espn.com/mens-college-basketball/teams'

# driver = webdriver.Firefox(executable_path = 'C:/Users/Nick/geckodriver.exe')
# driver.get(url)

#page_html = requests.get(url).text

# open connection, grab page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

site_json = str(page_soup.find_all('script', {'type':'text/javascript'})[2].extract())

site_json = site_json[54:-10]

j = json.loads(site_json)

j = j['page']['content']['leagueTeams']['columns']

links = re.findall(r'https://a.espncdn.com/i/teamlogos/ncaa/500/[0-9]{1,4}', str(j))

# logos = page_soup.find_all('img', attrs={'class':'Image Logo Logo__lg'})

i = 1
for link in links: 
	print(link)
	r = requests.get(link[0:22] + 'combiner/i?img=/' + link[22:] + '.png&scale=crop&cquality=40&location=origin&w=200&h=200')
	with open(str(i)+'.png', 'wb') as f:
		f.write(r.content)
	i += 1