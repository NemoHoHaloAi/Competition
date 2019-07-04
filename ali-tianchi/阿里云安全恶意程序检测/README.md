# [安全恶意程序检测](https://tianchi.aliyun.com/competition/entrance/231694/introduction)

## 赛题背景
恶意软件是一种被设计用来对目标计算机造成破坏或者占用目标计算机资源的软件，传统的恶意软件包括蠕虫、木马等，这些恶意软件严重侵犯用户合法权益，甚至将为用户及他人带来巨大的经济或其他形式的利益损失。近年来随着虚拟货币进入大众视野，挖矿类的恶意程序也开始大量涌现，黑客通过入侵恶意挖矿程序获取巨额收益。当前恶意软件的检测技术主要有特征码检测、行为检测和启发式检测等，配合使用机器学习可以在一定程度上提高泛化能力，提升恶意样本的识别率；

## 赛题说明
本题目提供的数据来自文件（windows 可执行程序）经过沙箱程序模拟运行后的API指令序列，全为windows二进制可执行程序，经过脱敏处理；

本题目提供的样本数据均来自于从互联网，其中恶意文件的类型有感染型病毒、木马程序、挖矿程序、DDOS木马、勒索病毒等，数据总计6亿条；

## 数据说明
**训练数据**（train.zip）：调用记录近9000万次，文件1万多个（以文件编号汇总），字段描述如下：

字段 | 类型 | 解释
-|-|-
file_id | bigint | 文件编号
label | bigint | 文件标签，0-正常/1-勒索病毒/2-挖矿程序/3-DDoS木马/4-蠕虫病毒/5-感染型病毒/6-后门程序/7-木马程序
api | string | 文件调用的API名称
tid | bigint | 调用API的线程编号
index | string | 线程中API调用的顺序编号

- 注1：一个文件调用的api数量有可能很多，对于一个tid中调用超过5000个api的文件，我们进行了截断，按照顺序保留了每个tid前5000个api的记录。
- 注2：不同线程tid之间没有顺序关系，同一个tid里的index由小到大代表调用的先后顺序关系。
- 注3：index是单个文件在沙箱执行时的全局顺序，由于沙箱执行时间有精度限制，所以会出现一个index上出现同线程或者不同线程都在执行多次api的情况，可以保证同tid内部的顺序，但不保证连续。
 
**测试数据**（test.zip）：调用记录近8000万次，文件1万多个。
> 说明：格式除了没有label字段，其他数据规格与训练数据一致。

## 评测指标
- 选手的结果文件包含9个字段：file_id(bigint)、和八个分类的预测概率prob0, prob1, prob2, prob3, prob4, prob5 ,prob6,prob7 (类型double，范围在[0,1]之间，精度保留小数点后5位，prob<=0.0我们会替换为1e-6，prob>=1.0我们会替换为1.0-1e-6)。选手必须保证每一行的|prob0+prob1+prob2+prob3+prob4+prob5+prob6+prob7-1.0|<1e-6，且将列名按如下顺序写入提交结果文件的第一行，作为表头：file_id,prob0,prob1,prob2,prob3,prob4,prob5,prob6,prob7。

- 分数采用logloss计算公式

## 借鉴高分kernel分享的思路、以及后续工作安排：

**所以，所谓程序的api调用时序可以理解为程序说的一句话，不同的程序说了不同的话，对这些话进行分类，也就区分开了不同的程序类型；**

在安全算法竞赛中，我们将任务归结为NLP域中具有词序的文本分类问题。首先，对原始数据进行特征提取，
利用自然语言处理和统计学习方法进行特征工程。
特征工程的主要特点是提取三组数据，API、TID、INDEX。
然后利用LGB和CNN方法构建模型。最后，利用LGB、CNN及其融合方法对测试集进行预测。
实验结果表明，LGB与CNN的融合方法可以达到最佳效果，为0.443705。

提取：
- 重要原始特征：API、TID、INDEX；
- 算法：LGB、CNN，模型融合提高泛化能力；



本课程设计提供的数据来自于由沙盒程序模拟的文件（Windows可执行程序）的API指令序列。
它们都是Windows二进制可执行程序，并且是不敏感的。
其中，恶意文件类型有传染性病毒、木马程序、挖掘程序、ddos木马、勒索病毒等，共有6亿数据。
每个文件都有几个API调用，并且API之间可能存在一些序列关系。
同时，api可以看作是一个词，文件的api调用是一个文本，
所以需要解决的分类问题可以看作是一个在nlp字段中具有词序的文本分类问题。 
我们认为可以从这些方面来研究我们的比赛，
并提出以下方法： 
1. NLP域中的文本词汇带模型建模 
2. 统计机器学习中的传统统计特征建模与分析 
3. 深度学习领域中时间序列建模的训练模型

提取：
- API时序序列关系（跟想的一样，很重要，这表示了程序代码是在做什么）
- 将api看做单词，那么文件的api调用就是一段文本
- 看做是文本分类问题（根据词序，比如nlp中的区分文本类型：八卦、实事、体育等，这里是分为正常、病毒等）


两种思路：
- 以统计特征为基础，结合过抽样，分类算法选择kNN等传统机器学习；
- 看做是nlp的文本分类问题（TF-IDF），算法可以是传统机器学习LR、GBDT等，可以是CNN等深度学习；

关于TF-IDF：
- TF：词频统计；
- IDF：逆文本频率指数，即一个词出现次数越少，越能标示某一类文本；

几个相关链接：
- https://tianchi.aliyun.com/notebook-ai/detail?spm=5176.12586969.1002.3.75c867b5PiAURi&postId=56989
- https://www.jianshu.com/p/dc00a5d597ed
- https://github.com/brightmart/text_classification


两种思路后续工作：
- 统计方法的特征构建：过抽样部分，不要对valid数据做过抽样，生成test预测结果并提交（关注在是直接得出0/1结论，还是通过k中的结果计算概率）；
- 基于TF-IDF方法：开启；

## 工作安排
### 20190702:
- 修复过抽样导致的过拟合问题：
	- 原来的操作：
		1. 过抽样；
		2. 划分数据集；
	- 修复：
		1. 去除过抽样；
- 增加logloss评价指标；
- 预演用户商品推荐项目；

### 20190704-恶意程序深度特征挖掘

特征的二维组合：

Feature|Feature_Name|DESC|
-|-|-
File_id+Api(tid)|count,identification|File+Api组合的数量以及其类别个数
File_id+Api(index)|identification,min,max,median,std|每个index对应的file+api类别个数、最小最大值、中值、标准差
File_id+Index(api)|count,idendification|File+Index组合的数量以及其类别个数
File_id+Index(tid)|identification,min,max,median,std|每个tid对应的file+index类别个数、最小最大值、中值、标准差

特征的三维组合：

Feature|Feature_Name|DESC|
-|-|-
File_id+Api+Tid(index)|identification,min,max,median,std|每个tid对应的file+api+tid的类别个数、最小最大值、中值、标准差
File_id+Tid+Api(index)|identification,min,max,median,std|每个tid对应的file+api+api的类别个数、最小最大值、中值、标准差

参考代码：

	def feature_combination(data_merge, data_orig, combination_feature, col1=None, col2=None, opts=None):
	    for opt in opts:
		# print(opt)
		train_split = data_orig.groupby(['file_id', col1])[col2].agg(
		    {'fileid_' + col1 + '_' + col2 + '_' + str(opt): opt}).reset_index()

		train_split_ = pd.pivot_table(train_split, values='fileid_' + col1 + '_' + col2 + '_' + str(opt),
					      index=['file_id'], columns=[col1])
		new_cols = ['fileid_' + col1 + '_' + col2 + '_' + opt + '_' + str(col) for col in train_split_.columns]

		combination_feature.append(new_cols)
		train_split_.columns = new_cols

		train_split_.reset_index(inplace=True)

		data_merge = pd.merge(data_merge, train_split_, how='left', on='file_id')
	    return data_merge, combination_feature
