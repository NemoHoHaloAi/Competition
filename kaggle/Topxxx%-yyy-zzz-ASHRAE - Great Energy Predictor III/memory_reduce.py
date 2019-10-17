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
import gc

sys.path.append('../../')
from toolbox.memory_tool import MemoryTool

import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns, sklearn

### 建筑数据
print '建筑数据'
print '初始指定类型加载'
building_data = pd.read_csv('./input/building_metadata.csv', dtype={'site_id':'uint8','building_id':'uint16','primary_use':'category','square_feet':'uint32','year_built':'float32','floor_count':'float32'})
print building_data.info(memory_usage='deep')
print '优化year_built和floor_count这两个带NaN的列，年份用0填充表示缺失，楼层同样'
building_data.year_built = building_data.year_built.fillna(0)
building_data.floor_count = building_data.floor_count.fillna(0)
building_data[['year_built','floor_count']] = building_data[['year_built','floor_count']].apply(pd.to_numeric,downcast='unsigned')
print building_data.info(memory_usage='deep')

### 天气数据
print '天气数据'
weather_train_data = pd.read_csv('./input/weather_train.csv', dtype={'site_id':'uint8','air_temperature':'float32','cloud_coverage':'float32','dew_temperature':'float32','precip_depth_1_hr':'float32','sea_level_pressure':'float32','wind_direction':'float32','wind_speed':'float32'}, parse_dates=['timestamp'], infer_datetime_format=True)
print weather_train_data.info(memory_usage='deep')
print '优化带NaN的列：air_temperature,cloud_coverage,dew_temperature,precip_depth_1_hr,sea_level_pressure,wind_direction,wind_speed'

#cloud_coverage
def downcast_with_nan(col, dc='unsigned'):
    _min = col.min()
    nan_indexs = np.isnan(col)
    col = col.fillna(_min-1)
    col = pd.to_numeric(col, downcast=dc)
    return col,nan_indexs
print weather_train_data.cloud_coverage
weather_train_data.cloud_coverage, cloud_coverate_nan_indexs = downcast_with_nan(weather_train_data.cloud_coverage)
print weather_train_data.cloud_coverage
print cloud_coverate_nan_indexs

1/0

### 读数数据
train_data = pd.read_csv('/home/helong/下载/1014/ashrae-energy-prediction/train.csv', dtype={}, parse_dates=['timestamp'], infer_datetime_format=True)

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
