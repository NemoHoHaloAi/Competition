#-*- coding: utf-8 -*-

import os,sys
import pandas as pd

sys.path.append('../')
from toolbox.memory_tool import MemoryTool

data = pd.read_csv('../../mlb_game_logs.csv')
print data.info(memory_usage='deep')

print '总占用：738M'
print ''

print '类型数量：'
print '77个float64, 6个int64，78个object'
print ''

print '类型平均占用情况：'
MemoryTool.memory_info_part(data)
print ''
print '可以看到总量、平均都是object类型占用最多，这主要是因为pandas对object的存储导致碎片化严重'

print '下面依次优化：'

print '各类型范围：'
MemoryTool.show_alltype_round()
print ''

print 'Int with unsigned：'
MemoryTool.memory_usage_int(data)
print ''

print 'Int with int：'
MemoryTool.memory_usage_int(data, downcast_type='integer')
print ''

print 'Float：'
MemoryTool.memory_usage_float(data)
print ''

print 'Object：'
MemoryTool.memory_usage_object(data.acquisition_info)
