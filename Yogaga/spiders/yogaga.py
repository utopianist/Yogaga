# -*- coding: utf-8 -*-
import scrapy
import re
import requests
from scrapy import Request
import logging
from scrapy import FormRequest
from pyquery import PyQuery as pq
from Yogaga.items import YogagaItem



class YogagaSpider(scrapy.Spider):
    name = 'yogaga'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'wz.yogaga.cn',
        'Referer': 'http://wz.yogaga.cn/index/user/login',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    url = 'http://wz.yogaga.cn/?page={page}'


    def start_requests(self):
        """
        login
        :return:
        """
        data = {
            'mobile': 'utopia',
            'password': '023299564b0db47d5f3e476a254d0c21',
        }
        yield FormRequest(url='http://wz.yogaga.cn/index/user/login', formdata=data, callback=self.parse, )

    def parse(self, response):
        header = response.headers['Set-Cookie'].decode('utf-8')
        cookie = re.match("(PHPSESSID=(.*?));.*", header).group(1)
        print('登陆成功！！')
        self.headers['Cookies'] = cookie
        for i in range(1,43418):
            yield Request(self.url.format(page=i), callback=self.url_parse)

    def url_parse(self, response):
        item = YogagaItem()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        doc = pq(response.text)
        tbody = doc('tbody tr').items()
        if tbody:
            for dt in tbody:
                url = dt('td:nth-child(1) a').attr('href')
                # yield Request(url, headers=headers, callback=self.article_parse, meta={'url': url})

                #测试永久链接部分
                item['url'] = url
                yield item

                #代理部分
                # request = Request(url, headers=headers, callback=self.article_parse, meta={'url': url})
                # request.meta['proxy'] = 'http://' + self.get_random_proxy()
                # yield request

    def article_parse(self, response):
        item = YogagaItem()
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text().replace("\n",""),
            'url': response.url,
            # 'date': doc('#post-date').text(),
            # 'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        if len(data['content']) > 100:
            for dt in data:
                item[dt] = data[dt]
            yield item


    def get_random_proxy(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

