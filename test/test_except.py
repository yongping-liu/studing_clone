#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_except.py
@time: 16-4-13 下午6:38
"""

import time
import traceback


def test_01():
    try:
        # raise Exception('error_message')
        raise Exception('error_message', 'error_code')
    except Exception as e:
        # 打印异常
        print type(e), e

        time.sleep(0.1)

        # 打印异常消息
        print type(e.message), e.message

        time.sleep(0.1)

        # 打印异常参数
        print e.args, type(e.args[0]), e.args[0]

        time.sleep(0.1)

        # 打印异常堆栈跟踪信息 stack traceback
        traceback.print_exc()


def test_02():
    try:
        print u'try'
        raise Exception(u'try')
    except Exception as e:
        print u'except'
        raise Exception(u'except')
    finally:
        print u'finally'


if __name__ == '__main__':
    test_02()
