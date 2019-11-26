# 深入分析tracking数据 - base on two notebook

一些概念、关键点、notebook解释链接：
- [NFL tracking: wrangling, Voronoi, and sonars - R](https://www.kaggle.com/statsbymichaellopez/nfl-tracking-wrangling-voronoi-and-sonars)
- [initial wrangling & Voronoi areas in Python - Python](https://www.kaggle.com/cpmpml/initial-wrangling-voronoi-areas-in-python)
- [泰森多边形-Voronoi](https://baike.baidu.com/item/%E6%B3%B0%E6%A3%AE%E5%A4%9A%E8%BE%B9%E5%BD%A2/3428661?fromtitle=voronoi&fromid=9089406&fr=aladdin)：通过Voronoi可以有效的可视化球员的理论控制区域，在不考虑球员个人身体素质，当前状态(速度，加速度，角度，面向)的情况下，这个图看到让人全身发抖，学到了学到了；

## Python版本
https://www.kaggle.com/holoong9291/nfl-tracking-wrangling-voronoi-and-sonars-python

## 整体的分析流程
1. 基本数据操作
    1. 加载数据
    2. 构建ToLeft、IsBallCarrier特征
    3. 处理异常的球队名数据
2. 绘制球员站位图
    0. 绘制6个回合
    1. 区分进攻、防守、持球人
    ![球员站位图](https://www.kaggleusercontent.com/kf/21999507/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..zYETe2xt4LV4ewND0ZhaDQ.zTPx1zGWujhHtvrSfd4wLGty0kYQvYSz1o6gBu9WWHoxtZWS1fqMVBzMk3zReBGV7vfKXNfH7UzNrc5-USo20DiBWlegrQsb1BKfczvZkp3IPVmTpMbKCMQO8X1PzHBI2Ivw5NrQ6hVMvEP0EMqugtASA2orJ_g8S7wkXFPn6t-P3_7ZxVvr2XneVPPq1yiTNEfC9ZePHNdaKttiI1LCYA.ClhckRpbNGqpvVrkZy5lXQ/__results___files/__results___3_1.png)
