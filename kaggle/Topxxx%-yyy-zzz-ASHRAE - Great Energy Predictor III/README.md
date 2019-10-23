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
- 0. 确定reading：
    1. 是否是累计的；
    2. 会不会清空；
    3. 有没有什么清空规律；
- 1. 合并训练数据；
- 2. EDA：
    - 查看各字段与reading的关系，以及可能有相关性的各字段之间的关系，比如楼层和面积，风速和温度等；
    - 查看年份、楼层对读数的影响，如果不大，则不进行填充，直接丢弃；
    - 查看楼层和面积的关系，如果相关性很强，那么楼层也可以舍弃，直接用面积即可；
- 3. FEATURE ENGINERING；
    - 表合并前，做一些异常处理、数据转换等工作，避免合并后太大，操作会内存溢出的问题；
    	- 建筑表1449：
    		- 缺失：
    			- 年份：675，平均值中位数、耗能情况、楼层；
    			- 楼层：355，面积、年份、耗能情况；
    		- onehot：
    			- primary_use
    		- 数据转换：
    			- 暂无；
    	- 天气表：
    		- 缺失：
    			- air_temperature       139718，前后填充；
    			- cloud_coverage        70600，前后填充；
    			- dew_temperature       139660，前后填充；
    			- precip_depth_1_hr     89484，前后填充；
    			- sea_level_pressure    129155，前后填充；
    			- wind_direction        133505，前后填充；
    			- wind_speed            139469，前后填充；
    		- 数据转换：
    			- 数值型考虑进行boxcox转换等；
    	- 读数表：
    		- 数据转换：
    			- meter_reading：考虑做boxcox；
    - weather信息颗粒度是低于building信息的，比如site_id为0，对应接近100个building_id，可以理解为某一个区域的天气信息，而不是针对某栋楼，因此风向等也是重要信息；
    - 数据存在一定的缺失、误差；
- 一些点：
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


## NOW
- 2019-10-20:
	- 项目创建；
	- 加载数据；
	- 分析reading的特性；
	- 展示数据基本信息；
	- 展示连续、类别特征与目标特征关系图、分布图；
- TODO
	- https://nbviewer.jupyter.org/github/NemoHoHaloAi/Competition/blob/master/kaggle/Top40%25-0.12847-zzz-House-Prices/House-Prices.ipynb
	- 是否要转移到kaggle kernel，目前本机内存不太够用；
		- 在kernel上测试下全连接训练数据下的日期转换速度；
	- EDA：
		- 类别特征分布可视化优化：
			- CHECKED-柱形图展示（sns.catplot(x="site_id", col="meter", col_wrap=2, data=all_train_data, kind="count")）；
			- 增加堆叠图查看占比
				- res = bd.groupby(['site_id','primary_use']).building_id.count()
				- res_unstack = res.unstack(level=-1).fillna(0).astype('int')
				- labels = list(res_unstack)
				- plt.stackplot(bd.site_id.unique(), list(res_unstack.values), labels=labels)
				- res_unstack_ratio = res_unstack.apply(lambda x:[xx*1./x.sum() for xx in x], axis=0)
				- plt.stackplot(bd.site_id.unique(), list(res_unstack_ratio.values), labels=labels)
		- 相关性、离散型计算（组合成df输出）；
			- 相关：直接corr，关注下连续性、离散型、线性相关与否等；
			- 离散：从分布图上观察；
		- 时间特征拆分为多个特征后删除，拆分后特征downcast；
			- 月份：x.month；
			- 第几周：x.week；
			- 几号：x.day；
			- 星期几：x.weekday()；
			- 时间段4小时一个段：x.hour/4；
			- 类型全部uint8
			- rolling添加新特征
			- 周期性：利用同一日、同一星期几、同一时间段分析；
			- prophet https://blog.csdn.net/anshuai_aw1/article/details/83412058 https://facebook.github.io/prophet/docs/quick_start.html
		- year_built：重组为建筑年限字段，观察关系图；
		- 楼层和面积的关系；
	- 预处理：
		- 缺失处理；
			- 建筑信息：
				- 年份：没有太好办法，考虑进行多条件组合后的均值或者中位数，缺失1/2，考虑丢弃；
				- 楼层：参考面积，如果没有直接关系，那么也没有太好办法，缺失了4/5，考虑丢弃；
			- 天气信息：
				- 温度：缺失不到100，考虑用同site前后时间段填充；
				- 云层覆盖：缺失一半，不清楚如何填充，暂时不处理，丢弃；
				- 露点温度：同温度；
				- precip_depth_1_hr：缺失一半不到，不知道什么含义，暂时不处理，丢弃；
				- 海平面压力：缺失1/12，填充方式类似；
				- 风向风速：缺失不多，填充类似；
				- wtd.fillna(method='ffill')
		- 异常处理；
	- 特征工程：
		- 根据上述EDA过程增删特征；
			- 删掉关系不大的：
			- 删掉有重复信息的：
			- 删掉缺失太多，且无法很好填充的：年份、楼层
			- 删掉不知道如何使用的：云层覆盖、precip
			- 删掉方差低的：VarianceThreshold(threshold=threshold).fit(all_data_without_id_saleprice)
		- 合并train和test数据？？？
		- 连续特征的分布转换（包括reading）；
		- labelEncode、one-hot；
	- 建模：
		- 定义rmsle；
		- cv+随机森林获取baseline score；
