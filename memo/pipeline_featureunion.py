# -*- coding: utf-8 -*-

from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.datasets import samples_generator
 
x, y = samples_generator.make_classification(n_informative=5, n_redundant=0, random_state=42)
print x.shape
print y.shape
anova_filter = SelectKBest(f_regression, k=5)
svm = SVC(kernel='linear')
# Pipeline简单示例
pipe = Pipeline([
                ('anova', anova_filter), 
                ('clf', svm)
                ])
pipe.set_params(anova__k=10, clf__C=0.1).fit(x, y) 
score = pipe.score(x, y)
print 'Pipeline score:'+str(score)

# make_pipeline简单示例
print 'make_pipeline score:'+str(make_pipeline(SelectKBest(f_regression, k=10), SVC(kernel='linear', C=.1)).fit(x, y).score(x, y))

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

# feature union
# 并行处理特征组合，比如通过pca和kernelPCA生成两列数据
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA
estimators = [('linear_pca', PCA())]#, ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
print x.shape
print x
x_ = combined.fit(x, y).transform(x)
print x_.shape
print x_
