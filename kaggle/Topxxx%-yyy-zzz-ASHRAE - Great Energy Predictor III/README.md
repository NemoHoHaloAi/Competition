# README

https://www.kaggle.com/c/ashrae-energy-prediction/data

## DESC

- 项目简单描述：通过对各种能源（冷水、电、天然气、热水和蒸汽表）消耗的预测达到节约能源的目的（未采取措施 vs 采取措施），数据来源于1000栋建筑3年的数据；
- 预测单位：单栋建筑的各项能源消耗；
- 是否时间序列：是；
- 数据量级：三年×1000栋建筑；
- 特点：未采取措施的建筑能源消耗 vs 采取措施的建筑能源消耗；
- 评估函数：RMSLE(Root Mean Squared Logarithmic Error)；
- TIMELINE：2019年12月12日；

## FILE

- weather.csv:各个site每小时的天气信息，7M；
- building.csv:每个建筑的元信息, 40+K；
- train.csv:每个建筑每小时的读数信息，600+M；
- 测试文件大于训练文件；

## FEATURE DESC

- train.csv:
  - building_id：建筑表的外键；
  - meter：资源代码{0: electricity, 1: chilledwater, 2: steam, 3: hotwater}，PS：不是所有建筑都有所有资源消耗的数据；
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

## TIPS

- 问题转换：不预测读数，预测增量；
- 记录每个表的NaN值，转换后；
- 预测的是仪表读数，这个是累积的；
- weather信息颗粒度是低于building信息的，比如site_id为0，对应接近100个building_id，可以理解为某一个区域的天气信息，而不是针对某栋楼，因此风向等也是重要信息；
- 数据存在一定的缺失、误差；
- 预测能源类型与各个特征字段应该是有不同含义的，比如温度可能主要影响用电、建筑类型影响用水等，这里是否要区分来建模预测呢？
- 设置timestamp为x坐标，观察各个能源读数的变化情况、能源消耗的变化情况；
- 合并表后，类似row_id这一类信息可以删掉；
- 加载csv时，直接指定字段类型；
- timestamp挖掘：日期（工作日）、时间段（上中下、工作时间等）
- 几个相关点：
	- 季节性：春夏秋冬气候各不同；
	- 天气：冷热、潮湿、刮风、特殊天气；
	- 时间性：白天晚上、工作非工作；
	- 建筑类型：住宅、办公、教育；
	- 年份：用电设备随着年份的增长而增长；
