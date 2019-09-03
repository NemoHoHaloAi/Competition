# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# https://blog.csdn.net/spartanfuk/article/details/82052503
# https://www.cnblogs.com/shengyang17/p/9649819.html

df = pd.DataFrame({
    '天气':['晴','晴','阴','雨','雨','雨','阴','晴','晴','雨','晴','阴','阴','雨'],
    '温度':['高','高','高','低','低','低','低','低','低','低','低','低','高','低'],
    '湿度':['高','低','高','高','高','低','低','高','低','高','低','高','低','高'],
    '起风':[False,True,False,False,False,True,True,False,False,False,True,True,False,True],
    '打球':['NO','NO','YES','YES','YES','NO','YES','NO','NO','YES','YES','YES','YES','YES']})

print '原始数据：'
print df[['天气','温度','湿度','起风','打球']]
print ''

df_tmp = df.copy(deep=True)
df_tmp['天气'] = le.fit_transform(df_tmp['天气'])
df_tmp['温度'] = le.fit_transform(df_tmp['温度'])
df_tmp['湿度'] = le.fit_transform(df_tmp['湿度'])
df_tmp['起风'] = le.fit_transform(df_tmp['起风'])
df_tmp['打球'] = le.fit_transform(df_tmp['打球'])

###################################

def entropy(D):
    count_array=np.array(Counter(D).values())
    P=count_array/float(count_array.sum())
    H=np.dot(-P,np.log2(P))
    return H

def condition_entropy(D,A):
    A=np.array(A)
    D=np.array(D)
    H_da=0
    for i in np.unique(A):
        index_i=np.ravel(np.argwhere(A==i))
        Di=D[index_i]
        H_Di=entropy(Di)
        pi=float(Di.size)/D.size
        H_da=H_da+pi*H_Di
    return H_da

def gain(y, x):
    return entropy(y) - condition_entropy(y, x)

def gain_ratio(y, x):
    '''
    说明：计算y和x的信息增益比，注意这里是除以x的信息增益，也就是对x的取值的离散度计算一个惩罚值，最明显的就是ID字段
    '''
    return gain(y,x) / entropy(x)

###################################
x1=[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2]
x2=[0,0,1,1,0,0,0,1,0,0,0,0,1,1,0]
x3=[0,0,0,1,0,0,0,1,1,1,1,1,0,0,0]
x4=[0,1,1,0,0,0,1,1,2,2,2,1,1,2,0]
y =[0,0,1,1,0,0,0,1,1,1,1,1,1,1,0]

X=np.c_[x1,x2,x3,x4]
Hy=entropy(y)
Hyx1=condition_entropy(y,x1)
Hyx2=condition_entropy(y,x2)
Hyx3=condition_entropy(y,x3)
Hyx4=condition_entropy(y,x4)

g_yx1=Hy-Hyx1
g_yx2=Hy-Hyx2
g_yx3=Hy-Hyx3
g_yx4=Hy-Hyx4

print y
print 'Entropy y:',Hy
print ''

print y
print x1
print 'ConditionEntropy y&x1:',Hyx1
print ''

print y
print x2
print 'ConditionEntropy y&x2:',Hyx2
print ''

print y
print x3
print 'ConditionEntropy y&x3:',Hyx3
print ''

print y
print x4
print 'ConditionEntropy y&x4:',Hyx4
print ''

print 'Gain y&x1:',gain(y,x1)
print 'Gain y&x2:',gain(y,x2)
print 'Gain y&x3:',gain(y,x3)
print 'Gain y&x4:',gain(y,x4)
print ''

# Gain ratio : gr_Xy=g_Xy/HX
print 'GainRatio y&x1:', g_yx1/entropy(y)
print 'GainRatio y&x1:', gain_ratio(y,x1)
print 'GainRatio y&x2:', g_yx2/entropy(y)
print 'GainRatio y&x2:', gain_ratio(y,x2)
print 'GainRatio y&x2:', g_yx3/entropy(y)
print 'GainRatio y&x2:', gain_ratio(y,x3)
print 'GainRatio y&x3:', g_yx4/entropy(y)
print 'GainRatio y&x3:', gain_ratio(y,x4)
print ''

print 'GainRatio:', gain_ratio(df_tmp['打球'], df_tmp['温度'])
print 'GainRatio:', gain_ratio(df_tmp['打球'], df_tmp['湿度'])
print 'GainRatio:', gain_ratio(df_tmp['打球'], df_tmp['天气'])
print 'GainRatio:', gain_ratio(df_tmp['打球'], df_tmp['起风'])

hp = pd.read_csv('../kaggle/House-Prices/input/train.csv')
print hp.sample(10)

for col in hp.columns:
    if hp[col].dtype == 'object':
        hp[col] = le.fit_transform(hp[col])

print 'Pearson:'
print hp.corrwith(hp['MSZoning'])#,method='pearson')
print ''

print 'Gain&Ratio:'
dict_ = {}
for col in hp.columns:
    print 'MSZoing&'+col+':',gain(hp['MSZoning'],hp[col]),gain_ratio(hp['MSZoning'],hp[col])
    dict_['MSZoing&'+col] = (gain(hp['MSZoning'],hp[col]),gain_ratio(hp['MSZoning'],hp[col]))
print ''

res = sorted(dict_.items(),key=lambda v:v[1][1],reverse=True)[:5]
for r in res:
    print r
