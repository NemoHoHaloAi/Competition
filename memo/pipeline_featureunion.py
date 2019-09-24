# -*- coding: utf-8 -*-

from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
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

