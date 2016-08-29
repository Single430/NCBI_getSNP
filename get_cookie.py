#!/usr/bin/env python2.7
# coding=utf-8

import time

from selenium import webdriver


class CookieGet(object):
    def __init__(self):
        pass

    def cookie_Get(self):
        """
            获得cookie，防止post中cookie过期
        """
        global cookieData, cookieList
        print '======================== Get Cookie==========================='
        url = 'http://www.ncbi.nlm.nih.gov/snp/?term=homo+sapiens'
        browser = webdriver.Firefox()
        browser.set_window_size(800, 600)
        try:
            print 'browser.get(url)'
            browser.get(url)

            try:
                print 'click'
                time.sleep(1)
                browser.find_element_by_id("EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.Display").click()
                time.sleep(1)
                browser.find_element_by_id("ps200").click()
                time.sleep(1)
                browser.find_element_by_xpath('//div[@id="display_settings_menu"]/button').click()

                print 'Start get cookie'
                try:
                    cookieList = browser.get_cookies()

                    print 'Get cookie success'
                    # print cookieList
                    cookieData = ';'.join(cook['name'] + '=' + cook['value'] for cook in cookieList)
                    print cookieData
                    print len(cookieData)
                    browser.close()
                    return cookieData

                except:
                    print "Get failed"
                    browser.close()
                    self.cookie_Get()

            except:
                print '=======PS200 ERROR======='
                browser.close()
                self.cookie_Get()

        except:
            print '=======Browser Get ERROR======='
            browser.close()
            self.cookie_Get()
