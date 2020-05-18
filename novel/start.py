import time
import os
import schedule

#检查是否更新
def checkUpdate():

        f = open('last_url.txt', 'r', encoding='utf-8')
        old_url = f.read()
        f.close()
        os.system("scrapy crawl url")
        #启动爬虫命令格式为:scrapy crawl *name,name为爬虫名
        f = open('last_url.txt', 'r', encoding='utf-8')
        new_url = f.read()
        f.close()
        return old_url == new_url


def download():
    if not checkUpdate():
        os.system("scrapy crawl content")
    else:
        print("\nNoUpdate\n")

def loop():
    #设置周期
    schedule.every(15).minutes.do(download)
    #every为间隔,minutes可替换为days,hours,seconds等
    while True:
        schedule.run_pending()
        #执行
        time.sleep(1)


if __name__ == '__main__':
    download()
    loop()