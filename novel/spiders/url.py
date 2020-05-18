from scrapy import Request
from scrapy.spiders import Spider
from novel.items import NovelItem

#爬取最新更新的链接
class urlSpider(Spider):
    name = "url"
    start_urls = ["http://www.shuquge.com/txt/97867/index.html"]
    #本项目爬取地址,若要更换其他,请进入该网站搜索并更换start_urls

    #refresh url
    def parse(self, response):
        new_url = response.xpath("/html/body/div[4]/div[2]/div[2]/span[6]/a/@href").extract_first()

        f = open('last_url.txt','r',encoding='utf-8')
        last_url = f.read()
        if new_url != last_url:
            f.close()
            f = open('last_url.txt', 'w', encoding='utf-8')
            f.write(new_url)
            f.close()