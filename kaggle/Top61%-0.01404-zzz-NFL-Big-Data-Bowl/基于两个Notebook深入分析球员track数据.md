# 深入分析tracking数据 - base on two notebook

一些概念、关键点、notebook解释链接：
- [NFL tracking: wrangling, Voronoi, and sonars - R](https://www.kaggle.com/statsbymichaellopez/nfl-tracking-wrangling-voronoi-and-sonars)
- [initial wrangling & Voronoi areas in Python - Python](https://www.kaggle.com/cpmpml/initial-wrangling-voronoi-areas-in-python)
- [泰森多边形-Voronoi](https://baike.baidu.com/item/%E6%B3%B0%E6%A3%AE%E5%A4%9A%E8%BE%B9%E5%BD%A2/3428661?fromtitle=voronoi&fromid=9089406&fr=aladdin)：通过Voronoi可以有效的可视化球员的理论控制区域，在不考虑球员个人身体素质，当前状态(速度，加速度，角度，面向)的情况下，这个图看到让人全身发抖，学到了学到了；

## Python版本
https://www.kaggle.com/holoong9291/nfl-tracking-wrangling-voronoi-and-sonars-python

## 整体的分析流程
1. 标准化坐标体系
    1. 基本数据操作
        1. 加载数据；
        2. 构建ToLeft、IsBallCarrier特征；
        3. 处理异常的球队名数据；
    2. 绘制回合图
        1. 绘制6个回合；
        2. 区分进攻、防守、持球人；
    ![回合图](https://www.kaggleusercontent.com/kf/21999507/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..zYETe2xt4LV4ewND0ZhaDQ.zTPx1zGWujhHtvrSfd4wLGty0kYQvYSz1o6gBu9WWHoxtZWS1fqMVBzMk3zReBGV7vfKXNfH7UzNrc5-USo20DiBWlegrQsb1BKfczvZkp3IPVmTpMbKCMQO8X1PzHBI2Ivw5NrQ6hVMvEP0EMqugtASA2orJ_g8S7wkXFPn6t-P3_7ZxVvr2XneVPPq1yiTNEfC9ZePHNdaKttiI1LCYA.ClhckRpbNGqpvVrkZy5lXQ/__results___files/__results___3_1.png)
    3. 调整进攻方向
        1. 将所有进攻都调整为从左往右，方向后续可视化以及视觉效果；
        2. 通过YardLine、FieldPosition、X、Y等；
        3. 展示统一方向后的回合图；
        4. 下图：蓝色是进攻方，红色是防守方，且蓝色一直是从左向右进攻，虚线是回合开始的地方，码数大于0说明在虚线右侧结束回合，小于0说明在左侧结束（被擒抱损失码数的情况下）；
    ![调整方向后回合图](https://www.kaggleusercontent.com/kf/21999507/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..zYETe2xt4LV4ewND0ZhaDQ.zTPx1zGWujhHtvrSfd4wLGty0kYQvYSz1o6gBu9WWHoxtZWS1fqMVBzMk3zReBGV7vfKXNfH7UzNrc5-USo20DiBWlegrQsb1BKfczvZkp3IPVmTpMbKCMQO8X1PzHBI2Ivw5NrQ6hVMvEP0EMqugtASA2orJ_g8S7wkXFPn6t-P3_7ZxVvr2XneVPPq1yiTNEfC9ZePHNdaKttiI1LCYA.ClhckRpbNGqpvVrkZy5lXQ/__results___files/__results___7_1.png)
2. 球员空间和Voronoi区域
    1. 比赛的关键在于找到橄榄球的特有特征，这使得数据更具表达力；
    2. 初步思考：持球人的**空间**（这一点我的kernel也考虑了，验证结果仅仅提升了0.0002，应该没有挖掘到更关键的点）；
    3. 空间：持球人的空间越大，更准确的说是从左向右进攻时前面的空间越大，越容易获得更多的码数（这里我之前计算的方式只考虑了距离，没有考虑空间，也就是面积，主要是没有找到一个量化空间的算法）；
    4. 量化算法：**Voronoi**是一种将空间划分为最近的点的方法，通过它可以初步的对球场控制区域进行划分；
    5. 看下图：每个球员（点）都有自己对应的空间，有的大有的小，这里就没有考虑球员的差异性，仅考虑点间的距离；
![Voronoi](https://www.kaggleusercontent.com/kf/21999507/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..zYETe2xt4LV4ewND0ZhaDQ.zTPx1zGWujhHtvrSfd4wLGty0kYQvYSz1o6gBu9WWHoxtZWS1fqMVBzMk3zReBGV7vfKXNfH7UzNrc5-USo20DiBWlegrQsb1BKfczvZkp3IPVmTpMbKCMQO8X1PzHBI2Ivw5NrQ6hVMvEP0EMqugtASA2orJ_g8S7wkXFPn6t-P3_7ZxVvr2XneVPPq1yiTNEfC9ZePHNdaKttiI1LCYA.ClhckRpbNGqpvVrkZy5lXQ/__results___files/__results___9_0.png)
3. 
