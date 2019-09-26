# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from feature_union_ext import FeatureUnionExt
from sklearn import datasets
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()
iris.target = np.expand_dims(iris.target, axis=1)
iris = pd.DataFrame(data=np.append(iris.data, iris.target, axis=1), columns=['花萼长度','花萼宽度','花瓣长度','花瓣宽度','品种'])

# pre 类型下降
iris[['品种']] = iris[['品种']].astype('int').apply(pd.to_numeric, downcast='unsigned')

iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']] = iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']].apply(pd.to_numeric, downcast='float')
print 'Info deep:'
iris.info(memory_usage='deep')
print ''

print 'Sample 5:'
print iris.sample(5)
print ''

# step 1_1 长度分箱、onehot
#from sklearn.preprocessing import KBinsDiscretizer
#print KBinsDiscretizer(n_bins=[5, 3], encode='ordinal').fit_transform(iris[['花萼长度','花瓣长度']])
from sklearn.preprocessing import Binarizer
print 'Binarizer:'
print Binarizer(threshold=iris['花萼长度'].mean()).fit_transform(iris[['花萼长度']])[:5]
print ''
print Binarizer(threshold=iris['花瓣长度'].mean()).fit_transform(iris[['花瓣长度']])[:5]
print ''

# step 1_2 指数变换、boxcox处理
# from sklearn.preprocessing import PowerTransformer
# print PowerTransformer(method='box-cox', standardize=False).fit_transform(iris[['花萼宽度','花瓣宽度']])
from sklearn.preprocessing import FunctionTransformer
print 'Log1p:'
print FunctionTransformer(np.log1p).fit_transform(iris[['花萼宽度','花瓣宽度']])[:5]
print ''

step1_1 = ('ToBinary', Binarizer())
step1_2 = ('ToLog', FunctionTransformer(np.log1p))
step1 = ('FeatureUnionExt', FeatureUnionExt(transformer_list=[step1_1, step1_2], idx_list=[[0,2], [1,3]]))

# step 2 无量纲化
from sklearn.preprocessing import MinMaxScaler
step2 = ('MinMaxScaler', MinMaxScaler())

# step 3 多模型并行训练
step3 = ('model', SVC(kernel='linear'))

# Pipeline
pipeline = Pipeline(steps=[step1, step2, step3])
pipeline.set_params(FeatureUnionExt__ToBinary__threshold=0.2) 

pipeline.fit(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种'])
print 'PipeLine score:'
print pipeline.score(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种'])
print ''

# GridSearch
grid_search = GridSearchCV(pipeline, param_grid={'FeatureUnionExt__ToBinary__threshold':[iris['花萼长度'].mean(),iris['花瓣长度'].mean()], 
                                                 'model':[SVC(kernel='linear'), LogisticRegression()], 
                                                 'model__C':[0.1,0.5,1]})
grid_search.fit(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种'])
print 'GridSearchCV score:{}'.format(grid_search.score(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种']))
print 'GridSearchCV Best parameters:{}'.format(grid_search.best_params_)
print 'GridSearchCV Best score:{:.2f}'.format(grid_search.best_score_)
print ''

# step 4 模型融合
