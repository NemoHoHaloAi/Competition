# [NLP简介](https://www.kaggle.com/matleonard/intro-to-nlp)

文本文档数据对于懂得使用它的人来说，是最为重要的几种数据之一，而如何对于进行处理、基于它建模称为最为关键的知识，spaCy是目前最为流程的NLP框架之一。

## Tokenizing - 标记化

利用spaCy根据特定语言建模后，可以直接处理特定语言的文本文档数据，遍历其对象，可以得到每个Token，token作为text doc的最小单元，它可以是单一的单词或者标点符号，注意的是spaCy将don't分割为两个token，do和n't，有利于后续处理。
