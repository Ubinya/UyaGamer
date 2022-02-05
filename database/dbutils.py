import sqlite3


def new_col(**kargs):
    sqlstr='''alter table '''
    sqlstr+=kargs['table']+' '
    sqlstr+='''add column '''
    sqlstr+=kargs['col']+' '
    sqlstr+=kargs['type']+';'
    return sqlstr

def add_item(**kargs):
    sqlstr = '''alter table '''
    # under building
    return sqlstr