import sqlalchemy as sa
from sqlalchemy import Column, Integer, NCHAR, NVARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from enum import Enum


class ObjGroup(Enum):
    DEFAULT = 0
    BUTTON = 1
    ICON = 2
    BUFF = 3
    CARD = 4


Base = declarative_base()

class ObjTable(Base):# 列名和成员名要相同
    __tablename__ = 'obj_tab'
    id = Column('id',Integer,primary_key=True)
    obj_name = Column('obj_name',NCHAR(20))
    descr = Column('descr',NVARCHAR)
    pack = Column('pack',Integer)
    game = Column('game',NCHAR(30))

class MyDB(object):
    def __init__(self):
        self.engine=sa.create_engine('sqlite:///database/test.db?check_same_thread=False',echo=True)
        # engine = sa.create_engine('sqlite:///test.db?check_same_thread=False')

        self.metadata=sa.MetaData(self.engine)

        DBSession=sa.orm.sessionmaker(bind=self.engine)
        self.session=DBSession()

    def setup_tab(self):
        # 这里后面添加对table name的分支
        ObjTable.__table__.create(self.engine, checkfirst=True)
        item0 = {'id': 0,
                'game': None,
                'obj_name': None,
                'descr': None,
                'pack': 0,}
        self.session.add_all([ObjTable(**item0)])
        self.session.commit()

    def add_obj(self, **kwargs):
        item = {'id':-1,
                'game':None,
                'obj_name':None,
                'descr':None,
                'pack':0}
        #rows = self.session.query(ObjTable).filter_by(obj_name='it').all()
        rows = self.session.query(ObjTable.id).order_by(ObjTable.id.desc()).first()
        print(type(rows))
        id = rows.id
        print(id)
        exit()

        tmp = ObjTable(**kwargs)
        self.session.add_all([tmp])
        self.session.commit()




