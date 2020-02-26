# [NLP简介](https://www.kaggle.com/matleonard/intro-to-nlp)

文本文档数据对于懂得使用它的人来说，是最为重要的几种数据之一，而如何对于进行处理、基于它建模称为最为关键的知识，spaCy是目前最为流程的NLP框架之一。

## Tokenizing - 标记化

利用spaCy根据特定语言建模后，可以直接处理特定语言的文本文档数据，遍历其对象，可以得到每个Token，token作为text doc的最小单元，它可以是单一的单词或者标点符号，注意的是spaCy将don't分割为两个token，do和n't，有利于后续处理。

## Preprocessing - 预处理

在遍历后的token对象中，最重要的两个属性分别是`lemma_`和`is_stop`：
- `lemma_`：返回该token对应的基本模式，例如working，返回work，英文中每个词都有几种不同的形式，而lemma_则是返回最基本的那种。
- `is_stop`：返回该词是否为停用词，英文中停用词有`is`,`and`,`that`等，这些词通常不携带太多信息，去除有利于使模型专注于真正重要的部分。

当然，这二者在preprocess阶段的使用最好是作为参数可配，因为其也有可能导致模型变差，需要根据具体问题灵活运用。

## Pattern Match - 模式匹配

即在整个文档或者文本块中匹配tokens或者短语，搜索方式可以通过普通字符串匹配、正则表达式等，但是使用spaCy的`Matcher`和`PhraseMatcher`更加简单强大。

匹配过程：
1. 创建`Matcher`或者`PhraseMatcher`对象。
2. 向其中add需要识别的短语模式。
3. 对文本进行识别。
4. 返回结果为三部分：vocad id，匹配位置的开始和结束。

## [练习](https://www.kaggle.com/holoong9291/exercise-intro-to-nlp)
