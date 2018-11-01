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
1. 观察是否还存在时间戳字段，一律改为时间段字段。
2. 数值型数据cut处理。
