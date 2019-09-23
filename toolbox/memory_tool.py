#-*- coding: utf-8 -*-
# https://blog.csdn.net/zhusongziye/article/details/92064823
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html

import pandas as pd
import numpy as np

class MemoryTool(object):

    @staticmethod
    def memory_info_part(df):
        for dtype in ['float','int','object']:
            selected_dtype = df.select_dtypes(include=[dtype])
            usage_b = selected_dtype.memory_usage(deep=True).sum()
            usage_mb = usage_b / 1024 ** 2
            mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
            mean_usage_mb = mean_usage_b / 1024 ** 2

            print("Total memory usage for {} columns: {:03.2f} MB".format(dtype,usage_mb))
            print("Average memory usage for {} columns: {:03.2f} MB".format(dtype,mean_usage_mb))

    @staticmethod
    def show_alltype_round():
        int_types = ["int8", "uint8", "int16", "uint16", "int32", "uint32", "int64", "uint64"]
        float_types = ["float16", "float32", "float64"]
        for type_ in int_types:
            print(np.iinfo(type_))
        for type_ in float_types:
            print(np.finfo(type_))

    @staticmethod
    def mem_usage(pandas_obj):
        if isinstance(pandas_obj,pd.DataFrame):
            usage_b = pandas_obj.memory_usage(deep=True).sum()
        else: # we assume if not a df it's a series
            usage_b = pandas_obj.memory_usage(deep=True)
        usage_mb = usage_b / 1024 ** 2 # convert bytes to megabytes
        return "{:03.2f} MB".format(usage_mb)

    @staticmethod
    def memory_usage_int(df, downcast_type='unsigned'):
        df_int = df.select_dtypes(include=['int'])
        converted_int = df_int.apply(pd.to_numeric,downcast=downcast_type)
        print(MemoryTool.mem_usage(df_int))
        print(MemoryTool.mem_usage(converted_int))

        compare_ints = pd.concat([df_int.dtypes,converted_int.dtypes],axis=1)
        compare_ints.columns = ['before','after']
        compare_ints.apply(pd.Series.value_counts)
        print compare_ints

    @staticmethod
    def memory_usage_float(df):
        df_float = df.select_dtypes(include=['float'])
        converted_float = df_float.apply(pd.to_numeric,downcast='float')
        print(MemoryTool.mem_usage(df_float))
        print(MemoryTool.mem_usage(converted_float))

        compare_ints = pd.concat([df_float.dtypes,converted_float.dtypes],axis=1)
        compare_ints.columns = ['before','after']
        compare_ints.apply(pd.Series.value_counts)
        print compare_ints

    @staticmethod
    def memory_usage_object(col):
        print col
        print(MemoryTool.mem_usage(col))
        print col.astype('category')
        print(MemoryTool.mem_usage(col.astype('category')))
