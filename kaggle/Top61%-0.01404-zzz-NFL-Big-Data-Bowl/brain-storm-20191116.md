# 脑暴 - 2019/11/16

```Python

根据项目的start notebook，提交测试集方式如下：

for 22 in test_set:
  每次取到22条数据，也即是一帧的数据
  预测结果为一条即可，也就是这一帧对应的推进码数
  这样看来还是需要对原始数据做聚合的，聚合方式同样也应用到测试数据上，包括各种填充、类型转换、新特征构建、聚合这四类操作；

聚合放在何处比较合适呢？
1. 预处理
2. EDA
3. FE
3. 聚合
4. 建模

聚合方式是啥？
Gert的notebook是直接去掉rusher以外的数据，只保留这一条，其实大部分都是重复的，比如Team这种，确实可以去掉一些

对于Yards来说，什么最重要？
- 进攻方信息
- 防守方信息
- 目前是主队还是客队进攻
- rusherid
- 球场信息（直接保留一份即可）
- 

什么是rusher以外的row可以提供的呢？？？不可能没有挖掘的点啊
球员个人信息，只有这一部分是不共享到每个row，且是每个row不同的，包括：
  X - player position along the long axis of the field. See figure below. - 在球场的位置x
  Y - player position along the short axis of the field. See figure below. - 在球场的位置y
  S - speed in yards/second - 速度，码/秒
  A - acceleration in yards/second^2
  Dis - distance traveled from prior time point, in yards
  Orientation - orientation of player (deg)
  Dir - angle of player motion (deg)
  DisplayName - player's name - 球员名
  JerseyNumber - jersey number - 球衣号码
  PlayerHeight - player height (ft-in) - 球员身高
  PlayerWeight - player weight (lbs) - 球员体重
  PlayerBirthDate - birth date (mm/dd/yyyy) - 生日、岁数
  PlayerCollegeName - where the player attended college - 大学
  Position - the player's position (the specific role on the field that they typically play) - 场上位置

全局：
胜率、对决胜率，总共是多少场比赛啊，各个球队总共比了多少场，构建这部分全局特征：
- 总胜率
- 主场胜率
- 客场胜率
- 是否对过当前这个对手，是的话赢了多少场，没对过就是0，赢得多就是正数，反之是负数
- 上一场是输还是赢 这个要看测试数据给出的是否是一场接一场，输是-1，赢是1，没有上一场是0

22个球员的信息：
1. XY：22个球员的XY位置，对方在rusher路径上的人的位置、距离
2. S：速度 整体速度分布、rusher速度，对方针对rusher的那个人的速度，防守锋线速度，进攻锋线速度 平均
3. A：加速度 与S一致 平均
3. Orientation、Dir
4. 身高体重 平均
5. 岁数 平均
6. 场上位置

犯规信息：
1. 犯规是会给对方码数的；

其他：
OffenseTime - 这个没法用到测试集上，放弃
是否进入突然死亡阶段

如果三次down后所需码数很多，那么通常选择手抛球到对方半场；


维度：球队-进攻队形-进攻组-防守队形-防守人数-防守组
当前进攻组平均推进码数
当前防守组平均(被)推进码数
当前进攻组、防守组推进码数

这个数据不一定有是个问题，目前测试数据是22条的给的，也就是没法构建需要上下文其他数据的特征，那么能操作的也就是这22条；

每节结束后，双方换边；

弃踢：如果踢出界，那么对方开球点会比较靠前，因此应该是尽量靠近对方达阵区，但是不出界；

是否到了goal区，在这个区域，是不按照10码要求定的，必须4次内完成得分，达阵或者射门；
```
