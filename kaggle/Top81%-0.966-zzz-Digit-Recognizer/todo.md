# TODO

## 0921
1. 构造特征 - check，测试
    - v-2.0：0.966；
2. 多模型
3. 模型融合 - 测试
4. 特征数据类型转换 - [内存问题](https://blog.csdn.net/zhusongziye/article/details/92064823)
    - 数值型（int、float）向下转换；
    - 字符型转为[Category](http://pandas.pydata.org/pandas-docs/stable/categorical.html)；
        - 编写一个循环函数来迭代式地检查每一 object 列中不同值的数量是否少于 50%；如果是，就将其转换成 category 类型；
5. 构造连续特征做转换 - 测试