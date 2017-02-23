from scrapy.spiders import  CrawlSpider



### 该文件名称要注意了!!


class doubanSpider(CrawlSpider):
#cmdline.execute("scrapy crawl test".split()) 这里的test 和下面的name 要一样!!
    name = 'test'
    start_urls = ['http://movie.douban.com/top250'];

    def parse(self, response):
        print(response.body)
        # filename = movie.name.com
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
        print(response.url)
        # 可以在此处断点 调试
        a = 1
        b = 2

