# Prophet - 先知

传统的时间序列分析的一种通用方式是时间序列分解，即将模型分解为季节St、趋势Tt、剩余项Rt，可能会再加一个高斯分布的噪声项，公式为![formula](http://latex.codecogs.com/gif.latex?y_t%3DS_t&plus;T_t&plus;R_t)，除了这种**加法**的形式，还有一种**乘法**的形式，公式为![formula](http://latex.codecogs.com/gif.latex?y_t%3DS_t*T_t*R_t)，而乘法可以写成先取对数，再计算加法，所以还可以写成这样![formula](http://latex.codecogs.com/gif.latex?lny_t%3DlnS_t&plus;lnT_t&plus;lnR_t)

Prophet的几点优化：
- 支持python和R；
- 拟合时使用pyStan，加快拟合速度；
- 预测使用时间序列+机器学习，提高性能；
- 可以对逻辑回归增长、降低进行先验的饱和设置；
- 时间序列模型上增加节假日项，这是对销售影响很大的项，算是对原始公式的补充，公式为![formula](http://latex.codecogs.com/gif.latex?y%28t%29%3Dg%28t%29&plus;s%28t%29&plus;h%28t%29&plus;%5Cepsilon%20_t)
    - g(t)表示趋势项；
    - s(t)表示周期项或者季节项；
    - h(t)表示节假日项；
    - epsilon表示剩余项或者误差项；
    - Prophet简单说就是对这几项进行拟合，最后累加起来得到预测结果；
    
## 公式分解

### 趋势项g(t)



### 周期项s(t)

### 节日项h(t)
    
## 适用优势场景

- 针对每小时、每天或每星期的观察频次，有至少数月（理想情况的一年）的历史记录；
- 多重显著的“人类层级”周期性：星期X以及年份；
- 日期间隔不规则的重要节日（比如超级碗），需要事先得知；
- 观察缺失或是异常值在合理范围内；
- 历史趋势变化，比如产品发布或者改写记录（logging changes）；
- 符合非线性增长曲线的趋势，有天然上、下限或者饱和点；

## 参考
- https://www.jiqizhixin.com/articles/2019-02-19-11
- https://www.jianshu.com/p/4d85e6fbe707
- https://www.cnblogs.com/jiaxin359/p/8872986.html
