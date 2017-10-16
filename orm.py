# -*- coding:'utf8' -*-
#encoding=utf-8
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class KvMap(Base):
    __tablename__ = 'kv_map'

    keys = Column(String(50),primary_key=True)
    key_values = Column(String(50))

class TargetSpider(Base):
    __tablename__ = 'target_spider'

    id = Column(String(50),primary_key=True)
    name = Column(String(50))
    parameter = Column(String(50))
    url = Column(String(50))
    viewType = Column(String(50))
    date = Column(String(50))
    is_second = Column(String(50))
    agg_lev = Column(String(50))
    user_bank = Column(String(50))
    regf_kind = Column(String(50))
    currency = Column(String(50))
    acctn_type = Column(String(50))
    industry = Column(String(50))
    fileName = Column(String(50))
    path = Column(String(50))
    data_rows = Column(String(50))
    data_clos = Column(String(50))
    describe = Column(String(50))
    remark1 = Column(String(50))
    remark2 = Column(String(50))
    remark3 = Column(String(50))