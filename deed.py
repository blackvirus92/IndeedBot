import pyautogui
import webbrowser
import csv
import time

webbrowser.open('https://www.indeed.ae')
time.sleep(10)
with open('links.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		time.sleep(2)
		pyautogui.press('f6')
		pyautogui.typewrite("https://www.indeed.ae/viewjob?jk="+str(row[0]))
		print("ROW#"+row[0])
		pyautogui.press('enter')
		time.sleep(4)
		try:
			pyautogui.click(pyautogui.locateCenterOnScreen('y.png'))
			time.sleep(2)
			pyautogui.moveTo(100, 200) 
			pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
			pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
			
			try:
				time.sleep(2)
				pyautogui.click(pyautogui.locateCenterOnScreen('applycv.png'))
				pyautogui.click(pyautogui.locateCenterOnScreen('browse.png'))
				time.sleep(2)
				pyautogui.click(pyautogui.locateCenterOnScreen('find2.png'))
				pyautogui.typewrite('dj.docx') 
				time.sleep(2)
				pyautogui.press('enter')
			except:

				pass
			try:
				pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
				pyautogui.press(['down', 'down', 'down', 'down', 'down'])
				time.sleep(2)
				pyautogui.click(pyautogui.locateCenterOnScreen('x.png'))
				time.sleep(2)
				pyautogui.moveTo(100, 200) 
			except:
				pass

			for y in range(6):
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox1.png'))
					pyautogui.typewrite("2")
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox2.png'))
					pyautogui.typewrite("2")
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox3.png'))
					pyautogui.typewrite("2")
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox4.png'))
					pyautogui.typewrite("2")
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox5.png'))
					pyautogui.typewrite("2")
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox6.png'))
					pyautogui.typewrite("2")
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox7.png'))
					pyautogui.typewrite("2")
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('textbox8.png'))
					pyautogui.typewrite("2")
					time.sleep(2)
				except:
					pass
		

				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('yes1.png'))
					
				except:
					pass
				try:
					
					pyautogui.click(pyautogui.locateCenterOnScreen('yes2.png'))
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('yes3.png'))
					time.sleep(1)
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('yes4.png'))
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('yes5.png'))
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('yes6.png'))
					
				except:
					pass
				try:
					pyautogui.click(pyautogui.locateCenterOnScreen('yes7.png'))
					
				except:
					pass


			try:
				pyautogui.click(pyautogui.locateCenterOnScreen('clicker1.png'))
				pyautogui.moveTo(100, 200) 
			except:
				pass
			try:
				pyautogui.click(pyautogui.locateCenterOnScreen('clicker2.png'))
				pyautogui.moveTo(100, 200) 
			except:
				pass
			try:
				pyautogui.click(pyautogui.locateCenterOnScreen('clicker3.png'))
				pyautogui.moveTo(100, 200) 
			except:
				pass
			try:
				pyautogui.click(pyautogui.locateCenterOnScreen('clicker5.png'))
				pyautogui.moveTo(100, 200) 
			except:
				pass

#END

			try:
				pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
				pyautogui.press(['down', 'down', 'down', 'down', 'down'])
				time.sleep(4)
				pyautogui.click(pyautogui.locateCenterOnScreen('x.png'))
				time.sleep(2)
				pyautogui.moveTo(100, 200) 
			except:
				pass

			try:
				pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
				pyautogui.press(['down', 'down', 'down', 'down', 'down'])
				time.sleep(2)
				pyautogui.click(pyautogui.locateCenterOnScreen('continue2.png'))
				time.sleep(2)
				pyautogui.moveTo(100, 200) 
			except:
				pass

			try:
				pyautogui.press(['down', 'down', 'down', 'down', 'down'])
				pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
				time.sleep(2)
				pyautogui.click(pyautogui.locateCenterOnScreen('apply.png'))
				time.sleep(2)
			except:
				pass

		except:
			pass

		







