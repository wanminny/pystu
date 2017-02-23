

from scrapy.spiders import  CrawlSpider



### 该文件名称要注意了!!


class doubanSpider(CrawlSpider):
#cmdline.execute("scrapy crawl test".split()) 这里的test 和下面的name 要一样!!
    name = 'entry'
    start_urls = ['http://www.sina.com'];

    def parse(self, response):
        # print(response.body)
        # filename = response.url.split("/")[-2]
        # open(filename, 'wb').write(response.body)
        print(response.url)
        a = 1
        b = 2



