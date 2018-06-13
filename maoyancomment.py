# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/5 15:22'
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import pymongo

# MONGO_URL = 'localhost'
# MONGO_DB = 'dianyingpinglun'
# MONGO_TABLE = 'pinglun'
# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / '
                      '537.36(KHTML, likeGecko) Chrome / 66.0.3359.170Safari / 537.36',
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image '
                  '/ webp, image / apng, * / *;q = 0.8',
        'Host': 'maoyan.com'
    }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None


def get_comment(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text().split(' ')[0]
    con = soup.select('.comment-content')
    path = 'E:\\PyCharmp\\PycharmProjects\\爬虫\\爬虫及算法\\image\\电影\\电影评论.txt'
    all_title = '电影:' + title + '的精彩短评'
    index = 1
    with open(path, 'a+', encoding='utf-8') as f1:
        f1.write(all_title + '\n')
        f1.close()
    for content in con:
        with open(path, 'a+', encoding='utf-8') as f2:
            content = '第' + str(index) + '条精彩短评:' + content.get_text() + '\n'
            index += 1
            f2.write(content)
            f2.close()
    print('电影:' + title + '的精彩短评已爬取完成...')


def main():
    url_list = ['http://maoyan.com/films/1203',
                'http://maoyan.com/films/1297',
                'http://maoyan.com/films/2641',
                'http://maoyan.com/films/4055',
                'http://maoyan.com/films/1247',
                'http://maoyan.com/films/267',
                'http://maoyan.com/films/123']
    for url in url_list:
        html = get_page(url)
        get_comment(html)


if __name__ == "__main__":
    main()
