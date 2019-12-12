# 使用.调用DataFrame的item列报错

这里直接type(Series.item)会看到是一个method类型，item应该是一个series的方法，所以要用Series.['item']代替；
