# libc_address
## 0x00 前言
这个项目主要用于测试对于程序开启PIE的程序，其libc的基地址是否随机的很均匀。本项目用python编写，web框架用的是flask，模板文件来源于CTFd框架的s模板文件，本来想有一个画图，但是，没有找到合适的控件。欢迎大佬补充，下面写一下画图需求。
### 0x00 画图需求
#### 0x00 最高需求
横坐标范围为0x7f0000000000~0x7fffffffffff,纵坐标为出现的次数。
#### 0x01 中等需求
画出top10出现次数的折线图，横坐标为时间，纵坐标，为出现的次数
#### 0x01 最低需求
横坐标为top的address，纵坐标为出现的次数
## 0x01 项目主要逻辑
利用 **pwntools** 的 **process()** 函数，不断的开启进程，用 **io.libc.address** 得到基地址，然后根据取得的地址，存到对应的json文件里面,考虑到json文件的可读性，地址均用16进制表示。本项目用的是单线程，主要考虑到多线程的话，不容易比较得出top10，还有文件锁的一些问题，也欢迎大佬，**加入多线程来增速**。
## 0x02 环境搭建
+ 安装python，pip
+ pip安装pwntools，flask
## 0x03 用法
需要用到screen命令
~~~ shell
screen
python ./get_libc.py
## ctrl+a+d
screen
python ./count.py
## ctrl+a+d
~~~
### 0x01 注意
可以通过控制app.run()里面的参数host，port参数来控制访问的地址和端口 0.0.0.0 为任意地址访问

## 例子
[www.douluodalu.wang/libc_address](http://47.94.212.159/libc_address)
## 未解决的问题
**import flask** 和 ** import pwn** 不能同时import，不然app.run()会出问题
