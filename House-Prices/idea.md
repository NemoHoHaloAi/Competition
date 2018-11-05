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
2. PCA后结果过于理想，说明存在过拟合问题可能。
3. 目前过拟合严重。

## 第三版
0. [学习曲线分析](https://blog.csdn.net/aliceyangxi1987/article/details/73598857)。
	
	当训练集和测试集的误差收敛但却很高时，为高偏差。 
	左上角的偏差很高，训练集和验证集的准确率都很低，很可能是欠拟合。 
	我们可以增加模型参数，比如，构建更多的特征，减小正则项。 
	此时通过增加数据量是不起作用的。

	当训练集和测试集的误差之间有大的差距时，为高方差。 
	当训练集的准确率比其他独立数据集上的测试结果的准确率要高时，一般都是过拟合。 
	右上角方差很高，训练集和验证集的准确率相差太多，应该是过拟合。 
	我们可以增大训练集，降低模型复杂度，增大正则项，或者通过特征选择减少特征数。

	理想情况是找到偏差和方差都很小的情况，即收敛且误差较小。

1. 处理过拟合问题：关注PCA、数值cut处理、[feature selection](https://www.cnblogs.com/stevenlk/p/6543628.html#%E7%A7%BB%E9%99%A4%E4%BD%8E%E6%96%B9%E5%B7%AE%E7%9A%84%E7%89%B9%E5%BE%81-removing-features-with-low-variance)。

feature selection:
1. 移除低方差的特征 (Removing features with low variance):说白了就是特征的取值偏斜很大时，取消该特征，比如90%都是a，只有10%是b的情况。
2. 单变量特征选择 (Univariate feature selection):计算单变量的相关性，分类问题（卡方检验，f_classif, mutual_info_classif，互信息），回归问题（皮尔森相关系数，f_regression, mutual_info_regression，最大信息系数）。
3. 递归特征消除 (Recursive Feature Elimination):类似PCA，指定一个所需的特征数，算法会尝试所有的特征组合来找到最小error的组合。
4. 使用SelectFromModel选择特征 (Feature selection using SelectFromModel)。
5. 将特征选择过程融入pipeline (Feature selection as part of a pipeline)。

## 第三版实施
0. 绘制学习曲线（针对各个算法），目测应该都是过拟合。
1. PCA前做特征选择。
	1. 过滤偏斜特征（针对所有特征） - 过滤掉偏斜厉害的特征（观察是否会过滤掉数值型特征）。
	2. 回归问题的过滤可以选[相关系数](http://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html#sphx-glr-auto-examples-feature-selection-plot-f-test-vs-mi-py) - 过滤掉低相关的特征。
		1. 我们特征中很多都不是线性关系（非数值） - [SelectKBest](http://scikit-learn.org/stable/modules/feature_selection.html#variance-threshold)-互信息过滤非线性特征中相关性不高的特征。
		2. 而数值依然可以通过相关系数来计算 - SelectKBest-线性回归过滤掉数值型中相关性不高的特征。
	3. 递归特征消除，设置算法过滤特征 - 组合各种特征来选择最优的组合（耗时比较长，取决于待筛选特征总数以及保留特征数的排列组合数量）。
	4. 根据特定算法来筛选 - 例如随机森林等拟合后有ceof_和feature_important_的算法。
2. PCA（可选）。
3. 训练模型。
4. 绘制学习曲线观察效果。
5. 重复1,2,3,4。
6. 将确定的特征选择使用[pipeline](https://www.jianshu.com/p/9c2c8c8ef42d)实现。

> 最适合的[解决办法](https://www.jianshu.com/p/f485dc676e1c)是，通过过滤法筛选出一批有潜力的特征，再通过封装法精选特征，从而构建一个预测效果良好的机器学习模型。
