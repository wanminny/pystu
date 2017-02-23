
from scrapy import cmdline

# 注意这里的名字和后面spiders目录中的name  要一样否则 会报错哦 找了半天才明白偶~~~~


# 测试OK!


cmdline.execute("scrapy crawl test".split())


print(1111)