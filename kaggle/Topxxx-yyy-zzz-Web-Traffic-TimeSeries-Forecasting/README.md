# 网站流量预测

- [项目链接](https://www.kaggle.com/c/web-traffic-time-series-forecasting)
- [notebook](https://www.kaggle.com/holoong9291/web-traffic-time-series-forecasting)
- 目标：为145,000篇wiki文章预测流量；
- 评价函数：SMAPE；
- 数据：
    - train格式：每一行表示一篇wiki文章，文章名由名称+来源+访问类型(all、mobile、desktop、spider)+代理类型组成，其余每一列表示特定日期的访问流量，此处有缺失(数据集的数据源无法区分零流量值和缺失值)；
    - key格式：提供名称与用于预测的短id的对应关系；
    - sample_submission格式：提供提交的正确格式；
    - 注意：数据分为1和2两部分，分别对应第一阶段和第二阶段；
        - 第一阶段：
            - train：从2015年7月1日到2016年12月31日
            - test：以2017年1月1日至2017年3月1日
        - 第二阶段：
            - train：截至2017年9月1日
            - test：2017年9月13日至2017年11月13日，12号前提交，所以这部分是真实的未来数据
- 结果：由key可以生成，其中Id对应submission的Id，后面的Page中包含了所需预测的日期，需要拆分出来；
- [start with](https://www.kaggle.com/headsortails/wiki-traffic-forecast-exploration-wtf-eda)

## 备注

- 名称需要分割；
- 考虑用传统模型对数据缺失进行填充：传统模型不依赖过多特征过多数据，传统模型都是针对某一个物品进行预测，也适合这里分别对各个文章进行填充的需求；
