## 第一版
1. 训练数据1460，测试数据1460。
2. 特征中大部分是枚举型，少部分是数值型和时间数据，需要mapping、convert，需要在full之后进行。
	1. 枚举型的值具有数值关系的（质量相关的），比如厨房质量：Ex>Gd>Ta>Fa>Po，那么mapping到数值上时这种关系要不要用数字体现。
	2. 其余枚举型是没有数值关系的，比如House Stype等。
3. 特征很多，70+，对应数据量却很少，需要feature Selection或者PCA。
4. (YearBuilt)关于建造年份、月份等，可以create一个房龄的feature。
5. 关于(YrSale,MoSale)销售年份、月份等，可以create一个至今销售时长的feature。
6. (YearRemodAdd)根据改建年份，create是否有改建的feature以及改建后的房龄的feature。
6. 部分数值型数据可能要cut处理来减少特征值。
7. 部分Feature的NA值通常是因为没有相关设施导致的，比如泳池面积，NA表示没有泳池，那么用0表示，而字符型的比如车库类型这种，NA用'None'表示代表没有车库的情况。
8. SaleType和SaleCondition看着对结果影响很大的样子。


## 第一版实施
1. 意义枚举型没有处理。
2. 数值型数据没有cut处理。
3. 去掉了YearBuilt、YrSold、MoSold字段。
4. 是否有其他年份等字段没有去除。


## 第二版
1. 观察是否还存在时间戳字段，一律改为时长字段。
2. 数值型数据cut处理，并LabelEnccoder处理。
3. 参考kernel可视化统计数据（例如：计算特征相关系数并绘制热图）。
4. PCA。
5. 绘制PCA后的热图。

## 第二版实施
1. 暂时没有做cut处理（不过目前过拟合，所以可能还是需要的）。
2. PCA后结果过于立项，可能有问题。
3. 目前过拟合严重。

## 第三版
0. [学习曲线分析](https://blog.csdn.net/aliceyangxi1987/article/details/73598857)。
1. 处理过拟合问题：关注PCA、数值cut处理、[feature selection](https://www.cnblogs.com/stevenlk/p/6543628.html#%E7%A7%BB%E9%99%A4%E4%BD%8E%E6%96%B9%E5%B7%AE%E7%9A%84%E7%89%B9%E5%BE%81-removing-features-with-low-variance)。

feature selection:
1. 移除低方差的特征 (Removing features with low variance):说白了就是特征的取值偏斜很大时，取消该特征，比如90%都是a，只有10%是b的情况。
2. 单变量特征选择 (Univariate feature selection):计算单变量的相关性，分类问题（卡方检验，f_classif, mutual_info_classif，互信息），回归问题（皮尔森相关系数，f_regression, mutual_info_regression，最大信息系数）。
3. 递归特征消除 (Recursive Feature Elimination):类似PCA，指定一个所需的特征数，算法会尝试所有的特征组合来找到最小error的组合。
4. 使用SelectFromModel选择特征 (Feature selection using SelectFromModel)。
5. 5. 将特征选择过程融入pipeline (Feature selection as part of a pipeline)。
