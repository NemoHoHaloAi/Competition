# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from feature_union_ext import FeatureUnionExt

from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn import datasets
from sklearn.datasets import samples_generator
from tempfile import mkdtemp
cachedir = mkdtemp()
 
x, y = samples_generator.make_classification(n_informative=5, n_redundant=0, random_state=42)
print x.shape
print y.shape
print '>'*50
anova_filter = SelectKBest(f_regression, k=5)
svm = SVC(kernel='linear')
# Pipeline简单示例
pipe = Pipeline([
                ('anova', anova_filter), 
                ('clf', svm)
                ], memory=cachedir)
pipe.set_params(anova__k=10, clf__C=0.1).fit(x, y) 
score = pipe.score(x, y)
print 'Pipeline score:'+str(score)
print '>'*50

# make_pipeline简单示例
print 'make_pipeline score:'+str(make_pipeline(SelectKBest(f_regression, k=10), SVC(kernel='linear', C=.1)).fit(x, y).score(x, y))
print '>'*50

# 结合GridSearch使用示例，注意此处是params既可以是针对pipe，也可以是针对pipe中的某个step的参数
# anova__k针对pipe的anova step设置的参数
# clf同上，针对clf参数
# clf__C则是针对clf step对应的共有的C参数
params = {
        'anova__k':range(5,16), 
        'clf':[SVC(), LogisticRegression()], 
        'clf__C':[i/0.1 for i in range(1,11)]
        }
grid_search = GridSearchCV(pipe, param_grid=params)
grid_search.fit(x, y)
print 'GridSearchCV score:{}'.format(grid_search.score(x, y))
print 'GridSearchCV Best parameters:{}'.format(grid_search.best_params_)
print 'GridSearchCV Best score on train set:{:.2f}'.format(grid_search.best_score_)
print '>'*50

# feature union
# 并行处理特征组合，比如通过pca(1)和TruncatedSVD(2)生成3列数据并合并，这里可以做一些新特征生成的逻辑，可以一起并行执行，比如多模型融合时生成输入特征
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA, TruncatedSVD
estimators = [('PCA', PCA(n_components=1)), ('TruncatedSVD', TruncatedSVD(n_components=2))]
combined = FeatureUnion(estimators)
print x.shape
print x[:3]
x_ = combined.fit(x, y).transform(x)
print x_.shape
print x_[:3]
print '>'*50

# feature union 做多模型输入生成，不支持，因为模型类没有transform方法
# combined = FeatureUnion([('SVC', SVC(kernel='linear')), ('LogisticRegression', LogisticRegression())])
# combined.fit(x, y)

############################################################################pipeline + featureunion -> iris#####################################################################################
iris = datasets.load_iris()
print iris.data[:10]
print iris.data.shape
iris.target = np.expand_dims(iris.target, axis=1)
print iris.target.shape
iris = pd.DataFrame(data=np.append(iris.data, iris.target, axis=1), columns=['花萼长度','花萼宽度','花瓣长度','花瓣宽度','品种'])
iris.info(memory_usage='deep')

# pre 类型下降
from sklearn.preprocessing import FunctionTransformer
print iris['品种'].memory_usage(deep=True)
print iris[['品种']].astype('int').apply(pd.to_numeric, downcast='unsigned').memory_usage(deep=True).sum()
iris[['品种']] = iris[['品种']].astype('int').apply(pd.to_numeric, downcast='unsigned')

print iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']].memory_usage(deep=True).sum()
print iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']].apply(pd.to_numeric, downcast='float').memory_usage(deep=True).sum()
iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']] = iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']].apply(pd.to_numeric, downcast='float')
iris.info(memory_usage='deep')
print iris.sample(5)

# step 1 长度分箱、onehot
#from sklearn.preprocessing import KBinsDiscretizer
#print KBinsDiscretizer(n_bins=[5, 3], encode='ordinal').fit_transform(iris[['花萼长度','花瓣长度']])
from sklearn.preprocessing import Binarizer
print Binarizer(threshold=iris['花萼长度'].mean()).fit_transform(iris[['花萼长度']])
print Binarizer(threshold=iris['花瓣长度'].mean()).fit_transform(iris[['花瓣长度']])

# step 1 指数变换、boxcox处理
# from sklearn.preprocessing import PowerTransformer
# print PowerTransformer(method='box-cox', standardize=False).fit_transform(iris[['花萼宽度','花瓣宽度']])
print FunctionTransformer(np.log1p).fit_transform(iris[['花萼宽度','花瓣宽度']])

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
print iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']]
print iris['品种']
iris = datasets.load_iris()
pipeline.fit(iris.data, iris.target)
pipeline.fit(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种'])
pipeline.score(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种'])

# GridSearch
grid_search = GridSearchCV(pipeline, param_grid={'FeatureUnionExt__ToBinary__threshold':[iris['花萼长度'].mean(),iris['花瓣长度'].mean()], 
                                                 'model':[SVC(kernel='linear'), LogisticRegression()], 
                                                 'model__C':[0.1,0.5,1]})
grid_search.fit(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种'])
print grid_search.score(iris[['花萼长度','花萼宽度','花瓣长度','花瓣宽度']], iris['品种'])

# step 4 模型融合
