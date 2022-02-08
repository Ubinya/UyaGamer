import sqlite3


def new_col(**kargs):
    sqlstr = '''alter table '''
    sqlstr += kargs['table']+' '
    sqlstr += '''add column '''
    sqlstr += kargs['col']+' '
    sqlstr += kargs['type']+';'
    return sqlstr


def add_item(**kargs):
    sqlstr = "insert into "
    sqlstr += kargs['table'] + ' '
    sqlstr += "values "
    sqlstr += kargs['item_tuple'] # under building
    return sqlstr


def str2sql(string):
    res = '\'' + string + '\''
    return res
