#!/bin/bash

# 启动多个jupyter多次多次切换的时候，忘记关闭某些浏览器打开的文件
# 保存文件的时候，保存到当前目录中来了，所以可以考虑指定端口号，单独使用，就没这问题了
# 指定端口号
jupyter notebook --port 9999
