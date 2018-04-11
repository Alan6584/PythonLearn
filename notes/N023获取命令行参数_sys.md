###通过 sys 获取命令行参数

####一、sys 模块

在 Python 中，通过 sys 模块中的 sys.argv 可以访问到所有的命令行参数，它的返回值是包含所有命令行参数的列表。

- sys.argv ：是命令行参数列表
- len(sys.argv) ：是命令行参数个数
- sys.argv[0]：参数1
- sys.argv[1]：参数2

**实例**

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@Time    : 2018-04-11 17：58
@Author  : jianjun.wang
@Email   : alanwang6584@gmail.com
"""

import sys

def main():
	print 'arg num : ', len(sys.argv)
	print 'args : ', sys.argv
	print 'script name : ', sys.argv[0]

	for i in range(len(sys.argv)):
		print "arg[{0}] = {1}".format(i, sys.argv[i])

if __name__ == "__main__":
    main()
```

命令行中输入：python D023_get_arg_sys.py alan 3

**输出**

```
arg num :  3
args :  ['D023_get_arg_sys.py', 'alan', '3']
script name :  D023_get_arg_sys.py
arg[0] = D023_get_arg_sys.py
arg[1] = alan
arg[2] = 3
```

