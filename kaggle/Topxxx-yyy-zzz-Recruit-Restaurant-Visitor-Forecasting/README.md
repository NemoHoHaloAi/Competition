# README

- [项目链接](https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting)
- 项目背景：经营一家餐厅并不总是像第一感觉一样迷人，会有很多问题跳出来干扰到生意，其中一个问题是预测当天的顾客数量以准备相应的食材和人工，而这通常是比较困难的，因为很多因素会对这一事件有干扰，比如不同的城市、地区，天气，节假日，赛事等等，尤其是对一些历史数据比较少的新店来说；
- 项目目的：建立模型，基于预约和到店的数据，对顾客数量进行预测；
- RMSLE；
- 预测目标：对每个店铺和日期的组合id(两份数据源的id连接的结果xxx_yyy)进行顾客数量预测；
- 数据：
    - 26M；
    - 跨度：
        - 训练集：16年到17年4月；
        - 测试集：17年4月最后一周和5月；
        - 注意：测试集有意包含了一个日本称之为黄金周的节日；
    - 组成：
        - Hot Pepper Gourmet (hpg)：类似大众点评，用户可以在线搜索以及在线预约；
        - AirREGI / Restaurant Board (air)：类似支付宝，预约控制及现金注册系统；
    - 关于id：每家店都有唯一的air_store_id and hpg_store_id，注意不是每家店都在两个系统上有数据，不能假设这一点；
    - 可以通过store_id_relation表做商店的归一处理；
    - date_info提供了基本的日期信息；
    - air_visit_data没有对应的hpg数据；

## 备注

```python
visit：
<class 'pandas.core.frame.DataFrame'>
Int64Index: 396262 entries, 0 to 477
Data columns (total 15 columns):
visit_date     396262 non-null datetime64[ns]       ----------------
store_id       396262 non-null object               ----------------
visitors       396262 non-null float64
from           396262 non-null float64
day_of_week    396262 non-null float64
holiday_flg    396262 non-null float64
genre_name     396262 non-null object
latitude       396262 non-null float64
longitude      396262 non-null float64
area_1         396262 non-null object
area_2         396262 non-null object
area_3         396262 non-null object
m_500          396262 non-null float64
m_1000         396262 non-null float64
m_5000         396262 non-null float64
dtypes: datetime64[ns](1), float64(9), object(5)
memory usage: 48.4+ MB


reserve：
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1384883 entries, 304 to 7051324
Data columns (total 9 columns):
store_id                   1384883 non-null object           ----------------
visit_date                 1384883 non-null datetime64[ns]   ----------------
reserve_count              1384883 non-null float64
from_air_count             1384883 non-null float64
from_hpg_count             1384883 non-null float64
from_both_count            1384883 non-null object
reserve_visitors_sum       1384883 non-null float64
reserve_visitors_mean      1384883 non-null float64
reserve_visitors_median    1384883 non-null float64
dtypes: datetime64[ns](1), float64(6), object(2)
memory usage: 105.7+ MB



_visit：
<class 'pandas.core.frame.DataFrame'>
Int64Index: 396262 entries, 0 to 396261
Data columns (total 22 columns):
visit_date                 396262 non-null datetime64[ns]
store_id                   396262 non-null object
visitors                   396262 non-null float64
from                       396262 non-null float64
day_of_week                396262 non-null float64
holiday_flg                396262 non-null float64
genre_name                 396262 non-null object
latitude                   396262 non-null float64
longitude                  396262 non-null float64
area_1                     396262 non-null object
area_2                     396262 non-null object
area_3                     396262 non-null object
m_500                      396262 non-null float64
m_1000                     396262 non-null float64
m_5000                     396262 non-null float64
reserve_count              28699 non-null float64
from_air_count             28699 non-null float64
from_hpg_count             28699 non-null float64
from_both_count            28699 non-null object
reserve_visitors_sum       28699 non-null float64
reserve_visitors_mean      28699 non-null float64
reserve_visitors_median    28699 non-null float64
dtypes: datetime64[ns](1), float64(15), object(6)
memory usage: 69.5+ MB
```

不是每个店每天都有预约数据，为什么reserve数据这么多，链接后还有那么多NaN：
- 数据是不是以store_id&visit_date为主键组织的；
- 没有的数据是否可以由0填充表示当天无顾客预约；
- 预约的日期与到店日期做映射，这个由链接字段指定，链接的是visit_date还是reserve_date，目前是visit_date，也就是根据预约的到店日期链接起来；
- 那为什么很多店很多日期没有该数据呢（396262数据只有28699是有数据的，其他都没有，这里要关注），有一个原因是两个来源之一是没有预约数据的，这个如何处理缺失问题，不代表没有预约，只是没有数据；
- 两段日期对应覆盖关系；
