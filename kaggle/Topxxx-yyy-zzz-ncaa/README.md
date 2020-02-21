# NCAA疯狂三月胜负预测比赛

## 往期比赛获奖kernel分析

信息来源于[19年的nacc疯狂三月预测男子组](https://www.kaggle.com/c/mens-machine-learning-competition-2019/discussion)，选择19年原因是这是距离目前最近的一期，选择男子组是因为之前的EDA主要是针对男子组数据进行的；

### [第一名](https://www.kaggle.com/c/mens-machine-learning-competition-2019/discussion/89150)

注意到这里有一个问题，这个男子组的第一名，在女子组的比赛却是432/500的排名，看起来有点奇怪，因为按照之前的主观感受，男子组女子组数据结构类似，那么在特征工程方面的差异应该不大，那么出现这种情况的理由是什么呢？

#### 讨论分享内容

1. 18年女子组的raddar的分享是第一名的主要基础；
2. 运气对结果印象很大，模型选择上偏保守，利用了一些首轮信息；
3. 原来的raddar的模型中对于种子的策略，即1,2,3,4号种子，百分百击败13,14,15,16号种子，该kernel没有采用这种规则，他认为这在男子组中会出现较多意外情况，即黑马；
4. 最终结果中，对于3场首轮比赛，选择指定某只球队100%会赢的方式，使得排名大幅提供，最终夺冠，而作者也说明了，同样方式，在女子比赛中完全不适用，说明这个trick要小心使用；
5. [ncaa2019第一名的R脚本](https://github.com/salmatfq/KaggleMarchMadnessFirstPlace/blob/master/win_ncaa_men.R)
6. [raddar的nacc2018](https://www.kaggle.com/raddar/paris-madness)

#### [nacc 2018 raddar 的kernel分析](https://www.kaggle.com/raddar/paris-madness)

因为ncaa2019的第一名是基于raddar的kernel进行的，因此先从该kernel进行分析：
1. 数据：常规赛、锦标赛的基础、指标信息，种子数据，跟之前计划的类似，这三部分数据也是最直接与预测相关的；
2. 准备数据：
    1. 交换了个列的位置，原始的是赢的在前，输的在后，交换后反过来了；
    2. 改变了WLoc的含义为LLoc，改变名字为location；
    3. 将列名中的W改为T1，L改为T2，swap则是反过来，也就是在原始df中，T1为原来的赢的队，在swap的df中则为输的队；
    4. concat原始df和swap的df；
    5. 计算每一行的score diff；
3. 准备数据操作应用于常规赛和锦标赛数据上；
3. 特征工程：
    1. 锦标赛融合常规赛：
        1. 对于**常规赛**数据，以season、T1_TeamId(这里的T1其实是包含了胜负两只球队的)分组，并计算部分box列的**平均值**；
        2. 上述聚合结果重整为**T1**和**T2**两份；
        3. 上述两份结果分别merge到原始的**锦标赛**数据中，注意这里完成了常规赛与锦标赛两份数据的融合，融合方式是**原始的锦标赛+分组聚合统计的常规赛**；
    2. 常规赛最后14天信息：
        1. 截取常规赛最后14天的数据；
        2. 构建win字段表示输还是赢，并根据该字段，求胜率；
        3. 同样针对T1和T2，输赢是反过来的；
        4. merge到原始的锦标赛数据中；
    3. 构建常规赛effects：
        1. 保留常规赛赛季、队伍id、分差信息，与Seed数据链接；
        2. 通过sm.GLM.from_formula构建各个赛季的**球队质量**特征，这里应该是一个重点；
        3. 将球队质量merge到原始锦标赛数据；
    4. 构建种子信息：
        1. 拆分出**种子号**；
        2. 分别构建两支球队的种子号特征，以及**种子号差**；
        3. merge到原始锦标赛数据；
4. 建模：
    1. y设置为两支球队的**分差**；
    2. x为之前几步的**特征集合**(注意这里相当于做了特征选择，很多原始特征都被直接去掉了)；
    3. 模型选择xgboost；
    4. n轮xgboost的cv；
    5. n轮kfold训练，预测结果clip到-30和30；
    6. 结果规整为**0**和**1**；
    7. 对规整后结果做**clip**；
    8. 对clip后结果根据两只球队的种子号做**规则处理**，即1~4有100%几率击败13到16，这个trick要小心使用；
    9. 在raddar的数据中，对于8的处理，意外情况只有一条，那么理论上这个trick就是可以使用的；
5. submission：
    1. 针对test数据构建与训练一致的数据结构；
    2. 模型预测、施以规则、输出结果；

#### 小结

特点：特征工程+规则，特征工程主要由分组聚合求mean、最后14天胜率、球队质量组成；

### [第二名](https://www.kaggle.com/c/mens-machine-learning-competition-2019/discussion/88805)

#### 讨论分享内容

1. [kenpom的调整进攻效率、调整防守效率、赛程力度](http://www.kenpom.com/index.php?y=)，这部分数据是通过外部网站获取的；
2. 使用了几组不同的排名信息；
3. 比赛数据，赛季篮板、最后30场比赛、罚球率百分比变化等；
4. 种子差；

#### [代码](https://github.com/gjwierz/NCAA_Kaggle_2019/blob/master/Kaggle_Submission_NCAA_Tournament.R)


#### 小结

特点：大量的外部信息，尤其是各个来源的排名信息整合为最终的排名信息；

### [第三名](https://www.kaggle.com/c/mens-machine-learning-competition-2019/discussion/90254)

#### 讨论分享内容

1. 第一版模型只使用队伍id以及胜利时的分数，模型使用线性回归扩展，没有使用boxscore，认为这类统计数据会对结果产生干扰；
2. 对胜负率接近(64% to 36%)的比赛进行flip；
3. 随机预测，对模型预测结果小于77%的情况，对ID小的球队直接指定其胜率为64%，或者对ID大的球队指定，这么做有效的原因是logloss的评估函数；

#### [代码](https://github.com/YouHoo0521/kaggle-march-madness-men-2019)

#### 小结

特点：对于结果中势均力敌的情况，比如结果为0.427，认为是不可预测的，直接预测teamid大的获胜，或者小的获胜；

### [第四名](https://www.kaggle.com/c/mens-machine-learning-competition-2019/discussion/89645)

#### 讨论分享内容

1. 针对每个球队的12个特征，因此结果文件中是24个特征：
    - Ken Pom赛季末排名
    - Ken Pom效率裕度
    - Ken Pom进攻效率
    - Ken Pom防守效率
    - Ken Pom ’幸运‘
    - 常规赛战胜排名前25的球队
    - 常规赛平均分差
    - 常规赛场进球率
    - 常规赛三分球命中率
    - 2004-2018年期间球队是否参加20多场比赛的二元指标
    - 团队是否在ACC、B10、B12或SEC中的二元指标
    - 种子号
2. 建模：
    1. 测试了随机森利、xgboost、神经网络，神经网络表现好的多，因此没有考虑融合；
    2. 对16,17,18赛季数据做holdout；

#### 代码

#### 小结

1. 收集整理了04到19年常规赛、锦标赛数据，主要的篮球学家的指标(例如ken pom)；
2. 各种模型，神经网络表现最好；

### [第五名](https://www.kaggle.com/c/mens-machine-learning-competition-2019/discussion/89942)

#### 讨论分享内容

特征按重要性排名：进攻效率、防守效率、获胜百分比、赛季前排名、学校是否在主要体育协会中；
