from bs4 import BeautifulSoup
import time


errorFile = open('C:\Python27\Projects\MIR_FFL\output\ERROR-MIRData.txt','w')
outputFile = open('C:\Python27\Projects\MIR_FFL\output\MIRData.txt','w')
print('start')

soup = BeautifulSoup(open("C:\Python27\Projects\MIR_FFL\output\htmlSourceFile.txt"),"html.parser")

owners = soup.findAll("div", {"class" : "teamInfoOwnerData"})

try:
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
except Exception as ex:
	errorFile.write("Exception: " + str(ex))
	print(ex)
	outputFile.close
	errorFile.close


	
outputFile.close
errorFile.close

