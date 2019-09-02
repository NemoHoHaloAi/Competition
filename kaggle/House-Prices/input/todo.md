# TODO 

## 需要填充的字段

- SaleType 1 销售类型
- KitchenQual 1 厨房质量
	- 其他厨房字段Kitchen填充
	- 只有一个kitchen，表示数量
	- 整体质量
- Exterior
	- Exterior2nd 1 房屋外部材料
	- Exterior1st 1 房屋外部材料2
- Electrical 1 电力系统 
	- 暖气形式、壁炉等辅助填充
	- CentralAir
- Functional 2 其他功能
- Utilities 2 可用资源类型，煤气、瓦斯等
	- 电力系统、暖气类型填充
	- CentralAir
- MSZoning 4 处在哪个区，比如南山区
	- street
- MasVnr
	- MasVnrArea 23 砖石面积
	- MasVnrType 24 砖石类型
- LotFrontage 486 距离街道直线距离，可以由LotConfig等其他Lot信息辅助
	- 其他Lot，比如LotConfig,LotArea,LotShape
- nan表示没有，这一类可以直接填充'None'，但是需要考虑他的nan是否是正常的，这里需要其他字段帮校验，例如PoolQC可以用PoolArea校验
	- FireplaceQu 1420 壁炉质量，nan表示没有
		- Fireplaces 数量
	- Fence 2348 围栏质量，nan表示没有
	- Alley 2721 物业通道类型，nan表示没有
	- MiscFeature 2814 其他功能，nan表示没有
		- MiscVal misc价值
	- PoolQC 2909 泳池质量，nan表示没有，结合PoolArea确认是否面积为0
