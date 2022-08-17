from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get("https://www.etoro.com/markets/btc")
for x in range(1, 10):
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    gold = soup.find_all('div', {'class': 'head-info-stats-content ng-star-inserted'})
    print(gold[0].get_text().split(" ")[1])
    print(gold[0].contents[0].get_text())
    #wait for 10 seconds
    # driver.closE()