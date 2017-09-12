import urllib2
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import os
import xlwt

class Scraper():

    def __init__(self, url):

        self.url = url
        self.loop_flag = True

        self.file = 'Lazada_output.xls'

        try:
            os.remove(self.file)
        except OSError:
            pass

        self.book = xlwt.Workbook()
        self.sh = self.book.add_sheet('Sheet 1', cell_overwrite_ok=True)
        self.sh.write(0, 0, 'Item Name')
        self.sh.write(0, 1, 'Item Price')
        self.row = 2


    def createPage(self):

        self.page = requests.get(self.url)



    def createContainer(self):

        self.soup = BeautifulSoup(self.page.text, 'html.parser')

        #Lazada
        self.container = self.soup.find_all('div', attrs={
            'data-tracking': 'product-card'},
                                       limit=None)

        if len(self.container) == 0:
            self.loop_flag = False

    def find_data_name(self, content):

        # Lazada
        content = content.find('div', attrs={'class': 'c-product-card__description'})
        content = content.find('a', attrs={'class': 'c-product-card__name'})
        model_name = content.text.strip()
        print 'Model: ' + model_name
        return model_name

    def find_data_price(self, content):

        content = content.find('div', attrs={'class': 'c-product-card__price-block'})
        content = content.find('span', attrs={'class': 'c-product-card__price-final'})
        model_price = content.text.strip()
        print 'Model: ' + model_price
        return model_price

    def get_pages(self):

        _page = self.soup.find_all('div', attrs={
            'class': 'c-paging__wrapper'},
                                       limit=None)

        print _page

        _page_ = _page.find('a', attrs={
            'class': 'c-paging__link'})

        last_page = _page_[(len(_page_) - 1)].text.strip()

        print last_page

        return last_page

    def get_all(self):

        print len(self.container)
        i = 1
        for content in self.container:
            print '{' + str(i) + '}'
            name = self.find_data_name(content)
            price = self.find_data_price(content)
            print '\n'

            self.importToFile(self.row, name, price)
            self.row += 1
            i += 1

        self.book.save(self.file)

    def importToFile(self, row, name, price):

        name = name.encode('utf-8').strip()
        price = price[1:].encode('utf-8').strip()

        # self.writer.writerow([name, price])

        self.sh.write(row, 0, name)
        self.sh.write(row, 1, price)

        # with open('test_output.csv', 'a') as csv_file:
        #     writer = csv.writer(csv_file)
        #     writer.writerow([name, price, datetime.now()])