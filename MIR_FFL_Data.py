from bs4 import BeautifulSoup
import time


errorFile = open('C:\Python27\Projects\MIR_FFL\output\ERROR-MIRData.txt','w')
outputFile = open('C:\Python27\Projects\MIR_FFL\output\MIRData.txt','w')
print('start')

def strip_html(colNum):
	if colNum == 1 :
		return col[colNum].a.string.strip()
	else:
		return col[colNum].string.strip()

print('1')

try:
##	soup = BeautifulSoup('C:\Python27\Projects\MIR_FFL\output\htmlSourceFile.txt','html.parser')
	soup = BeautifulSoup(open("C:\Python27\Projects\MIR_FFL\output\htmlSourceFile.txt"),"html.parser")

	print('2')
	
	tableStats_0 = soup.find("table", {"id" : "playertable_0"})
	tableStats_1 = soup.find("table", {"id" : "playertable_1"})
	for row in tableStats_0.findAll('tr') [3:-1]: ##first 3 rows are headers and don't need the last total row
		col = row.findAll('td')
		print('3-for')
		try:
			##name = col[0].a.string.strip()
			name = strip_html(0) ##couldn't get encode to work here. so cleanup and output are in 2 steps
			##outputFile.write(name.encode('utf-8')+'\n')
			outputFile.write(name.encode('utf-8'))
			opp = strip_html(1)
			outputFile.write(',' + opp.encode('utf-8'))
			pts = strip_html(3)
			outputFile.write(',' + pts.encode('utf-8') + '\n')
			
		except Exception as e:
			errorFile.write (str(e) + '***' + str(col) + '\n')
			print(e)
			pass
	print('4')
	for row in tableStats_1.findAll('tr') [3:-1]: ##first 3 rows are headers and don't need the last total row
		col = row.findAll('td')
		print('5-for')
		try:
			##name = col[0].a.string.strip()
			name = strip_html(0) ##couldn't get encode to work here. so cleanup and output are in 2 steps
			##outputFile.write(name.encode('utf-8')+'\n')
			outputFile.write(name.encode('utf-8'))
			opp = strip_html(1)
			outputFile.write(',' + opp.encode('utf-8'))
			pts = strip_html(3)
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


print('6')	
outputFile.close
errorFile.close

