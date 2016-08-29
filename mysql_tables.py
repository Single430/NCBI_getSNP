#!/usr/bin/env python2.7
# coding=utf-8

import MySQLdb


class MySqlTables(object):
    """
        初始化数据库，并将数据保存大数据库中
    """

    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='xxxxxx', db='xx', host='127.0.0.1', charset="utf8", use_unicode=True)
        self.cursor_chrom = self.conn.cursor()
        # self.cursor_chrom.execute("truncate table Chromosome;")

        self.cursor_geneid = self.conn.cursor()
        # self.cursor_geneid.execute("truncate table GeneID;")

        self.cursor_func = self.conn.cursor()
        # self.cursor_func.execute("truncate table Func;")
        self.conn.commit()

    def mysql_Item(self, item, i):
        if i == 'ch':
            print 'Chromosome_item'
            # try:
            #     m[1].execute("""INSERT INTO SNP.Chromosome(SNP_ID,Chromosome)
            #            VALUES (%s,%s)""",
            #           (
            #             item['snpid'].encode('utf-8'),
            #             item['chrom'].encode('utf-8'),
            #           )
            #     )
            #     m[0].commit()
            # except MySQLdb.Error, e:
            #     print "Error %d: %s" % (e.args[0], e.args[1])
        elif i == 'fc':
            print 'Func_item'
            # try:
            #     cursor_func.execute("""INSERT INTO SNP.Func(SNP_ID,Functional_Consequence)
            #            VALUES (%s,%s)""",
            #           (
            #             item['snpid'].encode('utf-8'),
            #             item['func'].encode('utf-8'),
            #           )
            #     )
            #     conn.commit()
            # except MySQLdb.Error, e:
            #     print "Error %d: %s" % (e.args[0], e.args[1])
        elif i == 'ge':
            print 'GeneID_item'
            # try:
            #     cursor_geneid.execute("""INSERT INTO SNP.GeneID(SNP_ID,Gene_ID)
            #            VALUES (%s,%s)""",
            #           (
            #             item['snpid'].encode('utf-8'),
            #             item['gene'],
            #           )
            #     )
            #     conn.commit()
            # except MySQLdb.Error, e:
            #     print "Error %d: %s" % (e.args[0], e.args[1])
        else:
            pass
