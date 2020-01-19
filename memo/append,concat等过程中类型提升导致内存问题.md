目前看到有两种情况会导致该问题：
- append、concat过程中某个列在两个df中类型不同：
    ```python
    pd.concat(pd.Series(dtype='int64'),pd.Series(dtype='int8'))
    
    此时结果Series类型是int64；
    
    解决方案：concat前统一类型即可；
    ```
- category列concat后变为object
    ```python
    blood_type1 = pd.Categorical(["A", "AB"]) 
    blood_type2 = pd.Categorical(["B", "O"]) 
    pd.concat([pd.Series(blood_type1), pd.Series(blood_type2)])
    
    此时结果Series是object类型，这里即便两个Series都是A,B类型转的Categorial，结果也是一样的；
    
    解决方案：
    from pandas.api.types import union_categoricals
    pd.Series(union_categoricals([blood_type1, blood_type2]))
    
    此时的Series就是category的了，非常有用，谨记；
    ```
