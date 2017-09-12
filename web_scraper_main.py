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

        page = 1
        # while self.scraper.self.loop_flag:
        # while page < 2:
        #
        #     print 'Page: ' + str(page)
        #     self.scraper.get_all()
        #
        #     page += 1
        #     self.scraper.url = 'https://fmovies.is/movies?page=' + str(page)
        #     # self.scraper.url = 'http://www.lazada.com.ph/shop-power-bank/?itemperpage=120&page='+ str(page) + '&sc=EeIb&searchredirect=Power+bank%3Fspm%3Da2o4l.home.0.0.0V7DGc'
        #     self.scraper.createPage()
        #     self.scraper.createContainer()

        chrome = webdriver.Chrome('C:\Python27\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
        chrome.get(self.scraper.url)
        # driver.set_window_position(0, 0)
        # driver.set_window_size(100000, 200000)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(5)  # wait to load
        #

        movie_list = chrome.find_element_by_class_name('movie-list')

        # for x in movie_list.find_elements_by_class_name('col-lg-3'):
        #     print x.get_attribute('innerHTML')

        hover_at = movie_list.find_elements_by_class_name('col-lg-3')

        for i in range(0, len(hover_at)):

            print '{' + str(i) + ')'

            hover = ActionChains(chrome).move_to_element(hover_at[i])
            hover.perform()
            time.sleep(1)

            print hover_at[i].get_attribute('innerHTML')

            cluetip = hover_at[i].find_element_by_id('cluetip-1')
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


            time.sleep(1)


if __name__ == '__main__':

    # url = 'http://www.lazada.com.ph/shop-power-bank/?itemperpage=120&page=1&sc=EeIb&searchredirect=Power+bank%3Fspm%3Da2o4l.home.0.0.0V7DGc'
    url = 'https://fmovies.is/movies'

    web_scraper = WebScraper(url)
    web_scraper.body()