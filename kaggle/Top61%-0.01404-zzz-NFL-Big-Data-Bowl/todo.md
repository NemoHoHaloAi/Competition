# todo

- 需要处理的特征：Location，PlayerCollegeName，Stadium，GameWeather，OffensePersonnel，DefensePersonnel，统一处理这一类问题，test中的类别不存在train中时如何处理
    - OffensePersonnel，DefensePersonnel进行拆分，拆为各个角色在场上的当前人数；
    - Location，PlayerCollegeName，Stadium，GameWeather：读取所有训练+测试中的可能，hardcode，用于fit LE；
- 提交结果
- 设计新的特征
