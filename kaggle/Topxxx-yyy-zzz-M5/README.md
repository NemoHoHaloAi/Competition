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

### EDA+baseline

0. [EDA 中英文](https://www.kaggle.com/holoong9291/eda-for-m5-en)
1. [baseline with prophet 中英文](https://www.kaggle.com/holoong9291/simple-baseline-with-prophet-en)
2. [baseline with ml](https://www.kaggle.com/holoong9291/baseline-with-ml)

### BASELINE 分析

#### Base on Prophet

目前没有进行参数调优，仅针对不同的数据集大小进行训练，包括最近一年、全部、最近两年(训练中)；

#### Base on ML

Base on 一个public的kernel，LB为0.84918，目前开放kernel中最好的分数；

流程整理：
1. 数据整理：
    1. 数据加载；
    2. 数据结构调整及合并，同时进行数据大小压缩；
    3. 最终结构：31681090 rows and 18 columns；
2. 转换：
    1. 以“unknown”填充事件相关4个字段的缺失；
    2. copy id字段，并label encode处理；
    3. 所有id和event字段做label处理；
3. FE:
    1. 需求的lag、rolling特征；
    2. 价格的rolling、lag、change特征；
    3. 基础的时间数据提取；
4. 训练模型：
    1. 模型选择lgb；
    2. round 2500, early stop 50；
5. 预测并生成结果文件；

优化：
1. FE部分：
    1. 平均编码特征，例如每天平均商品销量，结合各个维度，例如商店、州、其他id等；
    2. 趋势特征，包括商品销量趋势以及价格趋势；
    3. 第一次、上一次售出时间长度；
    4. xxxxx；

## 不确定分布预测
