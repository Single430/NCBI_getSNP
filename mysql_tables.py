#!/usr/bin/env python2.7
# coding=utf-8

import MySQLdb


class MySqlTables(object):
    """
        初始化数据库，并将数据保存大数据库中
    """

    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='xxxxxx', db='xx', host='127.0.0.1', charset="utf8", use_unicode=True)
        self.cursor_xxx = self.conn.cursor()
        # self.cursor_chrom.execute("truncate table Chromosome;")

        self.cursor_x = self.conn.cursor()
        # self.cursor_geneid.execute("truncate table GeneID;")

        self.cursor_xx = self.conn.cursor()
        # self.cursor_func.execute("truncate table Func;")
        self.conn.commit()

    def mysql_Item(self, item, i):
        if i == 'ch':
            print 'xx'
            # try:
            #     m[1].execute("""INSERT INTO xx.xx(xx,xx)
            #            VALUES (%s,%s)""",
            #           (
            #             item['xx'].encode('utf-8'),
            #             item['xx'].encode('utf-8'),
            #           )
            #     )
            #     m[0].commit()
            # except MySQLdb.Error, e:
            #     print "Error %d: %s" % (e.args[0], e.args[1])
        elif i == 'fc':
            print 'xx'
            # 同上
        elif i == 'ge':
            print 'xx'
           # 同上
        else:
            pass
