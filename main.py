#!/usr/bin/env python2.7
# coding=utf-8

import time

from get_cookie import CookieGet
from request_post import RequestPost


post_data = {
        'EntrezSystem2.PEntrez.DbConnector.Cmd': 'displaychanged',
        'EntrezSystem2.PEntrez.DbConnector.Db': 'snp',
        'EntrezSystem2.PEntrez.DbConnector.IdsFromResult': '',
        'EntrezSystem2.PEntrez.DbConnector.LastDb': 'snp',
        'EntrezSystem2.PEntrez.DbConnector.LastIdsFromResult': '',
        'EntrezSystem2.PEntrez.DbConnector.LastQueryKey': '1',
        'EntrezSystem2.PEntrez.DbConnector.LastTabCmd': '',
        'EntrezSystem2.PEntrez.DbConnector.LinkName': '',
        'EntrezSystem2.PEntrez.DbConnector.LinkReadableName': '',
        'EntrezSystem2.PEntrez.DbConnector.LinkSrcDb': '',
        'EntrezSystem2.PEntrez.DbConnector.QueryKey': '',
        'EntrezSystem2.PEntrez.DbConnector.TabCmd': '',
        'EntrezSystem2.PEntrez.DbConnector.Term': 'homo sapiens',
        'EntrezSystem2.PEntrez.Snp.Entrez_PageController.PreviousPageName': 'results',
        'EntrezSystem2.PEntrez.Snp.Snp_Facets.BMFacets': '',
        'EntrezSystem2.PEntrez.Snp.Snp_Facets.FacetSubmitted': 'false',
        'EntrezSystem2.PEntrez.Snp.Snp_Facets.FacetsUrlFrag': 'filters=',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Discovery_SearchDetails.SearchDetailsTerm': '"Homo sapiens"[Organism]',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Entrez_MultiItemSupl.RelatedDataLinks.DbName': 'snp',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Entrez_MultiItemSupl.RelatedDataLinks.rdDatabase': 'rddbto',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Entrez_Pager.CurrPage': '1',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Entrez_Pager.cPage': '1',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Entrez_Pager.cPage': '1',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.HistoryDisplay.Cmd': 'displaychanged',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.FFormat': 'DocSum',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.FFormat2': 'DocSum',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.FSort': 'SNP_ID',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.FSort2': 'SNP_ID',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.FileFormat': 'snpsum',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.FileSort': 'SNP_ID',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.Format': '',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.LastFormat': '',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.LastPageSize': '20',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.LastPresentation': 'snpsum',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.LastSort': 'SNP_ID',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.PageSize': '200',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.Presentation': 'snpsum',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.Sort': 'SNP_ID',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.sPageSize': '20',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.sPageSize2': '200',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.sPresentation': 'SnpSum',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.sPresentation2': 'SnpSum',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.sSort': 'SNP_ID',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.sSort2': 'SNP_ID',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_ResultsController.ResultCount': '164986514',
        'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_ResultsController.RunLastQuery': '',
        'p$a': 'EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Snp_DisplayBar.SetDisplay',
        'p$l': 'EntrezSystem2',
        'p$st': 'snp',
        'term': 'homo sapiens',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Host': 'www.ncbi.nlm.nih.gov',
    'Referer': 'http://www.ncbi.nlm.nih.gov/snp/?term=homo+sapiens',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ncbi_sid=396B32A67BAA1E51_0182SID;WebEnv=1Pi-NBdXC4EipdB5dUBsNQ3rrLHb6P8QQlDFNc8e_YHiVvvpJlFVUz6LIBK-Ab6jmJijKwOgv4nBPbtpr9SZ37O38WvhMy4mQjR5g%40396B32A67BAA1E51_0182SID;clicknext=;unloadnext=;prevselfurl=;ncbi_prevPHID=CE892D507BAA10E10000000000EBB1F9'
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
        post_data['EntrezSystem2.PEntrez.Snp.Snp_ResultsPanel.Entrez_Pager.CurrPage'] = str(page)
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
