# [Everything U can do with TS](https://www.kaggle.com/thebrownviking20/everything-you-can-do-with-a-time-series)

## 日期时间简介

- 加载TS数据：
    - 指定时序列为index，使用`parse_dates`转换为datetime字段，方便后续利用该字段特征做处理；
- 清洗、准备数据：
    - 时序相关数据的缺失值，通常可以利用`fillna`，参数`ffill`来前向填充，因为该类数据通常有周期性、前后依赖关系；
- 可视化TS：
    - `asfreq`改变数据的时序频率函数，例如传入参数`M`，即为将频率转为monthly，用于可视化看整体趋势很有用（可能天的数据太多，反而不直观）；
    - 直接调用`plot`，通过指定`subplots=True`，将数据绘制到子图中；
- 时间戳和周期：
    - 时间戳：表示一个时间点，可以通过`pd.Timestamp`，传入`(2017, 1, 1, 12)`创建，表示2017-01-01 12:00:00；
    - 周期：表示一段时间，可以通过`pd.Period`，传入`('2017-01-01')`创建，表示2017-01-01一整天，也包含上述时间戳；
    - 互相转换：通过`to_period`将时间戳转换为周期，传入`(freq='H')`表示范围为小时，通过`to_timestamp`将周期转换为时间戳，传入`(freq='H', how='start')`表示取周期的start点转换，取到小时；
- date_range：
    - 用于返回固定频率的`datetimeindex`，通过`date_range`；
    - 传入`(start='1/1/18', end='1/1/19', freq='M')`指定开始结束点，以及频率；
    - 传入`periods`来指定生成的步长规则；
- to_datetime：
    - 将其他类型转为datetime类型；
- 移动(**shifting**)和滞后(**lags**)：
    - 主要用于将当前数据与其过去、未来做对比时使用，或构造相关特征；
    - 通过调用`shift`，传入`periods`，正数表示后移，负数表示前移，并通过将移动后数据与自身进行数学运算得到delta等数据；
- 重采样：
    - 向上抽采样-过采样：
        - 将TS数据从低频提到高频，比如每月到每天，涉及到填充和插值处理；
        - 通过`resample`，传入`('D')`将频率从每三天提升为每天，通过指定`pad()`，指定前向填充，与ffill相同；
    - 向下抽采样-欠采样：
        - 将TS数据从高频降为低频，比如每天到每月，涉及到相关数据聚合（比如Future-Sales-Predict）；
        - 通过`resample`，传入`('3D')`将频率从每小时降低到每三天，通过指定`mean()`，聚合采用平均值；

## 金融与统计

- 百分比变化：
    - 通过`shift`、`div`实现百分比变化数据计算，例如```google.High.div(google.High.shift())```；

## TS分解与随机移动

## statsmodels建模
