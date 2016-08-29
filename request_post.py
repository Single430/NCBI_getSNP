#!/usr/bin/env python2.7
# coding=utf-8

import codecs

import requests
import scrapy
from scrapy.selector import Selector

from mysql_tables import MySqlTables


class SnpItem(scrapy.Item):
    snpid = scrapy.Field()
    snpurl = scrapy.Field()
    chrom = scrapy.Field()
    gene = scrapy.Field()
    func = scrapy.Field()
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
            retrun_data = requests.post('http://www.ncbi.nlm.nih.gov/snp/?term=homo+sapiens',
                                        data=post_data, headers=headers, timeout=20)

            print 'See status'
            status = int(retrun_data.status_code)
            print status
            if status == 200:
                sel = Selector(text=retrun_data.text)

                for i in range(1, 201):
                    print '=======%d============='%(i)
                    sn = sel.xpath('//div[%d][@class="rprt"]/div[@class="rslt"]/div[@class="supp"]/span//text()' % i).extract()
                    try:
                        snid = sn[0]

                        try:
                            snid,snid1 = ''.join(snid).split(' ',1)
                            snid = ''.join(snid)
                            self.item['snpid'] = snid
                        except:
                            self.item['snpid'] = snid

                        self.item['snpurl'] = 'http://www.ncbi.nlm.nih.gov' + ''.join(sel.xpath('//div[%d][@class="rprt"]/div[@class="rslt"]/div[@class="supp"]/span/a/@href' % i).extract())
                        sc = sel.xpath('//div[%d][@class="rprt"]/div[@class="rslt"]/div[@class="supp"]/dl' % i)

                        scc = sc.xpath('./dt[1]/text()').extract()
                        scc = ''.join(scc)
                        scc = scc.strip()
                        if scc == 'Chromosome:':
                            self.item['chrom'] = ''.join(sc.xpath('./dd[1]/text()').extract())
                        elif scc == 'Gene:':
                            genef = sc.xpath('./dd[1]/a/@href').extract()
                        elif scc == 'Functional Consequence:':
                            self.item['func'] = ''.join(sc.xpath('./dd[1]/text()').extract())
                        else:
                            self.item['chrom'] = 'NULL'

                        scc = sc.xpath('./dt[2]/text()').extract()
                        scc = ''.join(scc)
                        scc = scc.strip()
                        if scc == 'Gene:':
                            genef = sc.xpath('./dd[2]/a/@href').extract()
                        elif scc == 'Functional Consequence:':
                            self.item['func'] = ''.join(sc.xpath('./dd[2]/text()').extract())
                        else:
                            genef = 'NULL'

                        scc = sc.xpath('./dt[3]/text()').extract()
                        scc = ''.join(scc)
                        scc = scc.strip()
                        if scc == 'Functional Consequence:':
                            self.item['func'] = ''.join(sc.xpath('./dd[3]/text()').extract())
                        else:
                            self.item['func'] = 'NULL'

                        print 'download -> GeneID_table'
                        if genef != 'NULL':
                            for gen in genef:
                                gen0,gen1 = ''.join(gen).split('=', 1)
                                self.item['gene'] = int(gen1)
                                # GeneID_item(item)
                                mysql_Table.mysql_Item(self.item, 'ge')
                                print self.item['snpid'], ':', self.item['gene']
                        else:
                            self.item['gene'] = 0
                            # GeneID_item(item)
                            mysql_Table.mysql_Item(self.item, 'ge')
                            print self.item['snpid'], ':', self.item['gene']

                        print 'download -> Chromosome_table'
                        print self.item['snpid'], ':', self.item['chrom']
                        # Chromosome_item(item)
                        mysql_Table.mysql_Item(self.item, 'ch')

                        print 'download -> Func_table'
                        print self.item['snpid'], ':', self.item['func'].strip()
                        func = self.item['func']
                        func = ''.join(func).split(',')
                        for fun in func:
                            self.item['func'] = fun.strip()
                            # Func_item(item)
                            mysql_Table.mysql_Item(self.item, 'fc')
                    except:
                        print '????????????' # 这里的错误判断不全面，还在测试当中
                        pass

                print '\n===========%d Page: %d===========' % (page, page*200)
                page_f = codecs.open('page.txt', 'wb', 'utf-8')
                page_f.write(str(page))
                print '=============Write Success============='

            else:
                print 'Error restart'
                self.parse_post(page, post_data, headers, number)

        except Exception, e:
            print 'Restart', e
            self.parse_post(page, post_data, headers, number)
