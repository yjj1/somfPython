# encoding=utf-8
#2017-09-01
# step2 Connect to Db to get what excel needs to download

import mysql.connector
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy.ext.declarative import declarative_base
import requests
from orm import KvMap, TargetSpider
import datetime
# Base = declarative_base()
# class KvMap(Base):
#     __tablename__ = 'kv_map'
#
#     keys = Column(String(50),primary_key=True)
#     key_values = Column(String(50))
#
# class TargetSpider(Base):
#     __tablename__ = 'target_spider'
#
#     id = Column(String(50),primary=True)
#     name = Column(String(50))
#     parameter = Column(String(50))
#     url = Column(String(50))
#     viewType = Column(String(50))
#     date = Column(String(50))
#     is_second = Column(String(50))
#     agg_lev = Column(String(50))
#     user_bank = Column(String(50))
#     regf_kind = Column(String(50))
#     currency = Column(String(50))
#     acctn_type = Column(String(50))
#     industry = Column(String(50))
#     fileName = Column(String(50))
#     path = Column(String(50))
#     data_rows = Column(String(50))
#     data_clos = Column(String(50))

#Global Info

global kvData

#DataBase Connect
def dbConnect() :
    db_url = 'mysql+pymysql://root:test@192.168.1.108:3306/charge_db?charset=utf8'
    engine = create_engine(db_url, echo=True)
    # metaData=MetaData(engine)
    DBSession = sessionmaker(bind=engine)
    global session
    session = DBSession()
    list = session.query(KvMap).filter()

    for kvData in list:
        print 'type:',type(kvData)
        print 'value:', kvData.key_values


    spiderData = session.query(TargetSpider).filter(TargetSpider.id=='1').one()
    print spiderData.name


#从数据库获取经管报表登录账号
def getChargeAccount():
    getValue('account')
    return kvData.key_values

#从数据库获取经管报表登录密码
def getChargePassword():
    getValue('password')
    return kvData.key_values

#通过Key获取Value
def getValue(key):
    kvData = session.query(KvMap).filter(KvMap.Keys==key).one()
    return kvData.key_values

#登录获取session、cookie等数据
def login():
    login_url='https://154.211.26.40/rcubbi_web/logon'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    httpSession = requests.session()
    data = {
        'loginName':getChargeAccount(),
        'password':getChargePassword()
    }

    resp = httpSession.post(login_url, data=data, headers=headers)
    # get refer,host,cookie,session

# def askDownload():

#从数据库中读取数据请求：需要查询的数据列表
def getAskFromData():
    targetSpiderList = session.query(TargetSpider).filter()
    for targetSpider in targetSpiderList:
        askUrl = targetSpider.url

def getAskFromDbForTest(id):
    #date
    curDateTime = datetime.datetime.now()
    date = bytes(curDateTime.year) \
           + '-' + bytes(curDateTime.month) \
           + '-' +bytes(curDateTime.day)
    print date

    #header
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

    spiderData = session.query(TargetSpider).filter(TargetSpider.id == id).one()
    askUrl = "http://154.211.26.40" + spiderData.url

    data = {
        'date' : date,
        'viewType' : spiderData.viewType,
        'is_second' : spiderData.is_second,
        'agg_lev' : spiderData.agg_lev,
        'user_bank' : spiderData.user_bank,
        'regf_kind' : spiderData.regf_kind,
        'currency' : spiderData.currency,
        'industry' : spiderData.industry,
    }

    httpSession = requests.session()
    resp = httpSession.post(askUrl, data=data, header=headers)

if __name__ == "__main__":
    dbConnect()
    getAskFromDbForTest('1')