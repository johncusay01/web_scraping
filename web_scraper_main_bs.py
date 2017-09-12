from datetime import datetime
from threading import Timer
from web_scraper_func import Scraper
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import time


# query the website and return the html to the variable ?page?
# page = urllib2.urlopen(url)
#
# soup = BeautifulSoup(page, 'html.parser')

class WebScraper():

    def __init__(self, url):

        self.scraper = Scraper(url)

    def body(self):

        # self.scraper.get_all()
        self.scraper.createPage()
        self.scraper.createContainer()
        # pages = self.scraper.get_pages()
        # print pages
        page = 1
        # while self.scraper.loop_flag:
        while page < 10:

            print 'Page: ' + str(page)
            self.scraper.get_all()

            page += 1
            # self.scraper.url = 'http://www.lazada.com.ph/shop-power-bank/?itemperpage=120&page='+ str(page) + '&sc=EeIb&searchredirect=Power+bank%3Fspm%3Da2o4l.home.0.0.0V7DGc'
            self.scraper.createPage()
            self.scraper.createContainer()

if __name__ == '__main__':

    url = 'http://www.lazada.com.ph/shop-power-bank/?itemperpage=120&page=1&sc=EeIb&searchredirect=Power+bank%3Fspm%3Da2o4l.home.0.0.0V7DGc'


    web_scraper = WebScraper(url)
    web_scraper.body()