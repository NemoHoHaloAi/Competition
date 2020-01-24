# EDA

从这里也开始总结整理以下关于EDA的流程，最重要的是需要产出什么，来有效的服务于后续的特征工程、建模等部分；

![](https://www.kaggleusercontent.com/kf/14193052/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..-JztzEtAABmyrkm56lGsWg.cIKIED8Ln1JaLHHEWknw0JM4vGOytkPMsQMQDCRaA2PDHkRWqOJA6QKtxml72pXKwsz688RchbdQom-WjsdqycEGVS7UAHl9n2e-foL726CM4QnRwpVfJSQauuin4ltnWkubAbG0vYxYPOjZvwgFJOlDib4I598gvuE62X8O1e0.0I0BKd_aJNPzWLZfKKtVwg/__results___files/figure-html/unnamed-chunk-27-1.png)

EDA原因：因为air_visit信息是主要的训练数据，进行有效的可视化有助于理解数据，因此可视化其数据趋势可以看出是否存在周期性，可视化其分布可以看起是否满足正态，是否是否存在极值问题，而dayofweek、monthofyear则是时序数据中对于周期性判断的一般方法；

EDA输出：
1. 总visitors走向看，有一个很奇怪的阶段性整体上升发生在2016-07，初步怀疑是**系统中增加了对其他店铺的统计**；
2. 总visitors有一个明显的周期性，目测为一周；
3. 分布上看大部分店铺一天接待顾客为20人，少数会到达甚至超过100人；
4. 星期五、星期六、星期天顾客最多，星期一、星期二最少，符合客观事实；
5. 相对来说12月份最忙，345月份较忙，应该跟气候有关，比如冷天大家都不想做饭；

![](https://www.kaggleusercontent.com/kf/14193052/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..-JztzEtAABmyrkm56lGsWg.cIKIED8Ln1JaLHHEWknw0JM4vGOytkPMsQMQDCRaA2PDHkRWqOJA6QKtxml72pXKwsz688RchbdQom-WjsdqycEGVS7UAHl9n2e-foL726CM4QnRwpVfJSQauuin4ltnWkubAbG0vYxYPOjZvwgFJOlDib4I598gvuE62X8O1e0.0I0BKd_aJNPzWLZfKKtVwg/__results___files/figure-html/unnamed-chunk-28-1.png)

EDA原因：我们要预测的是2017年4月最后一周加5月，因此对2016年这段时间做可视化非常有意义，时序数据通常都存在周期相似性，尤其是对于黄金周等特殊时间段的理解格外有用；

EDA输出：
1. 这部分是2016年的4月最后一周加上5月；
2. 从更光滑的蓝色线看出，按照一周的周期确实存在；
3. 在4月29号到5月5号，这种周期性有些变化，这里对应着前面概述中的日本黄金周(连续一周时间内连续休息)，所以这里的周期性看起来被打乱；

