# README

## DESC

- 项目简单描述：通过对各种能源（冷水、电、天然气、热水和蒸汽表）消耗的预测达到节约能源的目的（未采取措施 vs 采取措施），数据来源于1000栋建筑3年的数据；
- 预测单位：单栋建筑的各项能源消耗；
- 是否时间序列：是；
- 数据量级：三年×1000栋建筑；
- 特点：未采取措施的建筑能源消耗 vs 采取措施的建筑能源消耗；
- 评估函数：RMSLE(Root Mean Squared Logarithmic Error)；
- TIMELINE：2019年12月12日；

## FEATURE INFO

- train.csv:
  - building_id：建筑表的外键；
  - meter：资源代码{0: electricity, 1: chilledwater, 2: steam, hotwater: 3}，PS：不是所有建筑都有所有资源消耗的数据；
  - timestamp：读数时间；
  - meter_reading - 千瓦时的真实读数，注意这个是带有误差的真实数据；
  - test.csv：多一个row_id，少meter_reading；
  - 间隔是1小时；
- building_meta.csv：
  - site_id - 天气表的外键；.
  - building_id - 训练表的外键；
  - primary_use - 建筑主要活动、用途类别指标（离散型，应该有很大相关性）；
  - square_feet - 建筑总面积，不知道包不包含每层楼，如果包含，那么跟floor_count就有重复，如果不包含，可以考虑构建一个总面积的特征；
  - year_built - 建筑开始使用年份，越老越费电？？
  - floor_count - 楼层总数，预计线性关系；
- weather[train/test].csv（尽可能接近建筑的天气信息）：
  - site_id - 天气表外键；
  - air_temperature - 空气摄氏温度；
  - cloud_coverage - Portion of the sky covered in clouds, in oktas
  - dew_temperature - [露点温度](https://baike.baidu.com/item/%E9%9C%B2%E7%82%B9/1574011?fr=aladdin)摄氏度；
  - precip_depth_1_hr - Millimeters
  - sea_level_pressure - 海平面压力，Millibar/hectopascals；
  - wind_direction - 风向，0~360；
  - wind_speed - 风速，米每秒；
  - 间隔是1小时；

注意：
- 预测的是仪表读数，这个是累积的；
- weather信息颗粒度是低于building信息的，比如site_id为0，对应接近100个building_id，可以理解为某一个区域的天气信息，而不是针对某栋楼，因此风向等也是重要信息；

## DATA ANALYSIS

- 建筑部分：
  1. 缺失情况：
- 天气部分：
  1. 缺失情况：
- 读数部分：
  1. 缺失情况：
