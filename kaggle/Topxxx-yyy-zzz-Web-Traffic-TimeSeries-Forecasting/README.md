# 网站流量预测

- [项目链接](https://www.kaggle.com/c/web-traffic-time-series-forecasting)
- [notebook](https://www.kaggle.com/holoong9291/web-traffic-time-series-forecasting)
- 目标：为145,000篇wiki文章预测流量；
- 评价函数：SMAPE；
- 数据：
    - train格式：每一行表示一篇wiki文章，文章名由名称+来源+访问类型+代理类型组成，其余每一列表示特定日期的访问流量，此处有缺失；
    - key格式：提供名称与用于预测的短id的对应关系；
    - sample_submission格式：提供提交的正确格式；
    - 注意：数据分为1和2两部分，分别对应第一阶段和第二阶段；
- [start with](https://www.kaggle.com/headsortails/wiki-traffic-forecast-exploration-wtf-eda)
