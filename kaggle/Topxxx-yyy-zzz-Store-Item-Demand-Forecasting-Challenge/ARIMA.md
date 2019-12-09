# ARIMA时序模型

1. 数据预处理；
2. Target做log1p转换，降低其偏度和峰度；
3. 提取训练集中store==1$&item==1的数据做分析；
4. 数据做平稳diff处理；
5. 可视化其自相关、偏自相关、季节性、趋势等特征；
6. 根据结果提取ARIMA的参数(1,1,0)；
    ```
    ARIMA参数order:
      参数1：自回归系数，来自平稳处理后的自相关lag显著个数；
      参数2：平稳阶级，通过多少次diff后平稳；
      参数3：移动平均系数；
    ```
7. 可视化预测结果与实际结果，计算rmse值(0.36)；
8. 季节、趋势分解有什么用？


ARIMA模型order参数确定：
- https://blog.csdn.net/qq_37135484/article/details/101205161
- https://www.codercto.com/a/41483.html
- PS：ARIMA模型是最复杂的，以上的各个模型都可以认为是特殊参数下的ARIMA；
- d：表示平稳需要的差分阶数，通常为1，通过diff(n)可以平稳处理；
- p(AR)、q(MA)：
    - pq都是由平稳序列的ACF和PACF图中确定；
    - ACF：q阶后衰减趋于零（几何型或震荡性）；
    - PACF：p阶后衰减趋于零（几何型或震荡性）；
    - 即：acf确认q，pacf确认p；
