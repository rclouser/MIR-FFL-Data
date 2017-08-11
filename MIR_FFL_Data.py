from bs4 import BeautifulSoup
import urllib2
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


errorFile = open('C:\Python27\Projects\MIR_FFL\output\ERROR-MIRData.txt','w')
outputFile = open('C:\Python27\Projects\MIR_FFL\output\MIRData.txt','w')
driver = webdriver.Chrome('C:\Google\Chromedriver\chromedriver_win32\chromedriver.exe') 
year = 2007
periodID = 1
print('start')
try:
	driver.get("http://games.espn.go.com/ffl/signin")
	#implement wait it is mandatory in this case
	WebDriverWait(driver,1000).until(EC.presence_of_all_elements_located((By.XPATH,"(//iframe)")))
	frms = driver.find_elements_by_xpath("(//iframe)")
	time.sleep(5)
	driver.switch_to_frame(frms[1])
	driver.find_element_by_xpath("(//input)[1]").send_keys("######")
	driver.find_element_by_xpath("(//input)[2]").send_keys("#######")
	driver.find_element_by_class_name("btn-submit").click()
	driver.switch_to_default_content()
	time.sleep(10)
	print('1')	
	while periodID < 17:
		teamID = 1
		while teamID < 12:
			url = 'http://games.espn.com/ffl/boxscorequick?leagueId=44549&teamId=' + teamID + '&scoringPeriodId=' + '&seasonId=' + year + '&view=scoringperiod&version=quick'
			driver.get(url)
			time.sleep(10)


			soup = BeautifulSoup(driver.page_source,"html.parser")

			owners = soup.findAll("div", {"class" : "teamInfoOwnerData"})

			for index,val in enumerate(owners):	
				print(index)
				print(owners[index])
				tableID = 'playertable_' + str(index)
				print(tableID)
				tableStats = soup.find("table", {"id" : tableID})
				for row in tableStats.findAll('tr') [3:-1]: ##first 3 rows are headers and don't need the last total row
					col = row.findAll('td')
					try:
						owner = owners[index].string.strip()
						outputFile.write(owner.encode('utf-8'))
						
						name = col[0].string.strip()
						outputFile.write(',' + name.encode('utf-8'))
						
						opp = col[1].a.string.strip()
						outputFile.write(',' + opp.encode('utf-8'))
						
						pts = col[3].string.strip()
						outputFile.write(',' + pts.encode('utf-8') + '\n')				
					except Exception as e:
						errorFile.write (str(e) + '***' + str(col) + '\n')
						print(e)
						pass
			teamID = teamID + 2			
		periodID = periodID + 1				
except Exception as ex:
	errorFile.write("Exception: " + str(ex))
	print(ex)
	outputFile.close
	errorFile.close
	driver.close


	
outputFile.close
errorFile.close
driver.close
