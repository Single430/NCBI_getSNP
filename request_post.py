#!/usr/bin/env python2.7
# coding=utf-8

import codecs

import requests
import scrapy
from scrapy.selector import Selector

from mysql_tables import MySqlTables


class SnpItem(scrapy.Item):
    xx = scrapy.Field()
    xpurl = scrapy.Field()
    xxxx = scrapy.Field()
    xx = scrapy.Field()
    xx = scrapy.Field()
    pass


class RequestPost(object):
    """
        实现对网页数据的获取并将数据保存到数据库中
    """

    def __init__(self):
        self.item = SnpItem()

    def parse_post(self, page, post_data, headers, number):
        mysql_Table = MySqlTables()
        print 'loading...'
        global retrun_data, status, isok, genef, snid
        try:
            retrun_data = requests.post('http://www.ncbi.nlm.nih.gov/x/?term=xxx',
                                        data=post_data, headers=headers, timeout=20)

            print 'See status'
            status = int(retrun_data.status_code)
            print status
            if status == 200:
                sel = Selector(text=retrun_data.text)

                # 主要部分不贴出了
                # 这里记得要入数据库或者保存本地

                print '\n===========%d Page: %d===========' % (page, page*200)
                page_f = codecs.open('page.txt', 'wb', 'utf-8')  # 其中的page.txt是保存了当前页数的文件，初始内容应该写为0
                page_f.write(str(page))
                print '=============Write Success============='

            else:
                print 'Error restart'
                self.parse_post(page, post_data, headers, number)

        except Exception, e:
            print 'Restart', e
            self.parse_post(page, post_data, headers, number)
