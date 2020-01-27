# README

[竞赛链接](https://www.kaggle.com/c/demand-forecasting-kernels-only)

[Notebook](https://www.kaggle.com/holoong9291/store-item-demand-predict)

## Background

典型的商店-商品-日期预测问题，提供了一个相对干净的数据集，以探索各种模型、各种时序数据处理方式间的差异；

## Data

- train:
    - date
    - store
    - item
    - sales
- test:
    - id
    - date
    - store
    - item

## Evaluation

SMAPE：对称平均绝对百分比误差（Symmetric Mean Absolute Percentage Error）；

## Different Algorithm

- ARIMA
- prophet
- xgboost
- NN
