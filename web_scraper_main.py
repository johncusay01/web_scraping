from datetime import datetime
from threading import Timer
from web_scraper_func import Scraper
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import time
from xlwt.ExcelFormulaLexer import true_pattern


# query the website and return the html to the variable ?page?
# page = urllib2.urlopen(url)
#
# soup = BeautifulSoup(page, 'html.parser')

class WebScraper():

    def __init__(self, url):

        self.scraper = Scraper(url)
        self._cont = True

    def getLastPage(self, url):

        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        _page = soup.find('ul', attrs={
        'class': 'pagination'},
                                   limit=None)
        
        _page_list = _page.find_all
        
        pass

    def getData(self, movie_list, driver):


        hover_at = movie_list.find_elements_by_class_name('col-lg-3')

        if len(hover_at) == 0:
            self._cont = False

        for i in range(0, len(hover_at)):

            print '{' + str(i) + ')'
            print hover_at[i].get_attribute('innerHTML')
            
            hover = ActionChains(driver).move_to_element(hover_at[i])
            hover.perform()
            time.sleep(1)


            cluetip = driver.find_element_by_id('cluetip-1')
            cluetip_o = cluetip.find_element_by_class_name('cluetip-outer')
            cluetip_i = cluetip_o.find_element_by_class_name('cluetip-inner')

            inner_ = cluetip_i.find_element_by_class_name('title')
            inner = inner_.find_element_by_xpath('//*[@id="cluetip-1"]/div[1]/div[2]/div/div[2]/h1')
            title = inner.get_attribute('innerHTML')

            inner = inner_.find_element_by_xpath('//*[@id="cluetip-1"]/div[1]/div[2]/div/div[2]/span')
            year = inner.get_attribute('innerHTML')

            country_ = cluetip_i.find_element_by_xpath('//*[@id="cluetip-1"]/div[1]/div[2]/div/div[4]')
            country = country_.find_element_by_xpath('//*[@id="cluetip-1"]/div[1]/div[2]/div/div[4]/a')
            country = country.get_attribute('innerHTML')

            genre_ = cluetip_i.find_element_by_xpath('//*[@id="cluetip-1"]/div[1]/div[2]/div/div[5]')
            genre = genre_.find_element_by_xpath('//*[@id="cluetip-1"]/div[1]/div[2]/div/div[5]/a[1]')
            genre = genre.get_attribute('innerHTML')

            stars_ = cluetip_i.find_element_by_xpath('//*[@id="cluetip-1"]/div[1]/div[2]/div/div[6]')
            stars = stars_.get_attribute('innerText')[7:]

            inner = cluetip_i.find_element_by_class_name('desc')
            desc = inner.get_attribute('innerHTML')
            div = cluetip_i.get_attribute('innerHTML')

            print 'Title: ' + title
            print 'Year: ' + year
            print 'Description: ' + desc
            print 'Country: ' + country
            print 'Genre: ' + genre
            print 'Stars: ' + stars

            movie_list = driver.find_element_by_class_name('widget-title')
            hover_ = ActionChains(driver).move_to_element(movie_list)
            hover_.perform()
            time.sleep(1)

    def body(self):

        self.scraper.createPage()
        self.scraper.createContainer()

        

        #=======================================================================
        # chrome = webdriver.Chrome('C:\Python27\selenium\webdriver\chrome\chromedriver')
        # chrome.get(self.scraper.url)
        #=======================================================================



        page = 490
        while self._cont:
            
            url = self.scraper.url + str(page)
            chrome = webdriver.Chrome('C:\Python27\selenium\webdriver\chrome\chromedriver')
            chrome.get(url)
            chrome.set_window_size(1000, 1000)
            
            #===================================================================
            # try:
            #     movie_list = chrome.find_element_by_class_name('movie-list')
            # except:
            #     break            
            #===================================================================
            print '{' + str(page) + '}'
            movie_list = chrome.find_element_by_class_name('movie-list')
            self.getData(movie_list, chrome)
            chrome.quit()
            page += 1

if __name__ == '__main__':

    # url = 'http://www.lazada.com.ph/shop-power-bank/?itemperpage=120&page=1&sc=EeIb&searchredirect=Power+bank%3Fspm%3Da2o4l.home.0.0.0V7DGc'
    url = 'https://fmovies.is/movies?page='

    web_scraper = WebScraper(url)
    web_scraper.body()