# 从Gert的Kernel开始

- Link: https://www.kaggle.com/gertjac/regression-approach
- Public Score: `0.01408`

## 问题分析

数据中给出的Target是码数，但是要求的提交文件是概率分布，因此这里需要一种转换方式来完成从pred到submission的过程；

## 解决方案

### 如何转换

1. 将模型的预测分成10部分，然后根据预测直接估计码的条件分布；
2. 注意数据要留出一部分用于验证，避免过拟合；
3. 码数经过了log1p处理，分布更加正态；
4. 条件分布被kde平滑处理；

### 如何提交

通过竞赛提供的nflrush提交结果；
