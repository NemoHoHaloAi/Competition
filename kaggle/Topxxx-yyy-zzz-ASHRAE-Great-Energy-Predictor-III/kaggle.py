#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import gc

import pandas as pd, numpy as np, matplotlib.pyplot as plt, sklearn

PATH = '../input/ashrae-energy-prediction/'
PATH_BUILDING = PATH+'building_metadata.csv'
PATH_WEATHER_TRAIN = PATH+'weather_train.csv'
PATH_WEATHER_TEST = PATH+'weather_test.csv'
PATH_TRAIN = PATH+'train.csv'
PATH_TEST = PATH+'test.csv'

### 建筑数据
print('建筑数据')
building_data = pd.read_csv(PATH_BUILDING, dtype={'site_id':'uint8','building_id':'uint16','primary_use':'category','square_feet':'uint32','year_built':'float32','floor_count':'float32'})
building_data.info(memory_usage='deep')
print('')

### 天气数据
print('天气数据')
weather_train_data = pd.read_csv(PATH_WEATHER_TRAIN, dtype={'site_id':'uint8','air_temperature':'float32','cloud_coverage':'float32','dew_temperature':'float32','precip_depth_1_hr':'float32','sea_level_pressure':'float32','wind_direction':'float32','wind_speed':'float32'}, parse_dates=['timestamp'], infer_datetime_format=True)
weather_train_data.info(memory_usage='deep')

### 读数数据
print('读数数据')
train_data = pd.read_csv(PATH_TRAIN, dtype={'building_id':'uint16','meter':'category','meter_reading':'float32'}, parse_dates=['timestamp'], infer_datetime_format=True)
train_data.info(memory_usage='deep')
print('')

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
print('连接后的全量数据')
all_data = pd.merge(pd.merge(train_data, building_data, how='left'), weather_train_data, how='left')
del train_data, building_data, weather_train_data
all_data[['building_id','meter_reading','site_id','square_feet']] = all_data[['building_id','meter_reading','site_id','square_feet']].apply(pd.to_numeric, downcast='unsigned')
all_data.info(memory_usage='deep')
print('')

### 全量数据DESC
print('='*50+'数值特征描述'+'='*50)
print(all_data.select_dtypes(include=['uint8','uint16','uint32','float32']).describe())
print('')
print('='*50+'时间特征描述'+'='*50)
print(all_data.select_dtypes(include=['datetime']).describe())
print('')
print('='*50+'类别特征描述'+'='*50)
print(all_data.select_dtypes(include=['category']).describe())
print('')

### 清理内存
gc.collect()

print(all_data.corr())

#################日期时间转换###################
print('日期时间转换')
all_data['Month'] = all_data.timestamp.apply(lambda x:x.month).astype('uint8')
all_data['Day'] = all_data.timestamp.apply(lambda x:x.day).astype('uint8')
all_data['Week'] = all_data.timestamp.apply(lambda x:x.week).astype('uint8')
all_data['Hour'] = all_data.timestamp.apply(lambda x:x.hour).astype('uint8')
all_data['WeekDay'] = all_data.timestamp.apply(lambda x:x.weekday()).astype('uint8')
all_data.info(memory_usage='deep')
print('')
