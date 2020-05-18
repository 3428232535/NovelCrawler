from scrapy import Request
from scrapy.spiders import Spider
import yagmail


class contentSpider(Spider):
    name = "content"
    #name为爬虫名,必须重写
    f = open('last_url.txt', 'r', encoding='utf-8')
    start_urls = [f.read()]
    #start_urls为爬取链接为一列表,目前仅支持单链接
    def parse(self, response):
        title = response.xpath("/html/body/div[4]/div[2]/h1/text()").extract_first()
        #extract_first提取第一个符合的元素
        content = response.xpath("/html/body/div[4]/div[2]/div[2]/text()").extract()[:-2]
        #extract提取满足条件的所有元素,返回一列表,最后两行为广告故舍去
        self.f.close()
        fw = open('%s.txt'%title,'w',encoding='utf-8')
        fw.writelines(title)
        fw.writelines(content)
        fw.close()
        self.sendUpdate(title)
        #发送邮件
        item = chapterItem()
        item["title"] = title
        item["content"] = content
        yield item

    def sendUpdate(self,chapname):
        yag = yagmail.SMTP(user="3428232535@qq.com", password="xnrqqizkamhedaag", host="smtp.qq.com")
        #user为发件邮箱,host为邮箱服务器地址
        #password为密码,部分邮箱需获取stmp授权码此时密码为授权码
        yag.send(
            to="3428232535@qq.com", subject="Novel Update",
            contents="%s"%chapname, attachments='%s.txt' % chapname)
        #to为收件邮箱,可以是一个列表,subject为邮件标题
        #contents邮件正文内容,attachments为上传附件,可以是一个列表
        #可选参数:  cc抄送    bcc密件抄送