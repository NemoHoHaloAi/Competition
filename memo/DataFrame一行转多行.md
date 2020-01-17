问题假设：
> info是一个dataframe，其中有一列city中包含有带空格的数据，这一类数据需要切分开当做两个city来处理；

代码：
```python
city = info['city'].str.split(' ', expand=True).stack().reset_index(level=1, drop=True).rename('city')
info.drop(['city'], axis=1).join(city)
```

代码分析：
1. str.split - 对字符串city按照空格划分，这里会得到两列
2. stack - 列转行
3. reset_index - 此时index是二级的，reset掉
4. rename - 对当前的series进行rename
5. 通过join将N条数据按照index连接到原来长度为n的dataframe中，最终长度为N，N>=n
