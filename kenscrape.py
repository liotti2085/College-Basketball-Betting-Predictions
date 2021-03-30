from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd

def xstr(x):
	if x is None:
		return ''
	return str(x)

url = 'https://kenpom.com/'

# open connection, grab page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

table = page_soup.table

table_rows = table.find_all('tr', attrs = {'class' : lambda x: xstr(x) == '' or xstr(x) == 'bold-bottom'})

filename = "kenpom.csv"
f = open(filename, "w")

headers = "Team, Conf, AjdEM, AdjO, AdjD, AdjT, Luck, SOS_AdjEM, SOS_OppO, SOS_OppD, NCSOS_AdjEM\n"
f.write(headers)

for tr in table_rows:
	names = tr.find('a')
	conf = tr.find('td', {'class' : 'conf'})
	adjem = tr.find('td', {'class' : None})
	stats = tr.find_all('td', {'class' : 'td-left'})
	row = [i.text for i in stats]
	#print(names.text, conf.text, adjem.text, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
	f.write(names.text+','+conf.text+','+adjem.text+','+row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6]+','+row[7]+'\n')

f.close()