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
    - 通过`shift`、`div`实现百分比变化数据计算，例如```google.High.div(google.High.shift())```，得到今天与前一天的百分比例，如果减去1，正数说明一天内增长，负数说明一天内下降；
    - 另一种方法，通过内置的`pct_change()`来计算百分比变化，效果一样；
- 股票收益：
    - 通过`Change.sub(1)`（也就是上面的百分比变化后减1），再通过`mul(100)`，计算股票今天对比昨天的收益情况，大于0涨，小于0跌，单位是百分比；
- 绝对变化：
    - 通过`diff()`计算当前行与前一行的绝对值差；
- 标准化后对比多个时间序列：
    - 通过`div`每个序列各自的第一个元素进行标准化，然后通过`mul(100)`计算整个序列的变化趋势；
- **窗口函数**：
    - Rolling：
        - 理解为从当前行向前取**一定**长度，即一般用于算一段时间内的变化；
        - 比如传入`30D`，则是取30天，后面跟一个`mean()`表示计算30D的平均值；
        - 通常会产生NaN，可以通过指定`min_periods`来避免；
        - 通过`agg({"amt_sum": np.sum, "amt_mean": np.mean})`可以获取多个结果，且重命名；
    - Expanding：
        - 计算从开始到最后的变化，对于最后一个元素，就是计算从第一个开始到最后一个的累计变化情况；
        - 当rolling()函数的参数window=len(df)时，实现的效果与expanding()函数是一样的；
        - 例如有三列数据时：`df.rolling(3, min_periods=1,axis=1).mean()` == `df.expanding(axis=1).mean()`；
- OHLC、CandleStick：专门用于股票等可视化，通过绘制其Open、High、Low、Close来分析预测，可以通过`plotly.graph_objs.Ohlc`和`plotly.graph_objs.Candlestick`进行绘制；
- [自相关(Autocorrelation)与偏自相关(Partial Autocorrelation)](https://www.biaodianfu.com/acf-pacf.html)：
    - 自相关：
        - 也叫序列相关，是一个信号于其自身在不同时间点的互相关，非正式地来说，它就是两次观察之间的相似度对它们之间的时间差的函数；
        - 即自身与自身lag的相关系数，超过置信区间则可以认为是统计显著的，不是意外；
        - 测量一个序列在不同的延迟(lag)下与自身的关系；
        - 通过`from statsmodels.graphics.tsaplots import plot_acf`引用；
        - `plot_acf(humidity["San Diego"],lags=25,title="San Diego")`指定可视化延后的范围，此处就是1~25；
        - 通过观察结果判断其自相关系数(是否大于置信区间)，判断其是否统计显著；
    - 部分自相关：
        - 偏自相关函数用来度量暂时调整所有其他较短滞后的项 (y_{t-1}, y_{t-2}, ..., y_{t-k-1}) 之后，时间序列中以 k 个时间单位（y_{t}和y_{t-k}）分隔的观测值之间的相关；
        - 偏自相关简单说就是只对比当前数据与滞后k后的数据而不考虑二者之间的数据，借此排除间接关系，因此通常会在某个**较大的k值**后相关系数急剧下降；
        - 通过`plot_pacf(humidity["San Diego"],lags=25)`可视化结果；
        - 注意：自相关高，不代表偏自相关也高，二者很可能是有很大差异的，比如这个kernel里；

## TS分解与随机移动

- 趋势、季节性、噪声：
    - 趋势：
        - 即一致的向上或者向下的斜率；
    - 季节性：
        - 清晰的周期性模式；
    - 噪声：
        - 离群点或者缺失值；
    - 趋势、季节性：通过`sm.tsa.seasonal_decompose`，传入`google["High"],freq=360`，指定要分解的数据以及分解频率，此处是360天，结果由趋势、季节性、剩余价值、原始数据，四列组成，直接plot看结果；
- 白噪声：
    - 具有固定均值、固定方差、所有滞后均为0的自相关系数；
- 随机游走：
- 平稳性：
    - 平稳时间序列是指其统计特性（如均值、方差、自相关等）随时间而保持**不变**的时间序列；
    - 强平稳：
    - 弱平稳：
    - 强平稳并非一定是弱平稳，二者并不是包含关系；
    - 非平稳序列在建模时，需要考虑的因素远多于平稳序列，`diff`方法可以有效的将非平稳序列（比如有上升趋势的）转换为平稳序列；

## statsmodels建模

- AR Models(自回归模型)：
    - 一类随机过程的表示，它规定输出变量**线性**的依赖它自己**以前的值**和一个**随机项**，因此模型是一个**随机差分方程**的形式；
    - AR(1)：
        - ![AR-1](http://latex.codecogs.com/gif.latex?%5Cinline%20R_t%20%3D%20%5Cmu%20&plus;%20%5Cphi%20R_%7Bt-1%7D%20&plus;%20%5Cvarepsilon%20_t)
- MA Models：
- ARMA Models：
- ARIMA Models：
