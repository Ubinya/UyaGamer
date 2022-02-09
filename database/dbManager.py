import sqlalchemy as sa
from sqlalchemy import Column, Integer, NCHAR, NVARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Obj1(Base):
    __tablename__ = 'mafia'
    id = Column('id',Integer,primary_key=True)
    obj_name = Column('obj_name',NCHAR(20))
    desc = Column('desc',NVARCHAR)
    #group = Column('group',Integer)


class MyDB(object):
    def __init__(self):
        self.engine=sa.create_engine('sqlite:///database/test.db?check_same_thread=False',echo=True)
        # engine = sa.create_engine('sqlite:///test.db?check_same_thread=False')

        self.metadata=sa.MetaData(self.engine)

        DBSession=sa.orm.sessionmaker(bind=self.engine)
        self.session=DBSession()

    def create_tab(self, table_name):
        # 这里后面添加对table name的分支
        Obj1.__table__.create(self.engine, checkfirst=True)

    def add_item(self, table_name, **kwargs):
        tmp = Obj1(**kwargs)
        self.session.add_all([tmp])
        self.session.commit()




