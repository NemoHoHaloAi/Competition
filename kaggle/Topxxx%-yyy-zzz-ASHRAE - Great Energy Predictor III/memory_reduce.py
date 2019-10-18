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
building_data = pd.read_csv('./input/building_metadata.csv', dtype={'site_id':'uint8','building_id':'uint16','primary_use':'category','square_feet':'uint32','year_built':'float32','floor_count':'float32'})
building_data.info(memory_usage='deep')

# print '优化year_built和floor_count这两个带NaN的列，年份用0填充表示缺失，楼层同样'
# building_data.year_built = building_data.year_built.fillna(0)
# building_data.floor_count = building_data.floor_count.fillna(0)
# building_data[['year_built','floor_count']] = building_data[['year_built','floor_count']].apply(pd.to_numeric,downcast='unsigned')
# print building_data.info(memory_usage='deep')
print ''

### 天气数据
print '天气数据'
# weather_train_data = pd.read_csv('./input/weather_train.csv', dtype={'site_id':'uint8','air_temperature':'float32','cloud_coverage':'float32','dew_temperature':'float32','precip_depth_1_hr':'float32','sea_level_pressure':'float32','wind_direction':'float32','wind_speed':'float32'}, parse_dates=['timestamp'], infer_datetime_format=True)
weather_train_data = pd.read_csv('./input/weather_test.csv', dtype={'site_id':'uint8','air_temperature':'float32','cloud_coverage':'float32','dew_temperature':'float32','precip_depth_1_hr':'float32','sea_level_pressure':'float32','wind_direction':'float32','wind_speed':'float32'}, parse_dates=['timestamp'], infer_datetime_format=True)
weather_train_data.info(memory_usage='deep')

# print '优化带NaN的列：air_temperature,cloud_coverage,dew_temperature,precip_depth_1_hr,sea_level_pressure,wind_direction,wind_speed'
# #cloud_coverage
# def downcast_with_nan(col, dc='unsigned'):
#     _min = col.min()
#     nan_indexs = np.isnan(col)
#     col = col.fillna(_min-1)
#     col = pd.to_numeric(col, downcast=dc)
#     return col,nan_indexs
# print weather_train_data.cloud_coverage
# weather_train_data.cloud_coverage, cloud_coverate_nan_indexs = downcast_with_nan(weather_train_data.cloud_coverage)
# print weather_train_data.cloud_coverage
# print cloud_coverate_nan_indexs
print ''


### 读数数据
print '读数数据'
# train_data = pd.read_csv('/home/helong/下载/1014/ashrae-energy-prediction/train.csv', dtype={'building_id':'uint16','meter':'category','meter_reading':'float32'}, parse_dates=['timestamp'], infer_datetime_format=True)
train_data = pd.read_csv('/home/helong/下载/1014/ashrae-energy-prediction/test.csv', dtype={'building_id':'uint16','meter':'category'}, parse_dates=['timestamp'], infer_datetime_format=True)
train_data.info(memory_usage='deep')
print ''

### 连接后的表数据
'''
how: One of ‘left’, ‘right’, ‘outer’, ‘inner’. 默认inner。
inner是取交集，outer取并集，left取左边数据集，right取右边数据集。
比如left：[‘A’,‘B’,‘C’], right[’'A,‘C’,‘D’]；
inner:AC
outer:ABCD
left:ABC
right:ACD

即保留哪部分：inner是保留两个表都有的（交集），outer并集，left是左侧，right是右侧
'''
print '连接后的全量数据'
all_data = pd.merge(pd.merge(train_data, building_data, how='left'), weather_train_data, how='left')
del train_data, building_data, weather_train_data
# all_data[['building_id','meter_reading','site_id','square_feet']] = all_data[['building_id','meter_reading','site_id','square_feet']].apply(pd.to_numeric, downcast='unsigned')
all_data[['building_id','site_id','square_feet']] = all_data[['building_id','site_id','square_feet']].apply(pd.to_numeric, downcast='unsigned')
all_data.info(memory_usage='deep')
print ''

### 全量数据DESC
print '='*50+'数值特征描述'+'='*50
print all_data.select_dtypes(include=['uint8','uint16','uint32','float32']).describe()
print ''
print '='*50+'时间特征描述'+'='*50
print all_data.select_dtypes(include=['datetime']).describe()
print ''
print '='*50+'类别特征描述'+'='*50
print all_data.select_dtypes(include=['category']).describe()
print ''
# all_data.to_csv('/home/helong/下载/1014/all_train.csv', index=False)
all_data.to_csv('/home/helong/下载/1014/all_test.csv', index=False)
