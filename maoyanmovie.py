# -*- coding:utf-8 -*-
__author__ = 'youjia'
__date__ = '2018/6/4 17:30'
import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

headers = {
    "Accept": "text/plain, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) " \
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.27" \
                  "85.104 Safari/537.36",
    "Content-Type": "text/html;charset=utf-8"
}


def getHtml(url):
    global headers
    try:
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            return page.text
        return None
    except RequestException:
            return None


def getList(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)'
                         '</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)'
                         '</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6],

        }


def write_to_file(content):
    path = 'E:\\PyCharmp\\PycharmProjects\\爬虫\\爬虫及算法\\image\\电影\\电影.txt'
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        # 写入本地的时候的编码
        f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset*10)
    html = getHtml(url)
    for lis in getList(html):
        # write_to_file(lis)
        print(lis)


if __name__ == "__main__":
    for i in range(10):
        main(i)
    # 进程池
    # pool = Pool()
    # pool.map(main, [i*10 for i in range(10)])
