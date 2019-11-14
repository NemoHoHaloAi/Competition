# [NFL大数据碗](https://www.kaggle.com/c/nfl-big-data-bowl-2020/overview/timeline)

## Attention

1. 该竞赛数据是**实时**产生的，通常每周四、周日、周一进行，之后会更新数据，这里要注意；
2. 提交方式为代码，且满足以下条件：
    - CPU<=4小时运行时间
    - GPU已禁用
    - 未启用internet访问
    - 不允许外部数据

详细提交要求参考：https://www.kaggle.com/dster/nfl-big-data-bowl-official-starter-notebook

## Competition Background

通过建立更好的模型，来预测对一个达阵最重要的因素是什么？

概念：
- 美式足球：进攻方基本目的是通过跑动、传球等尽快抵达对方半场，也就是达阵，而防守方的目的则是相反，尽全力去阻止对方的前进以及尽可能断球；
- 球员：双方场上共22人；
- 影响因素：带球者（四分卫?）、队友、教练、对手；
- handoff：传球
- snap：发球
- [基本知识](https://www.douban.com/note/321101362/)

BTW: I like `The Blind Side`;

## 相关图片

NFL：

![NFL](https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike933%2C5%2C5%2C933%2C330/sign=4b109f3b17950a7b613846966bb809bc/8326cffc1e178a82be19bbadfc03738da977e892.jpg)

位置图：

![位置图](https://img3.doubanio.com/view/note/large/public/p10518112.jpg)

## Deathline

`2019-11-27`:停止submit；

## Data DESC

数据中的每一行代表某个球员在某场比赛中的表现；

字段信息：
- `GameId` - a unique game identifier - 比赛ID
- `PlayId` - a unique play identifier - 
- `Team` - home or away - 主场还是客场
- `X` - player position along the long axis of the field. See figure below. - 在球场的位置x
- `Y` - player position along the short axis of the field. See figure below. - 在球场的位置y
- `S` - speed in yards/second - 速度，码/秒
- `A` - acceleration in yards/second^2
- `Dis` - distance traveled from prior time point, in yards
- `Orientation` - orientation of player (deg)
- `Dir` - angle of player motion (deg)
- `NflId` - a unique identifier of the player - NFL球员ID
- `DisplayName` - player's name - 球员名
- `JerseyNumber` - jersey number - 球衣号码
- `Season` - year of the season
- `YardLine` - the yard line of the line of scrimmage
- `Quarter` - game quarter (1-5, 5 == overtime) - 当前是第几节比赛，5为加时
- `GameClock` - time on the game clock - 比赛时间
- `PossessionTeam` - team with possession - 持球方
- `Down` - the down (1-4) - 达阵
- `Distance` - yards needed for a first down - 距离第一次达阵所需距离
- `FieldPosition` - which side of the field the play is happening on
- `HomeScoreBeforePlay` - home team score before play started - 赛前主队分数
- `VisitorScoreBeforePlay` - visitor team score before play started - 赛前客队分数
- `NflIdRusher` - the NflId of the rushing player
- `OffenseFormation` - offense formation
- `OffensePersonnel` - offensive team positional grouping
- `DefendersInTheBox` - number of defenders lined up near the line of scrimmage, spanning the width of the offensive line
- `DefensePersonnel` - defensive team positional grouping
- `PlayDirection` - direction the play is headed
- `TimeHandoff` - UTC time of the handoff
- `TimeSnap` - UTC time of the snap
- `Yards` - the yardage gained on the play (you are predicting this) - **目标**
- `PlayerHeight` - player height (ft-in) - 球员身高
- `PlayerWeight` - player weight (lbs) - 球员体重
- `PlayerBirthDate` - birth date (mm/dd/yyyy) - 生日、岁数
- `PlayerCollegeName` - where the player attended college - 大学
- `Position` - the player's position (the specific role on the field that they typically play) - 场上位置
- `HomeTeamAbbr` - home team abbreviation - 主队缩写
- `VisitorTeamAbbr` - visitor team abbreviation - 客队缩写
- `Week` - week into the season
- `Stadium` - stadium where the game is being played - 体育场
- `Location` - city where the game is being player - 城市
- `StadiumType` - description of the stadium environment - 体育场类型
- `Turf` - description of the field surface - 草皮
- `GameWeather` - description of the game weather - 比赛天气
- `Temperature` - temperature (deg F) - 温度
- `Humidity` - humidity - 湿度
- `WindSpeed` - wind speed in miles/hour - 风速
- `WindDirection` - wind direction - 风向

## Define Problem

回归预测，Target是码数，但是最终结果需要转换为条件概率分布；

## Evaluation Function

Continuous Ranked Probability Score (CRPS)；

## Start from Gert\`s Kernel

Kernel Link: https://www.kaggle.com/gertjac/regression-approach

## 4 milestone

1. 直接提交Gert的kernel；
2. 不考虑太多橄榄球相关业务情况，只进行基础处理；
3. 加入对橄榄球的理解 - 主要指FE部分；
4. 优化模型算法；

## WorkPlan

1. Fork with [Gert\`s kernel](https://www.kaggle.com/gertjac/regression-approach);
2. Submit by myself kernel as baseline;
3. Preprocess
    1. missing value
    2. outlier
    3. something else
        1. age
        2. time series
        3. ....
4. EDA
5. FE
6. Modeling
7. Stack or something
