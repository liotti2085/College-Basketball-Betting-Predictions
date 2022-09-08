import pandas as pd

temp = pd.read_csv('scores.csv', header = 0)

for i in range(0, temp.shape[0]):
	#Albany (NY) -> Albany
	if (temp.loc[i, 'Away_Team'] == 'Albany (NY)'):
		temp.loc[i, 'Away_Team'] = 'Albany'
	if (temp.loc[i, 'Home_Team'] == 'Albany (NY)'):
		temp.loc[i, 'Home_Team'] = 'Albany'

	#South Fla. -> South Florida
	if (temp.loc[i, 'Away_Team'] == 'South Fla.'):
		temp.loc[i, 'Away_Team'] = 'South Florida'
	if (temp.loc[i, 'Home_Team'] == 'South Fla.'):
		temp.loc[i, 'Home_Team'] = 'South Florida'

	#NC State -> N.C. State
	if (temp.loc[i, 'Away_Team'] == 'NC State'):
		temp.loc[i, 'Away_Team'] = 'N.C. State'
	if (temp.loc[i, 'Home_Team'] == 'NC State'):
		temp.loc[i, 'Home_Team'] = 'N.C. State'


	#Miami (FL) -> Miami FL	
	if (temp.loc[i, 'Away_Team'] == 'Miami (FL)'):
		temp.loc[i, 'Away_Team'] = 'Miami FL'
	if (temp.loc[i, 'Home_Team'] == 'Miami (FL)'):
		temp.loc[i, 'Home_Team'] = 'Miami FL'

	#North Ala. -> North Alabama
	if (temp.loc[i, 'Away_Team'] == 'North Ala.'):
		temp.loc[i, 'Away_Team'] = 'North Alabama'
	if (temp.loc[i, 'Home_Team'] == 'North Ala.'):
		temp.loc[i, 'Home_Team'] = 'North Alabama'

	#FGCU -> Florida Gulf Coast
	if (temp.loc[i, 'Away_Team'] == 'FGCU'):
		temp.loc[i, 'Away_Team'] = 'Florida Gulf Coast'
	if (temp.loc[i, 'Home_Team'] == 'FGCU'):
		temp.loc[i, 'Home_Team'] = 'Florida Gulf Coast'

	#St. John's (NY) -> St. John's
	if (temp.loc[i, 'Away_Team'] == "St. John's (NY)"):
		temp.loc[i, 'Away_Team'] = "St. John's"
	if (temp.loc[i, 'Home_Team'] == "St. John's (NY)"):
		temp.loc[i, 'Home_Team'] = "St. John's"
	
	#UConn -> Connecticut
	if (temp.loc[i, 'Away_Team'] == 'UConn'):
		temp.loc[i, 'Away_Team'] = 'Connecticut'
	if (temp.loc[i, 'Home_Team'] == 'UConn'):
		temp.loc[i, 'Home_Team'] = 'Connecticut'
	
	#Northern Ariz. -> Northern Arizona
	if (temp.loc[i, 'Away_Team'] == 'Northern Ariz.'):
		temp.loc[i, 'Away_Team'] = 'Northern Arizona'
	if (temp.loc[i, 'Home_Team'] == 'Northern Ariz.'):
		temp.loc[i, 'Home_Team'] = 'Northern Arizona'

	# Northern Colo. -> Northern Colorado
	if (temp.loc[i, 'Away_Team'] == 'Northern Colo.'):
		temp.loc[i, 'Away_Team'] = 'Northern Colorado'
	if (temp.loc[i, 'Home_Team'] == 'Northern Colo.'):
		temp.loc[i, 'Home_Team'] = 'Northern Colorado'
	
	# Eastern Wash. -> Eastern Washington
	if (temp.loc[i, 'Away_Team'] == 'Eastern Wash.'):
		temp.loc[i, 'Away_Team'] = 'Eastern Washington'
	if (temp.loc[i, 'Home_Team'] == 'Eastern Wash.'):
		temp.loc[i, 'Home_Team'] = 'Eastern Washington'

	# Charleson So. -> Charleston Southern
	if (temp.loc[i, 'Away_Team'] == 'Charleston So.'):
		temp.loc[i, 'Away_Team'] = 'Charleston Southern'
	if (temp.loc[i, 'Home_Team'] == 'Charleston So.'):
		temp.loc[i, 'Home_Team'] = 'Charleston Southern'

	# Gardner-Webb -> Gardner Webb
	if (temp.loc[i, 'Away_Team'] == 'Gardner-Webb'):
		temp.loc[i, 'Away_Team'] = 'Gardner Webb'
	if (temp.loc[i, 'Home_Team'] == 'Gardner-Webb'):
		temp.loc[i, 'Home_Team'] = 'Gardner Webb'

	# CSU Bakersfield -> Cal St. Bakersfield
	if (temp.loc[i, 'Away_Team'] == 'CSU Bakersfield'):
		temp.loc[i, 'Away_Team'] = 'Cal St. Bakersfield'
	if (temp.loc[i, 'Home_Team'] == 'CSU Bakersfield'):
		temp.loc[i, 'Home_Team'] = 'Cal St. Bakersfield'

	# CSUN -> Cal St. Northridge
	if (temp.loc[i, 'Away_Team'] == 'CSUN'):
		temp.loc[i, 'Away_Team'] = 'Cal St. Northridge'
	if (temp.loc[i, 'Home_Team'] == 'CSUN'):
		temp.loc[i, 'Home_Team'] = 'Cal St. Northridge'

	# Col. of Charleston -> Charleston
	if (temp.loc[i, 'Away_Team'] == 'Col. of Charleston'):
		temp.loc[i, 'Away_Team'] = 'Charleston'
	if (temp.loc[i, 'Home_Team'] == 'Col. of Charleston'):
		temp.loc[i, 'Home_Team'] = 'Charleston'

	# UNCW -> UNC Wilmington
	if (temp.loc[i, 'Away_Team'] == 'UNCW'):
		temp.loc[i, 'Away_Team'] = 'UNC Wilmington'
	if (temp.loc[i, 'Home_Team'] == 'UNCW'):
		temp.loc[i, 'Home_Team'] = 'UNC Wilmington'

	# Western Ky. -> Western Kentucky
	if (temp.loc[i, 'Away_Team'] == 'Western Ky.'):
		temp.loc[i, 'Away_Team'] = 'Western Kentucky'
	if (temp.loc[i, 'Home_Team'] == 'Western Ky.'):
		temp.loc[i, 'Home_Team'] = 'Western Kentucky'

	# Southern Miss. -> Southern Miss
	if (temp.loc[i, 'Away_Team'] == 'Southern Miss.'):
		temp.loc[i, 'Away_Team'] = 'Southern Miss'
	if (temp.loc[i, 'Home_Team'] == 'Southern Miss.'):
		temp.loc[i, 'Home_Team'] = 'Southern Miss'

	# Fla. Atlantic -> Florida Atlantic
	if (temp.loc[i, 'Away_Team'] == 'Fla. Atlantic'):
		temp.loc[i, 'Away_Team'] = 'Florida Atlantic'
	if (temp.loc[i, 'Home_Team'] == 'Fla. Atlantic'):
		temp.loc[i, 'Home_Team'] = 'Florida Atlantic'

	# Middle Tenn. -> Middle Tennessee
	if (temp.loc[i, 'Away_Team'] == 'Middle Tenn.'):
		temp.loc[i, 'Away_Team'] = 'Middle Tennessee'
	if (temp.loc[i, 'Home_Team'] == 'Middle Tenn.'):
		temp.loc[i, 'Home_Team'] = 'Middle Tennessee'

	# UIC -> Illinois Chicago
	if (temp.loc[i, 'Away_Team'] == 'UIC'):
		temp.loc[i, 'Away_Team'] = 'Illinois Chicago'
	if (temp.loc[i, 'Home_Team'] == 'UIC'):
		temp.loc[i, 'Home_Team'] = 'Illinois Chicago'

	# Northern Ky. -> Northern Kentucky
	if (temp.loc[i, 'Away_Team'] == 'Northern Ky.'):
		temp.loc[i, 'Away_Team'] = 'Northern Kentucky'
	if (temp.loc[i, 'Home_Team'] == 'Northern Ky.'):
		temp.loc[i, 'Home_Team'] = 'Northern Kentucky'

	# Detroit Mercy -> Detroit
	if (temp.loc[i, 'Away_Team'] == 'Detroit Mercy'):
		temp.loc[i, 'Away_Team'] = 'Detroit'
	if (temp.loc[i, 'Home_Team'] == 'Detroit Mercy'):
		temp.loc[i, 'Home_Team'] = 'Detroit'

	# Miami (OH) -> Miami OH
	if (temp.loc[i, 'Away_Team'] == 'Miami (OH)'):
		temp.loc[i, 'Away_Team'] = 'Miami OH'
	if (temp.loc[i, 'Home_Team'] == 'Miami (OH)'):
		temp.loc[i, 'Home_Team'] = 'Miami OH'

	# Central Mich. -> Central Michigan
	if (temp.loc[i, 'Away_Team'] == 'Central Mich.'):
		temp.loc[i, 'Away_Team'] = 'Central Michigan'
	if (temp.loc[i, 'Home_Team'] == 'Central Mich.'):
		temp.loc[i, 'Home_Team'] = 'Central Michigan'

	# Western Mich. -> Western Michigan
	if (temp.loc[i, 'Away_Team'] == 'Western Mich.'):
		temp.loc[i, 'Away_Team'] = 'Western Michigan'
	if (temp.loc[i, 'Home_Team'] == 'Western Mich.'):
		temp.loc[i, 'Home_Team'] = 'Western Michigan'

	# Eastern Michigan -> Eastern Michigan
	if (temp.loc[i, 'Away_Team'] == 'Eastern Mich.'):
		temp.loc[i, 'Away_Team'] = 'Eastern Michigan'
	if (temp.loc[i, 'Home_Team'] == 'Eastern Mich.'):
		temp.loc[i, 'Home_Team'] = 'Eastern Michigan'

	# Northern Ill. -> Northern Illinois
	if (temp.loc[i, 'Away_Team'] == 'Northern Ill.'):
		temp.loc[i, 'Away_Team'] = 'Northern Illinois'
	if (temp.loc[i, 'Home_Team'] == 'Northern Ill.'):
		temp.loc[i, 'Home_Team'] = 'Northern Illinois'

	# N.C. A&T -> North Caroline A&T
	if (temp.loc[i, 'Away_Team'] == 'N.C. A&T'):
		temp.loc[i, 'Away_Team'] = 'North Carolina A&T'
	if (temp.loc[i, 'Home_Team'] == 'N.C. A&T'):
		temp.loc[i, 'Home_Team'] = 'North Carolina A&T'

	# UNI -> Northern Iowa
	if (temp.loc[i, 'Away_Team'] == 'UNI'):
		temp.loc[i, 'Away_Team'] = 'Northern Iowa'
	if (temp.loc[i, 'Home_Team'] == 'UNI'):
		temp.loc[i, 'Home_Team'] = 'Northern Iowa'

	# Southern Ill. -> Southern Illinois
	if (temp.loc[i, 'Away_Team'] == 'Southern Ill.'):
		temp.loc[i, 'Away_Team'] = 'Southern Illinois'
	if (temp.loc[i, 'Home_Team'] == 'Southern Ill.'):
		temp.loc[i, 'Home_Team'] = 'Southern Illinois'

	# St. Francis Brooklyn -> St. Francis NY
	if (temp.loc[i, 'Away_Team'] == 'St. Francis Brooklyn'):
		temp.loc[i, 'Away_Team'] = 'St. Francis NY'
	if (temp.loc[i, 'Home_Team'] == 'St. Francis Brooklyn'):
		temp.loc[i, 'Home_Team'] = 'St. Francis NY'

	# Saint Francis (PA) -> St. Francis PA
	if (temp.loc[i, 'Away_Team'] == 'Saint Francis (PA)'):
		temp.loc[i, 'Away_Team'] = 'St. Francis PA'
	if (temp.loc[i, 'Home_Team'] == 'Saint Francis (PA)'):
		temp.loc[i, 'Home_Team'] = 'St. Francis PA'

	# Central Conn. St. -> Central Connecticut
	if (temp.loc[i, 'Away_Team'] == 'Central Conn. St.'):
		temp.loc[i, 'Away_Team'] = 'Central Connecticut'
	if (temp.loc[i, 'Home_Team'] == 'Central Conn. St.'):
		temp.loc[i, 'Home_Team'] = 'Central Conncticut'

	# SIUE -> SIU Edwardsville
	if (temp.loc[i, 'Away_Team'] == 'SIUE'):
		temp.loc[i, 'Away_Team'] = 'SIU Edwardsville'
	if (temp.loc[i, 'Home_Team'] == 'SIUE'):
		temp.loc[i, 'Home_Team'] = 'SIU Edwardsville'

	# Eastern Ky. -> Eastern Kentucky
	if (temp.loc[i, 'Away_Team'] == 'Eastern Ky.'):
		temp.loc[i, 'Away_Team'] = 'Eastern Kentucky'
	if (temp.loc[i, 'Home_Team'] == 'Eastern Ky.'):
		temp.loc[i, 'Home_Team'] = 'Eastern Kentucky'

	# Southeast Mo. St. -> Southeast Missouri St.
	if (temp.loc[i, 'Away_Team'] == 'Southeast Mo. St.'):
		temp.loc[i, 'Away_Team'] = 'Southeast Missouri St.'
	if (temp.loc[i, 'Home_Team'] == 'Southeast Mo. St.'):
		temp.loc[i, 'Home_Team'] = 'Southeast Missouri St.'

	# Eastern Ill. -> Eastern Illinois
	if (temp.loc[i, 'Away_Team'] == 'Eastern Ill.'):
		temp.loc[i, 'Away_Team'] = 'Eastern Illinois'
	if (temp.loc[i, 'Home_Team'] == 'Eastern Ill.'):
		temp.loc[i, 'Home_Team'] = 'Eastern Illinois'

	# UT Martin -> Tennessee Martin
	if (temp.loc[i, 'Away_Team'] == 'UT Martin'):
		temp.loc[i, 'Away_Team'] = 'Tennessee Martin'
	if (temp.loc[i, 'Home_Team'] == 'UT Martin'):
		temp.loc[i, 'Home_Team'] = 'Tennessee Martin'

	# Southern California -> USC
	if (temp.loc[i, 'Away_Team'] == 'Southern California'):
		temp.loc[i, 'Away_Team'] = 'USC'
	if (temp.loc[i, 'Home_Team'] == 'Southern California'):
		temp.loc[i, 'Home_Team'] = 'USC'

	# Army West Point -> Army
	if (temp.loc[i, 'Away_Team'] == 'Army West Point'):
		temp.loc[i, 'Away_Team'] = 'Army'
	if (temp.loc[i, 'Home_Team'] == 'Army West Point'):
		temp.loc[i, 'Home_Team'] = 'Army'

	# Boston U. -> Boston University
	if (temp.loc[i, 'Away_Team'] == 'Boston U.'):
		temp.loc[i, 'Away_Team'] = 'Boston University'
	if (temp.loc[i, 'Home_Team'] == 'Boston U.'):
		temp.loc[i, 'Home_Team'] = 'Boston University'

	# Loyola Maryland -> Loyola MD
	if (temp.loc[i, 'Away_Team'] == 'Loyola Maryland'):
		temp.loc[i, 'Away_Team'] = 'Loyola MD'
	if (temp.loc[i, 'Home_Team'] == 'Loyola Maryland'):
		temp.loc[i, 'Home_Team'] = 'Loyola MD'

	# Ole Miss -> Mississippi
	if (temp.loc[i, 'Away_Team'] == 'Ole Miss'):
		temp.loc[i, 'Away_Team'] = 'Mississippi'
	if (temp.loc[i, 'Home_Team'] == 'Ole Miss'):
		temp.loc[i, 'Home_Team'] = 'Mississippi'

	# ETSU -> East Tennessee St.
	if (temp.loc[i, 'Away_Team'] == 'ETSU'):
		temp.loc[i, 'Away_Team'] = 'East Tennessee St.'
	if (temp.loc[i, 'Home_Team'] == 'ETSU'):
		temp.loc[i, 'Home_Team'] = 'East Tennessee St.'

	# Western Caro. -> Western Carolina
	if (temp.loc[i, 'Away_Team'] == 'Western Caro.'):
		temp.loc[i, 'Away_Team'] = 'Western Carolina'
	if (temp.loc[i, 'Home_Team'] == 'Western Caro.'):
		temp.loc[i, 'Home_Team'] = 'Western Carolina'

	# Sam Houston -> Sam Houston St.
	if (temp.loc[i, 'Away_Team'] == 'Sam Houston'):
		temp.loc[i, 'Away_Team'] = 'Sam Houston St.'
	if (temp.loc[i, 'Home_Team'] == 'Sam Houston'):
		temp.loc[i, 'Home_Team'] = 'Sam Houston St.'

	# SFA -> Stephen F. Austin
	if (temp.loc[i, 'Away_Team'] == 'SFA'):
		temp.loc[i, 'Away_Team'] = 'Stephen F. Austin'
	if (temp.loc[i, 'Home_Team'] == 'SFA'):
		temp.loc[i, 'Home_Team'] = 'Stephen F. Austin'

	# UIW -> Incarnate Word
	if (temp.loc[i, 'Away_Team'] == 'UIW'):
		temp.loc[i, 'Away_Team'] = 'Incarnate Word'
	if (temp.loc[i, 'Home_Team'] == 'UIW'):
		temp.loc[i, 'Home_Team'] = 'Incarnate Word'

	# Southeastern La. -> Southeastern Louisiana
	if (temp.loc[i, 'Away_Team'] == 'Southeastern La.'):
		temp.loc[i, 'Away_Team'] = 'Southeastern Louisiana'
	if (temp.loc[i, 'Home_Team'] == 'Southeastern La.'):
		temp.loc[i, 'Home_Team'] = 'Southeastern Louisiana'

	# Central Ark. -> Central Arkansas
	if (temp.loc[i, 'Away_Team'] == 'Central Ark.'):
		temp.loc[i, 'Away_Team'] = 'Central Arkansas'
	if (temp.loc[i, 'Home_Team'] == 'Central Ark.'):
		temp.loc[i, 'Home_Team'] = 'Central Arkansas'

	# Lamar University -> Lamar
	if (temp.loc[i, 'Away_Team'] == 'Lamar University'):
		temp.loc[i, 'Away_Team'] = 'Lamar'
	if (temp.loc[i, 'Home_Team'] == 'Lamar University'):
		temp.loc[i, 'Home_Team'] = 'Lamar'

	# A&M-Corpus Christi -> Texas A&M Corpus Chris
	if (temp.loc[i, 'Away_Team'] == 'A&M-Corpus Christi'):
		temp.loc[i, 'Away_Team'] = 'Texas A&M Corpus Chris'
	if (temp.loc[i, 'Home_Team'] == 'A&M-Corpus Christi'):
		temp.loc[i, 'Home_Team'] = 'Texas A&M Corpus Chris'

	# McNeese -> McNeese St.
	if (temp.loc[i, 'Away_Team'] == 'McNeese'):
		temp.loc[i, 'Away_Team'] = 'McNeese St.'
	if (temp.loc[i, 'Home_Team'] == 'McNeese'):
		temp.loc[i, 'Home_Team'] = 'McNeese St.'

	# Southern U. -> Southern
	if (temp.loc[i, 'Away_Team'] == 'Southern U.'):
		temp.loc[i, 'Away_Team'] = 'Southern'
	if (temp.loc[i, 'Home_Team'] == 'Southern U.'):
		temp.loc[i, 'Home_Team'] = 'Southern'

	# Prairie View -> Prairie View A&M
	if (temp.loc[i, 'Away_Team'] == 'Prairie View'):
		temp.loc[i, 'Away_Team'] = 'Prairie View A&M'
	if (temp.loc[i, 'Home_Team'] == 'Prairie View'):
		temp.loc[i, 'Home_Team'] = 'Prairie View A&M'

	# Alcorn -> Alcorn St.
	if (temp.loc[i, 'Away_Team'] == 'Alcorn'):
		temp.loc[i, 'Away_Team'] = 'Alcorn St.'
	if (temp.loc[i, 'Home_Team'] == 'Alcorn'):
		temp.loc[i, 'Home_Team'] = 'Alcorn St.'

	# Grambling -> Grambling St.
	if (temp.loc[i, 'Away_Team'] == 'Grambling'):
		temp.loc[i, 'Away_Team'] = 'Grambling St.'
	if (temp.loc[i, 'Home_Team'] == 'Grambling'):
		temp.loc[i, 'Home_Team'] = 'Grambling St.'

	# Ark.-Pinr Bluff -> Arkansas Pine Bluff
	if (temp.loc[i, 'Away_Team'] == 'Ark.-Pine Bluff'):
		temp.loc[i, 'Away_Team'] = 'Arkansas Pine Bluff'
	if (temp.loc[i, 'Home_Team'] == 'Ark.-Pine Bluff'):
		temp.loc[i, 'Home_Team'] = 'Arkansas Pine Bluff'

	# Mississippi Val. -> Mississippi Valley St.
	if (temp.loc[i, 'Away_Team'] == 'Mississippi Val.'):
		temp.loc[i, 'Away_Team'] = 'Mississippi Valley St.'
	if (temp.loc[i, 'Home_Team'] == 'Mississippi Val.'):
		temp.loc[i, 'Home_Team'] = 'Mississippi Valley St.'

	# Kansas City -> UMKC
	if (temp.loc[i, 'Away_Team'] == 'Kansas City'):
		temp.loc[i, 'Away_Team'] = 'UMKC'
	if (temp.loc[i, 'Home_Team'] == 'Kansas City'):
		temp.loc[i, 'Home_Team'] = 'UMKC'

	# Western Ill. -> Western Illinois
	if (temp.loc[i, 'Away_Team'] == 'Western Ill.'):
		temp.loc[i, 'Away_Team'] = 'Western Illinois'
	if (temp.loc[i, 'Home_Team'] == 'Western Ill.'):
		temp.loc[i, 'Home_Team'] = 'Western Illinois'

	# Omaha -> Nebraska Omaha
	if (temp.loc[i, 'Away_Team'] == 'Omaha'):
		temp.loc[i, 'Away_Team'] = 'Nebraska Omaha'
	if (temp.loc[i, 'Home_Team'] == 'Omaha'):
		temp.loc[i, 'Home_Team'] = 'Nebraska Omaha'

	# App State -> Appalachian St.
	if (temp.loc[i, 'Away_Team'] == 'App State'):
		temp.loc[i, 'Away_Team'] = 'Appalachian St.'
	if (temp.loc[i, 'Home_Team'] == 'App State'):
		temp.loc[i, 'Home_Team'] = 'Appalachian St.'

	# ULM -> Louisiana Monroe
	if (temp.loc[i, 'Away_Team'] == 'ULM'):
		temp.loc[i, 'Away_Team'] = 'Louisiana Monroe'
	if (temp.loc[i, 'Home_Team'] == 'ULM'):
		temp.loc[i, 'Home_Team'] = 'Louisiana Monroe'

	# Ga. Southern -> Georgia Southern
	if (temp.loc[i, 'Away_Team'] == 'Ga. Southern'):
		temp.loc[i, 'Away_Team'] = 'Georgia Southern'
	if (temp.loc[i, 'Home_Team'] == 'Ga. Southern'):
		temp.loc[i, 'Home_Team'] = 'Georgia Southern'

	# LMU (CA) -> Loyola Marymount
	if (temp.loc[i, 'Away_Team'] == 'LMU (CA)'):
		temp.loc[i, 'Away_Team'] = 'Loyola Marymount'
	if (temp.loc[i, 'Home_Team'] == 'LMU (CA)'):
		temp.loc[i, 'Home_Team'] = 'Loyola Marymount'

	# Saint Mary's (CA) -> Saint Mary's
	if (temp.loc[i, 'Away_Team'] == "Saint Mary's (CA)"):
		temp.loc[i, 'Away_Team'] = "Saint Mary's"
	if (temp.loc[i, 'Home_Team'] == "Saint Mary's (CA)"):
		temp.loc[i, 'Home_Team'] = "Saint Mary's"

	# UTRGV -> UT Rio Grande Valley
	if (temp.loc[i, 'Away_Team'] == 'UTRGV'):
		temp.loc[i, 'Away_Team'] = 'UT Rio Grande Valley'
	if (temp.loc[i, 'Home_Team'] == 'UTRGV'):
		temp.loc[i, 'Home_Team'] = 'UT Rio Grande Valley'

	# California Baptist -> Cal Baptist
	if (temp.loc[i, 'Away_Team'] == 'California Baptist'):
		temp.loc[i, 'Away_Team'] = 'Cal Baptist'
	if (temp.loc[i, 'Home_Team'] == 'California Baptist'):
		temp.loc[i, 'Home_Team'] = 'Cal Baptist'

	# Seattle U -> Seattle
	if (temp.loc[i, 'Away_Team'] == 'Seattle U'):
		temp.loc[i, 'Away_Team'] = 'Seattle'
	if (temp.loc[i, 'Home_Team'] == 'Seattle U'):
		temp.loc[i, 'Home_Team'] = 'Seattle'

temp.to_csv('temp.csv', index=False)