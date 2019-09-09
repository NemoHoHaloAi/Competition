# TODO 

## 需要填充的字段

- MSZoning 4 处在哪个区，比如南山区
	- street
- MasVnr
	- MasVnrArea 23 砖石面积
	- MasVnrType 24 砖石类型
- LotFrontage 486 距离街道直线距离，可以由LotConfig等其他Lot信息辅助
	- 其他Lot，比如LotConfig,LotArea,LotShape
    
## [可视化](https://github.com/NemoHoHaloAi/something_I_should_remember/blob/master/memo/iiam/iv/da_ml/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96/README.md)

- [seaborn用法](http://seaborn.pydata.org/examples/index.html)
- [seaborn多维度分析](https://www.jianshu.com/p/3ae90f227034)
- [seaborn讲解](https://www.jianshu.com/p/95d02007bff5)
- 当目标字段为连续值时，如何进行连续特征和离散特征的可视化；
	- 散点图可视化连续值&连续值，同时可以在其中增加点的颜色表示另一个离散维度，比如销售价格和地下室总面积，颜色表示是否有泳池；
- 对于离散特征的LabelEncode操作，半有序的特征的LabelEncode是否手动指定映射关系为好；
- 考虑多特征的可视化怎样组合合适，是根据业务上的共同点，还是相关性上较高的点；
	- 单特征分析：数值型可视化分布情况、离散型占比等，比如房屋类型各个类型数量；
	- 结合目标特征分析：类型对应售价情况；
	- 加入辅助特征联合可视化分析：售价&面积的散点图，类型做颜色；
- 可视化需要得到什么样的结果算是完成；

## 0905
- 可视化的目的、结果需求是什么？
- 怎么进行后续的可视化来达到我们的需求，产出我们需要的结果？

## 0906
- 可视化过程需要考虑的四个问题：
	1. What data do u have?
	2. What do u want to know about data?
	3. Which visulazation method should be use?
	4. What do u see and is it mean something or not?

> 「先总览，再缩放并筛选，然后按需寻找细节」

## 0908
- 目前在可视化特征构建部分遇到一些困难，如何进行好的可视化来指导后续的特征工程：拆分组合、丢弃、离散化等等；
- 考虑：第一版先不考虑太多，争取尽快提交，以结果为导向，继续优化；

## 0909
通过FE电子书、文章中寻求一些答案；

分类数据有两大类——定序（Ordinal）和定类（Nominal），定序分类的属性值则存在着一定的顺序意义或概念，比如衣服的按大小号分类，在任意定类分类数据属性中，这些属性值之间没有顺序的概念：
- 定序分类熟悉之间存在着先后顺序。一般来说，没有通用的模块或者函数可以根据这些顺序自动将这些特征转换和映射到数值表示，可以使用自定义的编码\映射方案；
- 定类属性转换成更具代表性的数值格式，即OneHot编码；

- 考虑离散特征如何处理：
	- 目前：
		1. 特征对应目标均值；
		2. 组合两个特征构建新特征；
	- 后续：
		1. 仍需处理的特征：['MSSubClass', 'MSZoning', 'LotShape', 'Street', 'Alley', 'LandContour', 'LandSlope', 'Utilities', 'LotConfig', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating', 'CentralAir', 'Electrical', 'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive', 'PoolQC', 'Fence', 'MiscFeature', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition']

## 后续
### 处理
- label encode（- 对于有序、半有序的离散化，手动指定离散化后的映射关系）, one-hot；
- 标准化、归一化；

### 其他
- 函数式编程+pipe：
	- https://www.jianshu.com/p/6bcb0f11cc1d
	- 函数式编程：所有对与dataframe的操作都抽象为函数，尤其是特征预处理、特征工程部分；
	- 利用pipe进行链式编程，增强可读性；

## 版本特征工程记录
1. v0.1：
    - 连续特征离散化；
    - 离散特征聚合处理；
    - 特征LabelEncode（部分有序的手动指定数字，其实也不需要，因为OneHot后都是二值化的结果）；
    - 离散特征OneHot处理；
