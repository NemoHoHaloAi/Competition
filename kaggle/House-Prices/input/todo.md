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
- 当目标字段为连续值时，如何进行连续特征和离散特征的可视化；
	- 散点图可视化连续值&连续值，同时可以在其中增加点的颜色表示另一个离散维度，比如销售价格和地下室总面积，颜色表示是否有泳池；
- 对于离散特征的LabelEncode操作，半有序的特征的LabelEncode是否手动指定映射关系为好；
- 考虑多特征的可视化怎样组合合适，是根据业务上的共同点，还是相关性上较高的点；
	- 单特征分析：数值型可视化分布情况、离散型占比等，比如房屋类型各个类型数量；
	- 结合目标特征分析：类型对应售价情况；
	- 加入辅助特征联合可视化分析：售价&面积的散点图，类型做颜色；
- 可视化需要得到什么样的结果算是完成；
