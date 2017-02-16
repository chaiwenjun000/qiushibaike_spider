import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
import re
from qiushibaike.items import QiushibaikeItem

class Myspider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    base_url = 'http://www.qiushibaike.com/hot/page/'
    def start_requests(self):
        url = self.base_url+'1'+'/'
        yield Request(url,self.parse)
    def parse(self, response):
        max_num = BeautifulSoup(response.text,'lxml').find_all('span',class_='page-numbers')[-1].get_text()
        #max_num = 35
        for i in range(1,int(max_num)+1):
            url = self.base_url + str(i)+'/'
            #print('现在是'+str(i)+'页')
            yield Request(url,callback=self.get_page,meta={'page':i})
    def get_page(self,response):
        test = BeautifulSoup(response.text,'lxml')
        #print (test.prettify())
        articles = BeautifulSoup(response.text,'lxml').find_all('div',class_='article block untagged mb15')

        print ('现在是第'+str(response.meta['page'])+'页')
        for article in articles:
            item = QiushibaikeItem()
            id = article.get('id')[11:]
            name = article.find('div',class_='author clearfix').find('h2').get_text()
            content = article.find('div',class_='content').find('span').get_text()

            agreed_number = article.find('span',class_='stats-vote').find('i').get_text()

            item['page_number'] = str(response.meta['page'])
            item['id'] = id
            item['name'] = name
            item['content'] = content
            item['agreed_number'] = agreed_number


            #print(item)
            #discuss_number =
            # print ('-----------------------------------------')
            # print('id:' + id)
            # print ('姓名: '+name.strip())
            # print ('内容: '+content.strip())
            # print ('点赞: '+agreed_number.strip())
            #
            # print('-----------------------------------------')

            yield item
            # print ('评论: '+agreed_number[1].string)




