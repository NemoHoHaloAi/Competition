# README

[竞赛链接](https://www.kaggle.com/c/favorita-grocery-sales-forecasting/rules)

[GettingStart](https://www.kaggle.com/ceshine/lgbm-starter)

## Competition Background

实体店的采购与销售是敏感且影响很大的一对因素：
- 预测多了一点，商品会堆积，甚至过期产生成本；
- 预测少了一点，热门商品会售空，顾客会感到不满；

而由于实体店不停增加的新的店面、新产品、新的营销策略等，预测变得很困难，希望能够通过构建模型来实现很准确的预测，从而达到采购-销售平衡；

## 评价函数

Normalized Weighted Root Mean Squared Logarithmic Error：加权的RMSLE；

## 数据源

- train.csv：
  - 训练数据；
  - 4.65G+；
  - `unit_sales`：目标字段，表示每天每个商店每个商品的销量，对应一个unique的`id`，这个值可以是整型，比如1袋，可以是浮点型，比如1.5公斤，负数表示退货；
  - `onpromotion`：表示指定商品是否处于特定日期或商店的促销活动中，约16%为NaN；
  - 注意：
    1. 训练数据总不包含销量为0行；
    2. 没有关于商品在当前是否有库存这样的信息；
    3. 需要考虑这种情况；
    4. 训练中的部分item没有出现在测试中；
- test.csv：
  - 测试数据；
  - 120M+；
  - `date`, `store_nbr`, `item_nbr`, `onpromotion`；
  - 注意：测试数据中存在没有出现在训练数据中的商品，如何用同类商品进行辅助预测是很重要的一个点；
- sample_submission.csv：
  - 建议压缩后上传；
- store.csv：
  - 商店数据；
  - 包含：`city`, `state`, `type`, and `cluster`；
  - `cluster`：是相似店铺的一个群组；
- items.csv：
  - 商品数据；
  - 包含：`family`, `class`, and `perishable`；
  - `perishable`：表示是否是易腐品，该类权重为1.25，其他为1.0；
- transactions.csv：
  - 每天每个商店的销量；
- oil.csv：
  - 每日油价数据；
  - 厄瓜多尔是石油国家，因此整体经济非常依赖石油价格的走势；
- holidays_events.csv：
  - 假日、事件数据；
  - 注意转移放假日，比如1号的节日，3号放假，那么应该更看重3号，关于Bridge的是额外的放假日期；
  - 额外的假日通常指一个工作日放假；
- 其他信息：
  - 厄瓜多尔国营单位每个月15号和最后一天发放工资；
  - `2016年4月16日`这一天厄瓜多尔发生地震，很多人向超时捐水和食物等，这一特殊事件对销量有很大影响；
