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
import gc

sys.path.append('../../')
from toolbox.memory_tool import MemoryTool

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

    global building_data, weather_train_data

    print '='*50+'建筑信息'+'='*50
    print building_data.info(memory_usage='deep')
    MemoryTool.memory_info_part(building_data)
    print ''
    print '='*50+'5个样本'+'='*50
    print building_data.sample(5)
    print ''
    print '='*50+'非数值特征描述'+'='*50
    print building_data.select_dtypes(include=['object']).describe()
    print ''
    print '='*50+'数值特征描述'+'='*50
    print building_data.select_dtypes(include=['int','float']).describe()
    print ''

    print '='*50+'天气(训练)信息'+'='*50
    print weather_train_data.info(memory_usage='deep')
    MemoryTool.memory_info_part(weather_train_data)
    print ''
    print '='*50+'5个样本'+'='*50
    print weather_train_data.sample(5)
    print ''
    print '='*50+'非数值特征描述'+'='*50
    print weather_train_data.select_dtypes(include=['object']).describe()
    print ''
    print '='*50+'数值特征描述'+'='*50
    print weather_train_data.select_dtypes(include=['int','float']).describe()
    print ''

    print '='*50+'内存情况'+'='*50

    memory_data = pd.read_csv('/home/helong/下载/1014/ashrae-energy-prediction/building_metadata.csv')
    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    print '-'*100
    memory_data[['building_id','site_id','square_feet','floor_count','year_built']] = memory_data[['building_id','site_id','square_feet','floor_count','year_built']].apply(pd.to_numeric,downcast='unsigned')
    memory_data.year_built = pd.to_numeric(memory_data.year_built, downcast='signed')
    memory_data.primary_use = memory_data.primary_use.astype('category')
    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    del memory_data 
    gc.collect()
    print ''

    memory_data = pd.read_csv('/home/helong/下载/1014/ashrae-energy-prediction/weather_train.csv')
    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    print '-'*100
    memory_data[['site_id']] = memory_data[['site_id']].apply(pd.to_numeric,downcast='unsigned')
    memory_data[['air_temperature','dew_temperature','precip_depth_1_hr','cloud_coverage','sea_level_pressure','wind_direction','wind_speed']] = memory_data[['air_temperature','dew_temperature','precip_depth_1_hr','cloud_coverage','sea_level_pressure','wind_direction','wind_speed']].apply(pd.to_numeric,downcast='float')

    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    del memory_data 
    gc.collect()
    print ''
    1/0

    memory_data = pd.read_csv('/home/helong/下载/1014/ashrae-energy-prediction/train.csv')
    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    print '-'*100
    memory_data[['building_id','meter','meter_reading']] = memory_data[['building_id','meter','meter_reading']].apply(pd.to_numeric,downcast='unsigned')
    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    del memory_data 
    gc.collect()
    print ''

    memory_data = pd.read_csv('/home/helong/下载/1014/ashrae-energy-prediction/test.csv')
    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    print '-'*100
    memory_data[['building_id','meter']] = memory_data[['building_id','meter']].apply(pd.to_numeric,downcast='unsigned')
    memory_data.info()
    MemoryTool.memory_info_part(memory_data)
    del memory_data 
    gc.collect()
    print ''

if __name__ == '__main__':
    main()
