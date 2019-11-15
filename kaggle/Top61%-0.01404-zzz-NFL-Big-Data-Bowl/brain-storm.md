# 脑暴

```Python
缺失值

- Orientation
- Dir
- FieldPosition
- OffenseFormation
- DefendersInTheBox
- StadiumType

df_train[df_train.NflId==496723].Orientation.plot()
df_train[df_train.NflId==496723].Dir.plot()

sns.lineplot(data=df_train[df_train.NflId==496723]["Orientation"].reset_index(), color="coral", label="line")

采样频率
df_train[df_train.NflId==496723].GameClock.head(100)

0         14:14:00
22        13:52:00
44        13:02:00
67        12:12:00
110       11:21:00
            ...   
492558    02:56:00
492580    01:32:00
492602    00:22:00
492668    08:58:00
492690    08:09:00


df_train[['GameId','PlayId','NflId']].head(1)

2017090700	20170907000118	496723

df_train.GameClock.unique()

array([20170907000118, 20170907000139, 20170907000189, 20170907000345,
       20170907000395, 20170907000473, 20170907000516, 20170907000653,
       20170907000680, 20170907000801, 20170907000917, 20170907001004,
       20170907001077, 20170907001156, 20170907001177, 20170907001296,
       20170907001355, 20170907001376, 20170907001443, 20170907001488,
       20170907001509, 20170907001530, 20170907001551, 20170907001605,
       20170907001664, 20170907001715, 20170907001736, 20170907001819,
       20170907001955, 20170907002430, 20170907002648, 20170907002669,
       20170907002829, 20170907002900, 20170907002961, 20170907003138,
       20170907003161, 20170907003261, 20170907003444, 20170907003465,
       20170907003507, 20170907003635, 20170907003874, 20170907004025,
       20170907004046, 20170907004182, 20170907004314, 20170907004465,
       20170907004486, 20170907004622, 20170907004660, 20170907004721])
       

df_train[['GameId','PlayId','NflId','NflIdRusher','GameClock','TimeSnap','TimeHandoff','Dis','Yards','Distance','Quarter','YardLine','FieldPosition']].head(44)

df_train[['GameId','PlayId','NflId','NflIdRusher','Team','PossessionTeam','FieldPosition','HomeTeamAbbr','VisitorTeamAbbr']].head(22)

print(df_train.X.min())
print(df_train.X.max())
print(df_train.Y.min())
print(df_train.Y.max())

print(len(df_train[df_train.GameId==2017090700]))
print(len(df_train[df_train.GameId==2017090700].groupby(['GameId','PlayId'])))
# 52

df_train[df_train.GameId==2017090700][['HomeTeamAbbr','VisitorTeamAbbr','PossessionTeam','PlayDirection','FieldPosition']].head(44)


TimeSnap TimeHandoff上看，这二者是前后关系，即发球后，接传球时间（似乎一般都是这样，由中锋传给四分卫，这两个时间间隔一般也就一两秒，主要持球的是四分卫，中锋负责发球）

如果这样说的话，一个PlayId表示的是一次进攻，GameClock是倒计时，一节是15分钟，因此是从15分钟倒计时到0为止，总共四节

对于数据结构更准确的描述：一场比赛（GameId）的一次进攻（PlayId）中，球队（Team）中的每个球员（NflId）在当前状况（比赛状况、球场状况、天气状况）下的信息展示；

也就是说对应一个GameId、PlayId对应22条数据（场上有22个球员）；

Distance最大为10，即每次进攻（4次机会）需要推进至少10码才能继续进攻；

YardLine意思是当前这次进攻最终停在了哪条线上，结合FieldPosition、PossessionTeam可以知道是哪只球队在进攻，以及目前的球场位置（球场是对称的，所以需要在哪一侧来定位）

PossessionTeam当前球权属于哪个队，对应是球队的缩写，这里可以跟主客队缩写对上

PlayDirection指的是进攻方向是向着哪边，如果是left，意思是目前是从右向左进攻

比赛过程中不会交换场地，这里跟其他运动不太像

# 将数据分组为每场比赛的每一节（4节，如果打平会加时1节）的每次进攻（4次进攻机会，比如推进10码）中22名球员与当前状态的数据
# 1场比赛
#     4~5节
#         两只球队轮流有4次进攻机会，推进10码
df_train.groupby(['GameId','Quarter','PlayId'])

matplotlib绘制22个球员（圈圈叉叉）、YardLine图，text显示distance、yards、Quarter、GameId、GameClock等信息，哇哦，So cool

# 统计码数和xy的位置，这里把码线+PossessionTeam结合得到一个0~120范围的码线


plt.figure(figsize=(30, 50))
subplot_len = len(df_train[df_train.GameId==2017090700].groupby(['GameId','PlayId']))
df_train_groupby_gp = df_train[df_train.GameId==2017090700].groupby(['GameId','PlayId'])
i=1

for gp,chance in df_train_groupby_gp:
    game_id,play_id = gp[0],gp[1]
    chance['TeamBelongAbbr'] = chance.apply(lambda row:row['HomeTeamAbbr'] if row['Team']=='home' else row['VisitorTeamAbbr'],axis=1)
    chance['Offense'] = chance.apply(lambda row:row['PossessionTeam']==row['TeamBelongAbbr'],axis=1)
    rusher = chance[chance.NflId==chance.NflIdRusher]
    offense = chance[chance.Offense]
    defense = chance[~chance.Offense]
    yard_line_left = offense.YardLine.iloc[0]+10 # yard_line 加10偏移量，这个10是左侧的达阵区
    yard_line_right = offense.YardLine.iloc[0]+2*(50-offense.YardLine.iloc[0])+10
    yard_line = yard_line_left if np.abs(yard_line_left-rusher.X.iloc[0])<=(yard_line_right-rusher.X.iloc[0]) else yard_line_right
    
    plt.subplot(subplot_len/4 if (subplot_len/4*4)==subplot_len else (subplot_len/4)+1,4,i)#, sharex=True, sharey=True)
    plt.xlim(0,120)# 0~120已经包含了达阵区，实际场内只有100码，码线也是0~100的范围
    plt.ylim(-10,63)
    plt.scatter(list(offense.X),list(offense.Y),marker='x',c='red',s=20,alpha=0.5,label='Offense-'+offense.Team.iloc[0]+'-'+offense.TeamBelongAbbr.iloc[0])
    plt.scatter(list(defense.X),list(defense.Y),marker='o',s=18,alpha=0.5,label='Defense-'+defense.Team.iloc[0]+'-'+defense.TeamBelongAbbr.iloc[0])
    plt.scatter(list(rusher.X),list(rusher.Y),marker='<' if offense.PlayDirection.iloc[0]=='left' else '>',c='black',s=50,label='Rusher')
    plt.plot([yard_line,yard_line],[-100,100],c='orange')
    
    plt.plot([10,10],[-100,100],c='green',linewidth=3) # down zone left
    plt.plot([110,110],[-100,100],c='green',linewidth=3) # down zone right
    plt.title('Quarter:'+str(offense.Quarter.iloc[0])+' - '+str(offense.GameClock.iloc[0])+' - '+offense.PlayDirection.iloc[0]+' - push:'+str(offense.Yards.iloc[0])+',dis:'+str(offense.Dis.iloc[0])+',need:'+str(offense.Distance.iloc[0]))
    plt.legend()
    
    i+=1

plt.show()



怎样一个瞬间的数据：xy代表的是开球的时候球员的站位，码线也是开球点的码线，那么yards对应的就是这样一个开球的情况下，最终推进的码数，所以这个瞬间是开球的瞬间，码数是这次进攻的结果；
```
