# PredictFlow

PredictFlow是一个预测口碑商家流量的工具，通过已知的口碑商家流量预测各个口碑商家未来一个月的流量。主要是运用TF-IDF算法对特征信息进行提取，再通过朴素贝叶斯算法对未来一个月的流量进行预测。

# 入门

PredictFlow包括analyze、bean、dataBase、file和main。

file主要是文件操作，对给定的已知数据进行读取，建立训练集。

bean和dataBase主要是对数据库进行操作。

analyze主要是通过算法对数据进行预测。

main主要是对整个程序进行控制。

# 文件结构

file主要是文件操作，对给定的已知数据进行读取，建立训练集。

bean和dataBase主要是对数据库进行操作。

analyze主要是通过算法对数据进行预测。

manage.py主要是对整个程序进行控制。

prediction.csv是预测结果。

# 支持平台

PredictFlow基于Python3.5。如果想要运行PredictFlow推荐下载Python3.x解析器，并且需要pymysql，sklearn等包的支持。同时，需要注意处理文件和网页的格式。

# 疑问

如果您发现了诸如崩溃、意外行为或类似的问题，请访问[issue tracker](https://github.com/ranmengyuan/PredictFlow/issues)方便交流。

谢谢！
mengyuan

