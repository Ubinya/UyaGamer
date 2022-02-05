import sqlite3
from .dbutils import *
db_name = 'test_db'

class dbMgr(object):
    def __init__(self, name):
        self.conn = sqlite3.connect(name+'.db')
        self.c = self.conn.cursor()
        print('Database '+name+'.db opened!\n')

    @staticmethod
    def db_alter(op, **kargs):
        if op == "new col":
            sqlstr = new_col(kargs)
            dbMgr.db_exe(sqlstr)


    @staticmethod
    def db_op(op, **kargs):
        if op=="add item":
            sqlstr =
            dbMgr.db_exe(sqlstr)
        elif op == "del item":
            sqlstr =



    def db_exe(self, sqlstr):
        self.c.execute(sqlstr)
        self.conn.commit()


