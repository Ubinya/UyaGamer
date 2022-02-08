import sqlite3
from database.dbUtils import *
import os

db_name = 'test_db'
game_name = 'mafia'

class dbMgr(object):
    def __init__(self, name):
        self.conn = sqlite3.connect(name+'.db')
        self.c = self.conn.cursor()
        print('Database '+name+'.db opened!')

    def db_setup(self, table0):
        sqlstr = '''select count(*) FROM sqlite_master WHERE type='table' AND name = '''
        sqlstr += str2sql(table0)
        print(self.db_exe(sqlstr))
        exit()

        sqlstr = "create table "
        sqlstr += table0
        sqlstr += "(id int primary key not null);"
        self.db_exe(sqlstr)

        # 'table','col','type'
        tmp_col = {'table':game_name, 'col':'name', 'type':'varchar'}
        self.db_alter("new col", **tmp_col)
        tmp_col={'table':game_name,'col':'desc','type':'text'}
        self.db_alter("new col", **tmp_col)

    def db_alter(self, op, **kargs):
        if op == "new col":
            sqlstr = new_col(**kargs)
            self.db_exe(sqlstr)

    def db_op(self, op, **kargs):
        if op=="add item":
            sqlstr = add_item(**kargs)
            self.db_exe(sqlstr)
        # elif op == "del item":
        #     sqlstr =

    def db_exe(self, sqlstr):
        self.c.execute(sqlstr)
        self.conn.commit()
        return self.c.fetchall()

