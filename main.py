Import requests
import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome("chromedriver.exe", options = options)
driver.get("https://www.etoro.com/discover/markets/stocks/exchange/london")

soup = BeautifulSoup(driver.page_source, 'html.parser')

soup = BeautifulSoup(driver.page_source, 'html.parser')
section = soup.find_all("a", attrs = {"class" : "price"})
firms = []
section2 = soup.find( class_ = "price" )
for i in range(len(section)):
    firms.append(section[i]["href"].split("/")[2])
    print(section[i]["href"].split("/")[2])
