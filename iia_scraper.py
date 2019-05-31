from bs4 import BeautifulSoup
from time import sleep
import csv
# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/akashrao96/chromedriver_linux64/chromedriver") # if you want to use chrome, replace Firefox()    with Chrome()
driver.get("http://www.iiaonline.in/memberdirectory.aspx") # load the web page
#search_begin = driver.find_element_by_xpath("//*[@id='Assessor']/div/div[2]/a/i").click()
# for websites that need you to login to access the information
#elem = driver.find_element_by_id("unit") # Find the email input field of the login form
#elem.send_keys("Agra") # Send the users email
sleep(1)
search_exeute = driver.find_element_by_xpath("//*[@type='button']").click()
sleep(40)


f = open('output.csv', 'w')

Sr_No=""
Menber_Id=""
Unit_Name=""
COntact=""
Chapter=""
Category=""

#print(table)


number_of_pages = 161
for page in range(number_of_pages - 1):
    list_of_rows = []
    src = driver.page_source # gets the html source of the page
    parser = BeautifulSoup(src,'html.parser') # initialize the parser and parse the source "src"
    sleep(1)
    table = parser.find("table") # A list of attributes that you want to check in a tag)
    sleep(1)
    for row in table.find_all('tr')[:]:
        list_of_cells = []
        for cell in row.find_all('td'):
            text = cell.text.replace("&nbsp;", "")
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
        writer=csv.writer(f)
        writer.writerow(list_of_cells)
    driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()
    sleep(1)
        
        

print (list_of_rows)
f.close()

driver.close() # closes the driver ?>
