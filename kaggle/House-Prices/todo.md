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

## 0913 - all in Sklearn

1. Data Loading(Check):
2. Data Info showing(Check):
3. Data Preprocessing(Check):
    - StandardScaler  无量纲化    标准化，基于特征矩阵的列，将特征值转换至服从标准正态分布
    - MinMaxScaler    无量纲化    区间缩放，基于最大最小值，将特征值转换到[0, 1]区间上
    - Normalizer    归一化      基于特征矩阵的行，将样本向量转换为“单位向量”
    - Binarizer    二值化      基于给定阈值，将定量特征按阈值划分
    - OneHotEncoder    哑编码      将定性数据编码为定量数据
    - Imputer    缺失值计算    计算缺失值，缺失值可填充为均值等
    - PolynomialFeatures  多项式数据转换    多项式数据转换
    - FunctionTransformer  自定义单元数据转换  使用单变元的函数来转换数据
4. Feature Selection(None):
    1. 2 side:
        - 特征是否发散：如果一个特征不发散，例如方差接近于0，也就是说样本在这个特征上基本上没有差异，这个特征对于样本的区分并没有什么用。
        - 特征与目标的相关性：这点比较显见，与目标相关性高的特征，应当优选选择。除方差法外，本文介绍的其他方法均从相关性考虑。
    2. 3 method:
        - Filter：过滤法，按照发散性或者相关性对各个特征进行评分，设定阈值或者待选择阈值的个数，选择特征。
        - Wrapper：包装法，根据目标函数（通常是预测效果评分），每次选择若干特征，或者排除若干特征。
        - Embedded：嵌入法，先使用某些机器学习的算法和模型进行训练，得到各个特征的权值系数，根据系数从大到小选择特征。类似于Filter方法，但是是通过训练来确定特征的优劣。
5. Dimension Reduction(None):
    - PCA
    - LDA
6. ML Model(Check):
    - Random Forest
7. Correction Factor(None):
    - Just One
8. Build Result File and Upload(Check):

## 0914 - opt

1. 修改损失函数：rmse、cv_rmse；
    1. rmse：计算根均方误差；
    2. cv_rmse：进行cv，并且计算rmse；
2. 处理异常数据点、方差过滤；
    1. 异常数据点：由于数据量不大，因此影响比较大，去掉明显处于分布外的；
    2. 方差过滤：过低方差特征无法提供足够的有用信息，且会造成干扰，比如Utilities，只有一个数据点跟其他数据点该特征值不同，这就没意义了；
3. 多模型测试、模型融合、校正系数；
    1. 单模型会陷入过拟合情况，bagging思想进行融合；
    2. 模型融合：权重调整，设置范围、步长，进行迭代计算，也就是网格搜索思想；
    3. 观察结果是否有明显的错误偏向，如果有，可以加入统一校正系数；
4. 偏斜处理-测试；
    1. 目标特征的偏斜处理；
    2. 其他距离、面积、价值等特征偏斜处理，根据skew值；
5. 构建新特征-测试；
    1. ....；
6. 优化可视化部分：与目标对比、分布情况；
    1. 明确这样做的目的、需要的产出；
    2. 可视化特征目标的关系：线性vs线性-散点图，离散vs线性-类似小提琴图；
    3. 可视化特征分布情况：线性-线图，离散-柱形图；
7. 优化整体流程：并行流程化；
    1. 结合Pipeline做流程化处理；
    2. 结合FeatureUnion做并行处理；
8. 完；
    1. 总结项目收获；
    2. 填充到memo；
    3. 修改项目名字，增加Top信息；
    4. 增加到Introduction、boss；

## 版本特征工程记录
1. v0.1：
    - 连续特征离散化；
    - 离散特征聚合处理；
    - 特征LabelEncode（部分有序的手动指定数字，其实也不需要，因为OneHot后都是二值化的结果）；
    - 离散特征OneHot处理；
