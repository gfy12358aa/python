本版本实现了一个基本单线程的爬去网页的爬虫。
并简单分析网页


问题1 忘记设定爬虫最大读取个数  2018 1 14

1.001 新增退出时保存未读取、已读取的网址分别存放在save.txt,history.txt文件中。
添加一个stream静态类
读取文件
1.002 
从文本改成读取数据库
数据库文件
book
name ReadNumber Reader留存率 简介 网址

sql类
数据库连接字
构造函数
方法

2.0
自动获取小说的信息存入sql server中

获取小说
网址 题目 类型() 读者留存率 追书人数 简介



System.Data.SqlClient.SqlException (0x80131904): 在与 SQL Server 建立连接时出现与网络相关的或特定于实例的错误。未找到或无法访问服务器。请验证实例名称是否正确并且 SQL Server 已配置为允许远程连接。 (provider: SQL Network Interfaces, error: 26 - 定位指定的服务器/实例时出错)
 