
import  requests
from  bs4 import BeautifulSoup
from lxml import etree



url = 'http://www.jianshu.com'

html = requests.get(url).text
# print(html)
# exit();
sp = BeautifulSoup(html, 'html.parser')
# print(sp)

cols = sp.find_all('div')

# print(cols)


# xpath  后面要加上/text()  =====> 取出文本内容

pathx = '/html/body/div[1]/div/div[1]/div[3]/ul/li[1]/div/a/text()'
ele = etree.HTML(html)
conreate = ele.xpath(pathx)
print(type(conreate))
for data in conreate:
    print(data)
# print(dir(ele))





