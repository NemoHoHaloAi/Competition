# README

该竞赛分为两部分：
- [Wal-Mart零售商品的单位销售额](https://www.kaggle.com/c/m5-forecasting-accuracy)
- [Wal-Mart单位销售额的不确定性分布](https://www.kaggle.com/c/m5-forecasting-uncertainty)

## 销售额预测

目标：预测两个28天的时间段的不同门店不同商品的销售情况。

数据：使用沃尔玛的分层销售数据来预测明年的销售额，数据涵盖了美国三个州的门店，包括商品级别、部门、产品类别和门店详细信息、价格、促销、星期几和特殊事件。

评价指标：RMSSE

submission：每一行有29列，第一项表示商品&商店，其余项每一项代表某一天该商店的该商品的销量。

文件：
- calendar.csv - 包含有关商品的销售日期信息。
- sample_submission.csv - 提交格式文件。
- sell_prices.csv - 包含有关每个商店和日期销售的产品价格的信息。 
- sales_train_validation.csv - 每个商店的每个商品的每天销量的历史信息。
- sales_train_evaluation.csv - 比赛截止前一个月提供，包含销售额信息。

## 不确定分布预测

## EDA+baseline
