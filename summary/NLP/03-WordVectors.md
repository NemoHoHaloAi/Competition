# [文本向量](https://www.kaggle.com/matleonard/word-vectors)

词袋模型统计的是单词的出现次数，而不考虑上下文，而Word2Vec考虑的是每个单词所处的上下文环境，例如，对于lion和tiger，通常来说出现在各个文集中的上下文环境是类似的，因此二者的向量也应该是类似的，而这就是文本向量的思想，通过所处上下文环境的次数组成向量来表示每个单词。

## .vector

spaCy通过`vector`属性获取每个token对应的文本向量。

## 分类模型

通过spaCy的`vector`属性可以很方便的构建出numpy格式的矩阵，作为模型的输入。

## 相似度计算

既然可以得到文档对应的向量表现，就可以通过计算`cos`来衡量两个向量的相似度，即文档的相似度，这在新闻分类中非常常见。

## [练习](https://www.kaggle.com/holoong9291/exercise-word-vectors)
