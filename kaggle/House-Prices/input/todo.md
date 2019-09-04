# TODO 

## 需要填充的字段

- MSZoning 4 处在哪个区，比如南山区
	- street
- MasVnr
	- MasVnrArea 23 砖石面积
	- MasVnrType 24 砖石类型
- LotFrontage 486 距离街道直线距离，可以由LotConfig等其他Lot信息辅助
	- 其他Lot，比如LotConfig,LotArea,LotShape
    
## 可视化

https://www.jianshu.com/p/ffcd6e49c373

- 当目标字段为连续值时，如何进行连续特征和离散特征的可视化；
	- 散点图可视化连续值&连续值，同时可以在其中增加点的颜色表示另一个离散维度，比如销售价格和地下室总面积，颜色表示是否有泳池；
- 对于离散特征的LabelEncode操作，半有序的特征的LabelEncode是否手动指定映射关系为好；
- 可视化需要得到什么样的结果算是完成；
