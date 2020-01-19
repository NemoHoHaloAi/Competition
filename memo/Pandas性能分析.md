# Pandas性能分析

集中在CPU、内存、速度方面；

## 速度

### 数据的读取与存取

在`Pandas`中内置了众多的数据读取函数，可以读取众多的数据格式，最常见的就是`read_csv`函数从**csv**文件读取数据了。但`read_csv`在读取大文件时并不快，所以建议你使用`read_csv`读取一次原始文件，将`dataframe`存储为**HDF**或者**feather**格式。一般情况下**HDF**的读取比读取**csv**文件快几十倍，但**HDF**文件在大小上会稍微大一些。

> **建议1**：尽可能的避免读取原始csv，使用hdf、feather或h5py格式文件加快文件读取；

### 按行迭代：itertuples与iterrows

`itertuples`和`iterrows`都能实现按行进行迭代的操作，但在任何情况下`itertuples`都比`iterrows`快很多倍。

![itertuples vs iterrows](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%5Bb%5D%7B%7Cc%7Cc%7C%7D++%5Chline%E8%A1%A8%E6%A0%BC%E8%A1%8C%E6%95%B0+%261K%E8%A1%8C%26+10K%E8%A1%8C%26100K%E8%A1%8C%261000K%E8%A1%8C%5C%5C++%5Chline+iterrows%E6%80%BB%E7%94%A8%E6%97%B6+%26+58ms%26361ms%263.06s%2630.3s%5C%5C+%5Chline+itertuples%E6%80%BB%E7%94%A8%E6%97%B6+%26+8ms%2617ms%2658ms%26577ms%5C%5C+%5Chline++%5Cend%7Barray%7D%5C%5C)

> **建议2**：如果必须要要用`iterrows`，可以用`itertuples`来进行替换。

### 传播方法：apply、transform和agg时尽量使用内置函数

在很多情况下会遇到`groupby`之后做一些统计值计算，而如果用内置函数的写法会快很多。

- transform() 方法+自定义函数，用时1分57s；
![transform + custome method](https://pic1.zhimg.com/80/v2-f5904ee81b339402f75b7a3753f4100c_hd.jpg)
- transform() 方法+内置方法，用时712ms；
![transform + buildin method](https://pic1.zhimg.com/80/v2-e610e7d4df872cc6a45cdad8683fc03c_hd.jpg)
- agg() 方法+自定义函数，用时1分2s；
![agg + custome method](https://pic1.zhimg.com/80/v2-3a0cea2593791d3862d494a169b1983c_hd.jpg)
- agg() 方法+内置方法，用时694ms；
![agg + buildin method](https://pic4.zhimg.com/80/v2-b45b306e229a97a74544537c2257b7c3_hd.jpg)

> **建议3**：在`groupby`、`agg`和`transform`时尽量使用**内置函数**计算。

### 第三方库并行库优化Pandas单核问题

由于`Pandas`的一些操作都是单核的，往往浪费其他核的计算时间，因此有一些第三方库对此进行了改进：

- modin：对读取和常见的操作进行并行；
- swifter：对apply函数进行并行操作；
- joblib：sklearn的并行模块；

> **建议4**：如果能并行就并行，用第三方库或者自己手写多核计算。

### 尽量使用category类型代替object

在多数情况下，只要列不是id之类取值与行数基本一致的情况，类似gender、type等都是使用category不管是内存占用还是cpu运算速度，都要明显优于object；

> **建议5**：使用category代替object；

## 内存

常见内存问题处理方式：
1. 数值类型的字段可以downcast；
2. 字符类型的字段可以转换为category；
3. 设置chunksize参数，进行分块处理；
4. 导出数据集时选择压缩；

### 指定列类型加载

在`pandas`读取数据的同时，指定列类型加载，可以有效减少内存占用（比如int，不指定默认为int64，最低可以指定为int8），但是要注意，携带NaN的字段无法指定底类型（应该是`pandas`认为未知数具有最大当前类型的保守做法，一种处理方法是将NaN填充后，再进行downcast）；

> **建议1**：尽量在加载的同时指定范围内最低的类型；

### 使用Category类型

例如性别字段，可能原始值为“男”、“女”，而string在`pandas`中占空间是很大的，而且其实取值只有两种，这种情况下建议用Category代替string，注意如果每个string各不相同，那这种指定是没有意义的，可以理解为Category只保存了一份“男”“女”，每个取值都是指向这两个值的指针；

> **建议2**：对于类别字段，尽量使用Category代替string；

## CPU

## 磁盘

## 参考链接

1. https://zhuanlan.zhihu.com/p/81554435
2. https://blog.csdn.net/zhusongziye/article/details/92064823
3. https://www.cnblogs.com/zry-yt/p/11803892.html#_label3_5
