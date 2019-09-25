# -*- coding: utf-8 -*-

from sklearn.pipeline import FeatureUnion, _fit_one_transformer, _fit_transform_one, _transform_one 
from sklearn.externals.joblib import Parallel, delayed
from scipy import sparse
import numpy as np

#部分并行处理，继承FeatureUnion
class FeatureUnionExt(FeatureUnion):
    #相比FeatureUnion，多了idx_list参数，其表示每个并行工作需要读取的特征矩阵的列
    def __init__(self, transformer_list, idx_list, n_jobs=1, transformer_weights=None):
        self.idx_list = idx_list
        FeatureUnion.__init__(self, transformer_list=map(lambda trans:(trans[0], trans[1]), transformer_list), n_jobs=n_jobs, transformer_weights=transformer_weights)

    #由于只部分读取特征矩阵，方法fit需要重构
    def fit(self, X, y=None):
        transformer_idx_list = map(lambda trans, idx:(trans[0], trans[1], idx), self.transformer_list, self.idx_list)
        transformers = Parallel(n_jobs=self.n_jobs)(
            #从特征矩阵中提取部分输入fit方法
            delayed(_fit_one_transformer)(trans, X[:,idx], y)
            for name, trans, idx in transformer_idx_list)
        self._update_transformer_list(transformers)
        return self

    #由于只部分读取特征矩阵，方法fit_transform需要重构
    def fit_transform(self, X, y=None, **fit_params):
        transformer_idx_list = map(lambda trans, idx:(trans[0], trans[1], idx), self.transformer_list, self.idx_list)
        result = Parallel(n_jobs=self.n_jobs)(
            #从特征矩阵中提取部分输入fit_transform方法
            delayed(_fit_transform_one)(trans, name, X[:,idx], y,
                                        self.transformer_weights, **fit_params)
            for name, trans, idx in transformer_idx_list)

        Xs, transformers = zip(*result)
        self._update_transformer_list(transformers)
        if any(sparse.issparse(f) for f in Xs):
            Xs = sparse.hstack(Xs).tocsr()
        else:
            Xs = np.hstack(Xs)
        return Xs

    #由于只部分读取特征矩阵，方法transform需要重构
    def transform(self, X):
        transformer_idx_list = map(lambda trans, idx:(trans[0], trans[1], idx), self.transformer_list, self.idx_list)
        Xs = Parallel(n_jobs=self.n_jobs)(
            #从特征矩阵中提取部分输入transform方法
            delayed(_transform_one)(trans, name, X[:,idx], self.transformer_weights)
            for name, trans, idx in transformer_idx_list)
        if any(sparse.issparse(f) for f in Xs):
            Xs = sparse.hstack(Xs).tocsr()
        else:
            Xs = np.hstack(Xs)
        return Xs

if __name__ == '__main__':
    pass
