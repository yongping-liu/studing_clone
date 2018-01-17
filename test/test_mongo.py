# encoding: utf-8
__author__ = 'zhanghe'


import sys
sys.path.append('..')
from tools.mongo import Mongodb

import time
import calendar
from datetime import datetime, timedelta, date


def time_local_to_utc(local_time):
    """
    本地时间转UTC时间
    :param local_time:
    :return:
    """
    # 字符串处理
    if isinstance(local_time, str) and len(local_time) == 10:
        local_time = datetime.strptime(local_time, '%Y-%m-%d')
    elif isinstance(local_time, str) and len(local_time) >= 19:
        local_time = datetime.strptime(local_time[:19], '%Y-%m-%d %H:%M:%S')
    elif not (isinstance(local_time, datetime) or isinstance(local_time, date)):
        local_time = datetime.now()
    # 时间转换
    utc_time = local_time + timedelta(seconds=time.timezone)
    return utc_time


def time_utc_to_local(utc_time):
    """
    UTC时间转本地时间
    :param utc_time:
    :return:
    """
    # 字符串处理
    if isinstance(utc_time, str) and len(utc_time) == 10:
        utc_time = datetime.strptime(utc_time, '%Y-%m-%d')
    elif isinstance(utc_time, str) and len(utc_time) >= 19:
        utc_time = datetime.strptime(utc_time[:19], '%Y-%m-%d %H:%M:%S')
    elif not (isinstance(utc_time, datetime) or isinstance(utc_time, date)):
        utc_time = datetime.utcnow()
    # 时间转换
    local_time = utc_time - timedelta(seconds=time.timezone)
    return local_time


db_config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'test_user'
}


test_date = [
    {
        '_id': 1,
        'id': 1,
        'name': 'Lily',
        'sex': 'F',
        'age': 20,
        'city': 'shanghai',
        'skill': ['word', 'excel']
    },
    {
        '_id': 2,
        'id': 2,
        'name': 'Tom',
        'sex': 'M',
        'age': 22,
        'city': 'shanghai',
        'skill': ['php', 'java']
    },
    {
        '_id': 3,
        'id': 3,
        'name': 'Jerry',
        'sex': 'M',
        'age': 22,
        'city': 'beijing',
        'skill': ['php', 'python']
    }
]


def test():
    try:
        table_name = 'user'
        conn = Mongodb(db_config)
        print conn.db
        print conn.find_one(table_name)
        print conn.remove(table_name)  # 清空记录
        print conn.insert(table_name, test_date)  # 插入记录
        print conn.distinct(table_name, 'age')  # 统计年龄范围
        print conn.update(table_name, {'id': 3}, {'age': 24})  # id=3的记录年龄更新为24
        print conn.distinct(table_name, 'age')  # 统计年龄范围
        conn.output_rows(table_name)
        print conn.update(table_name, {}, {'age': 1}, 'inc')  # 所有记录年龄增加1岁
        conn.output_rows(table_name)
        # print conn.update(table_name, {'id': 3}, {'skill': 'mysql'}, 'push')  # 向数组字段中添加单个元素
        # print conn.update(table_name, {'id': 3}, {'skill': 'mysql'}, 'pull')  # 向数组字段中删除单个元素
        print conn.update(table_name, {'id': 3}, {'skill': ['ruby', 'c#']}, 'pushAll')  # 向数组字段中添加多个元素
        print conn.update(table_name, {'id': 3}, {'skill': ['ruby', 'c#']}, 'pullAll')  # 向数组字段中删除多个元素
        conn.output_rows(table_name)
    except Exception, e:
        print e


def test_02():
    table_name = 'user'
    conn = Mongodb(db_config)
    print conn.db
    print conn.find_one(table_name)
    test_doc = {
        '_id': 1,
        'id': 1,
        'name': 'admin',
        'create_time': datetime.strptime('2017-07-07 08:00:00', '%Y-%m-%d %H:%M:%S'),
        'create_time_utc': time_local_to_utc('2017-07-07 08:00:00'),
        'create_time_str': '2017-07-07 08:00:00'
    }
    print conn.remove(table_name)  # 清空记录
    print conn.insert(table_name, test_doc)  # 插入记录
    print conn.find_one(table_name)
    conn.output_rows(table_name)


if __name__ == '__main__':
    # test()
    test_02()


"""
Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), u'test_user')
None
0
[1, 2, 3]
[20, 22]
1
[20, 22, 24]
**********  表名[user]  [1/3]  **********
city : shanghai
name : Lily
 sex : F
 age : 20
  id : 1
 _id : 1
**********  表名[user]  [2/3]  **********
city : shanghai
name : Tom
 sex : M
 age : 22
  id : 2
 _id : 2
**********  表名[user]  [3/3]  **********
city : beijing
name : Jerry
 sex : M
 age : 24
  id : 3
 _id : 3
3
**********  表名[user]  [1/3]  **********
city : shanghai
name : Lily
 sex : F
 age : 21
  id : 1
 _id : 1
**********  表名[user]  [2/3]  **********
city : shanghai
name : Tom
 sex : M
 age : 23
  id : 2
 _id : 2
**********  表名[user]  [3/3]  **********
city : beijing
name : Jerry
 sex : M
 age : 25
  id : 3
 _id : 3

"""
