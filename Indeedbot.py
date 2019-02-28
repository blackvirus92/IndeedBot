from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import webbrowser
import pyautogui



class IndeedBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()
	def CloseBorwser(self):
		self.driver.close()

	def login(self):
		driver = self.driver
		
	def apply_job(self, jobtitle):
		print("Process Start..")
		try:
			driver = self.driver
			driver.get("https://www.indeed.ae/m/jobs?q="+jobtitle+"+&l=Dubai&from=searchOnSerp")
			for xx in range(1000):
			#searching for links
				csv_file = open('links.csv','a')
				csv_writer = csv.writer(csv_file)
				hrefs = driver.find_elements_by_xpath("//*[@href]")

				for ii in hrefs:
					try:
						link = str(ii.get_attribute('href'))
						link2 = link.split("jk=")[1]
						csv_writer.writerow([link2])
					except:
						pass
				driver.find_element_by_link_text("Next").click()
			
		except:
			print("Scraping Complete!")
			driver.close()
			csv_file.close()
			pass	
		
		time.sleep(4)
blackIndeed = IndeedBot("djaydequina92@gmail.com", "Dequina761")
blackIndeed.login()
blackIndeed.apply_job("Office Assistant")



