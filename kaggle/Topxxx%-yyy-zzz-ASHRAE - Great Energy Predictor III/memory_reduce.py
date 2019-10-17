#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	Energy Predict DataFrame内存优化
function	xxx
author		Ho Loong
date		2019-10-17
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import sys
import os

def enviroment_init():
    """
    程序运行环境初始化
    """
    pass

def main():
    """
    程序入口
    """
    enviroment_init()

    ### step 1: int, float 考虑正负
    ### step 2: category 考虑是否太分散，如果太分散，转为category不仅不会减小，还会增加内存占用
    ### step 3: datetime, timestamp 考虑时间类型怎么处理

    ### 读取数据时指定类型：
    ### building

if __name__ == '__main__':
    main()
