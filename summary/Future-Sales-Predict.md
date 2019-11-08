# [Future Sales Predict](https://www.kaggle.com/holoong9291/predict-future-sales)

1. 当日售出数量、商品价格中的异常极值处理，通过可视化，明显离群的两个点，需要去除；
2. 商店名字有重复，这里不要假设这些信息都是没问题的，这里有名字重复但是ID不同的情况，要归一处理，这些需要不带假设的去分析数据才能发现；
3. Matrix是配合test数据做的结构重组后的样子，因此数据量达到1000w+，这种数据处理方式之前的项目中没有遇到，算是TS中第一次出现（Rossmann中都没有）；
4. TS数据中通常会构建lag特征，比如为每条数据新增昨天、上周今天、上个月今天等周期性的对应日子的销售情况，作为当前数据的重要参考特征；
5. lag后的数据通常会存在某一段数据中某些特征均为NaN，比如特征为去年今天的销量，那么第一年的数据则没有该特征，那么此时如果该特征为重要特征，可以考虑直接删掉第一年的数据；
6. 计算商品上一次最后售出、第一次售出是多久前，这个特征应该是TS的销售领域比较常用且有效的；
7. 连续数据分布转换时，对比下对数、指数、幂函数、box-cox等转换方法，并通过偏度、峰度来决定，主要是偏度，越接近0越好，0为标准正太，峰度为3为正态；
8. 数据转换中出现的boxcox结果skew大于原始的问题，因为测试数据中大量fill了0，导致数据正偏太严重，无法正常转换，因此这一步应该做到预处理部分；
9. 数据转换位置很关键，目前是放在concat test前，避免被test的0干扰，同时对matrix和train的连续特征做了转换，target用的是log1p，方便恢复；
10. 模型堆叠：


## 整个流程中数据结构的变化

0. 原始数据结构：
    - train:date(年月日)、date_block_num(月份累计)、shop_id(商店id)、item_id(商品id)、item_price(商品价格)、item_cnt_day(日销量);
    - test:ID(提交ID，作为Index)、shop_id(商店id)、item_id(商品id);
    - shop:shop_id(商店id)、shop_name(商店名);
    - item:item_id(商品id)、item_name(商品名)、item_category_id(类别id);
    - cat:item_category_id(类别id)、item_category_name(类别名);
1. 预处理：
    1. 异常处理：价格、日销量、商店名，不影响结构；
    2. 提取城市、type、subtype：
        - shop:shop_id、city_code;
        - cat:item_category_id、type_code、subtype_code;
        - item:item_id、item_category_id;
    3. 以train为基础构建以月为维度的数据体，来匹配测试数据：
        - matrix:date_block_num、shop_id、item_id，结构为训练数据的这三个特征的所有取值的排列组合;
    4. 增加销售额特征：
        - train:增加revenue(销售额，等于price\*cnt_day);
    5. 基于train增加月销量特征到matrix：
        - matrix:增加item_cnt_month(月销量，train中每个block,shop,item的组合的所有数据求和的结果，nan填充为0，clip到0~20);
    6. test增加item_block_num特征：
        - test:增加item_block_num(顺延为34);
    7. matrix中拼接test数据，按照(block,shop,item)，item_cnt_month用0填充，不影响结构；
    8. matrix组合shop,item,cat：
        - matrix:增加city_code,item_category_id,type_code,subtype_code;
2. 特征工程：
    1. 基于item_cnt_month构建相应的lag特征：
        - matrix:item_cnt_month_lag_(1,2,3,6,12);
    2. 增加平均编码特征：
        1. 每个月的平均销量：matrix:增加date_avg_item_cnt_lag_1;
        2. 每个月每个商品的平均销量：matrix:增加date_item_avg_item_cnt_lag_(1,2,3,6,12);
        3. 每个月每家店的平均销量：matrix:增加date_shop_avg_item_cnt_lag_(1,2,3,6,12);
        4. 每个月每个类别的平均销量：matrix:增加date_cat_avg_item_cnt_lag_1;
        5. 每个月每家店每个类别的平均销量：matrix:增加date_shop_cat_avg_item_cnt_lag_1;
        6. 每个月每家店每个type的平均销量：matrix:增加date_shop_type_avg_item_cnt_lag_1;
        7. 每个月每家店每个subtype的平均销量：matrix:增加date_shop_subtype_avg_item_cnt_lag_1;
        8. 每个月每个城市的平均销量：matrix:增加date_city_avg_item_cnt_lag_1;
        9. 每个月每个城市每个商品的平均销量：matrix:增加date_item_city_avg_item_cnt_lag_1;
        10. 每个月每个type的平均销量：matrix:增加date_type_avg_item_cnt_lag_1;
        11. 每个月每个subtype的平均销量：matrix:增加date_subtype_avg_item_cnt_lag_1;
    3. 趋势特征：
        1. 最后6个月的商品价格趋势：
            - item_avg_item_price 每个商品平均价格
            - date_item_avg_item_price 每个月每个商品的平均价格
            - date_item_avg_item_price lag [1,2,3,4,5,6] 每个月每个商品的平均价格的lag
            - delta_price_lag_[1,2,3,4,5,6] = (date_item_avg_item_price_lag_[1,2,3,4,5,6] - item_avg_item_price) / item_avg_item_price
            - delta_price_lag = delta_price_lag_[1,2,3,4,5,6]中最近的有值的那个，或者0
        2. 最后一个月的商品销售额趋势：matrix:增加delta_revenue_lag_1，表示((每月每个店总销售额 - 每个店的平均销量) / 每个店的平均销量)
    4. 其他特征：
        1. 月份天数：matrix增加month,days;
        2. 每个商店的每个商品上一次售出是几个月前：matrix增加item_shop_last_sale;
        3. 每个商店的每个商品第一次售出是几个月前：matrix增加item_shop_first_sale;
        4. 每个商品上一次售出是几个月前：matrix增加item_last_sale;
        5. 每个商品第一次售出是几个月前：matrix增加item_first_sale;
    5. 连续特征分布转换：不影响结构；
    6. 删减处理：不影响结构；
3. 建模；
