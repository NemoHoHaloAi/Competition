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

挖挖挖：
1. XY：22个球员的XY位置
2. S：速度 整体速度分布、rusher速度
3. A：加速度 与S一致
3. Orientation、Dir
4. 身高体重
5. 岁数
6. 场上位置
```
