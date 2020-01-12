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

想法：
1. 只关注air的预约数据以及hpg中与air150个相同店的预约数据，肯定存在缺失，缺失reserve填0；
    1. 修改reserve，去掉hpg全部，补充150个有关系的；
    2. 链接到visit后，进行缺失填充，用0；
    3. 829-314&150(333) for 821；
2. reserve_count如何与visitors配合使用，还是单独使用；
    1. 暂定单独使用，方式跟visitors类似；
3. 将hpg剩余部分用上；


```python
关系表中air店铺数量：150
air店铺信息表中air店铺数量：829
关系表中hpg店铺数量：150
hpg店铺信息表中hpg店铺数量：4690
air预约表中air店铺数量：314
hpg预约表中hpg店铺数量：13325
air光顾表中air店铺数量：829
在air光顾表但是不在air预约表店铺数量：515


314%150店铺数量：333
air光顾表中air店铺数量：829
在visit中而不在reserve中的店铺数量：496
```

看到合并后补充了一些，但是对visit来说，依然是更多的店铺(496 in 829)是不在预约数据中的，同时大量预约数据处于无用状态；
- 链接有的：visit中只有1/6是有对应store&date的reserve的；
- 挖掘没的：更多的数据是缺失的；

想法2.0：
1. 不对reserve数据与visit数据链接，目前看能够直接链接的部分太少了1/6，可能不仅起不到作用，还容易有副作用；
2. 分别对visit和reserve进行FE处理，方式类似目前的visit，只不过对于reserve，target是reserve_visitors；
3. 整合，reserve数据量大，visit数据量小，但是visit是直接数据，而reserve是间接，如何整合，最大化发挥作用；
4. 最终就是考虑如何对不同的store&date对的visitors和reserve_visitors进行整合的问题；

终极目的：预测某一天某家店的顾客数量，开开脑洞，如何用现有的两份数据visit和reserve更好的进行预测，之前只用visit得到0.75；

到底该怎么整合两个在时间、店铺、target均不同的数据：
1. 从基础维度考虑，只要时间和店铺能对上就是ok的，目前看时间可以通过对缺失日期填充后得到同样一段连续的日期数据；
2. 店铺，这个问题比较大，reserve和visit中同样存在的只有333家(314%150)家，而不存在visit中存在reserve中的却有4000+家；
3. 对于visit的fe过程中看，每家店铺的数据分布也是不一致的，这不影响特征构建，顶多就是部分特征构建后在valid阶段可能会存在错误导致结果异常；
4. 如何将没出现在visit中的店铺的reserve数据链接到visit数据上？？？？

不再通过store&date链接visit和reserve，因为同样的store太少，如果通过date和店铺周围距离来链接，即对于visit中店铺A在日期2月3号的数据链接2在店铺A周围N米内的店铺(可能包含自身)在2月3号的各项reserve特征的统计值，比如count、mean等，这里计算量应该很大，需要考虑优化，在store数据最初，即计算在自己100米内的店铺的id，逗号拼接作为一个单独的特征，该特征传递到reserve中，在reserve中根据date分组后，每一组的每个store都可以找到自己100米内的店铺，取出来并在当前group中看有哪些store在自己100米内，取出，计算count、mean等数据，主要应该是count；

