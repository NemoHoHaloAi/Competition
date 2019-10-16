#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	Great Energy Predictor Analysis
function	xxx
author		Ho Loong
date		2019-10-16
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import sys,os

import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns, sklearn

building_data = pd.read_csv('./input/building_metadata.csv')
weather_train_data = pd.read_csv('./input/weather_train.csv')

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

    print '='*50+'建筑信息'+'='*50
    print building_data.info()
    print ''
    print '='*50+'5个样本'+'='*50
    print building_data.sample(5)
    print ''
    print '='*50+'建筑用途所有取值'+'='*50
    print building_data.primary_use.unique()
    print ''
    print '='*50+'数值特征描述'+'='*50
    print building_data.describe()
    print ''

    print '='*50+'天气(训练)信息'+'='*50
    print weather_train_data.info()
    print ''
    print '='*50+'5个样本'+'='*50
    print weather_train_data.sample(5)
    print ''
    print '='*50+'数值特征描述'+'='*50
    print weather_train_data.describe()
    print ''

if __name__ == '__main__':
    main()
