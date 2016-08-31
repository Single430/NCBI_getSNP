#!/usr/bin/env python2.7
# coding=utf-8

import time

from get_cookie import CookieGet
from request_post import RequestPost


post_data = {
        # 各种post数据，自行填写
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Host': 'www.ncbi.nlm.nih.gov',
    'Referer': 'http://www.ncbi.nlm.nih.gov/xx/?term=xxxxx',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '必须有'
}


def main():
    """
        主函数
    """
    page_f = open('page.txt', 'r')
    start_page = 0
    for i in page_f:
        start_page = int(i.strip())+1
    if start_page == 0:
        start_page = 1
    print start_page

    cookieData = CookieGet()
    requestPost = RequestPost()

    for page in xrange(start_page, 824933):
        print '=======Page:%d======='%page
        if (page%4000 == 0) | (page == start_page):
            headers['Cookie'] = cookieData.cookie_Get()
        post_data['xxxxxxxxxxx'] = str(page)
        print 'download -> item'
        requestPost.parse_post(page, post_data, headers, (page-1)*200)
        print '.'
        time.sleep(1)
        print '..'
        time.sleep(1)
        print '...'
        time.sleep(1)
        print '....'
        time.sleep(1)
        print '.....'
        time.sleep(1)
        print '......'


if __name__ == '__main__':
    """
        main.py
    """
    print '--------------Start----------------'
    main()
