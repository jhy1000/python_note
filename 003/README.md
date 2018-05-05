# 第 3 章 表达式

## 3.1 句法规则

### 源文文件编码

```
# coding=utf-8
# -*- coding:utf-8 -*-
```

```python
#!/usr/bin/env python

def main():
    print("世界末日日!")


# 玛雅人人都是骗人人的!
if __name__ == "__main__":
    main()
```

```
root@jhy-linux:~/python_note/003# python2 001.py 
  File "001.py", line 4
SyntaxError: Non-ASCII character '\xe4' in file 001.py on line 4, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

root@jhy-linux:~/python_note/003# python3 001.py 
世界末日日!
```

### 强制缩进

```
#!/usr/bin/env python
# coding=utf-8
__builtins__.end = None

# 看这里里,看这里里......
def test(x):
    if x > 0:
        print("a")
    else:
        print("b")
    end
end

def main():
    print("世界末日日!") # 再次鄙视玛雅人人!(*_*)
end

if __name__ == "__main__":
    main()
```

### 注释
注释从 # 开始,到行尾结束,不支持跨行。大段的描述可以用 """__doc__"""。


### 语句
可以用 ";" 将多条语句写在同一行,或者用 "\" 将一条语句拆分成多行。
某些 ()、[]、{} 表达式无需 "\" 就可写成多行。


## 3.2 命名规则

- 必须以字母或下划线开头,且只能是下划线、字母和数字的组合。
- 不能和语言保留字相同。
- 名字区分大小写。
- 模块中以下划线开头的名字视为私有。
- 以双下划线开头的类成员名字视为私有。
- 同时以双下划线开头和结尾的名字,通常是特殊成员。
- 单一下划线代表最后表达式的返回值。

```
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> len(keyword.kwlist)
33
>>>
```

## 3.3 赋值
除非在函数中使用关键字 global、nolocal 指明外部名字,否则赋值语句总是在当前名字空间创建
或修改 {name:object} 关联。
与 C 以 block 为隔离,能在函数中创建多个同名变量不同,Python 函数所有代码共享同一名字空间,会出现下面面这样的状况。
```
>>> def test():
...     while True:
...         x = 10
...         break
...     print(locals())
...     print(x)       # 这个写法在 C 里里面面会报错。
... 
>>> test()
{'x': 10}
10
```
 
```
>>> a, b = 'abc'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> a,b,_ = 'abc'
>>> a,b='abc'[:2]
>>> 
>>> 
>>> a,*b, c = 'a1234c'
>>> a,b,c
('a', ['1', '2', '3', '4'], 'c')
>>> 
```

## 3.4 表达式
```
>>> x = 10
>>> if x > 0:
...     print('+')
... elif x < 0:
...     print('-')
... else:
...     print('0')
... 
+
>>> 
```

```
>>> x = 1
>>> print("+" if x > 0 else ('-' if x < 0 else '0'))
+
>>> x = 0
>>> print("+" if x > 0 else ('-' if x < 0 else '0'))
0
>>> x = -1
>>> print("+" if x > 0 else ('-' if x < 0 else '0'))
-
>>>
```

```
>>> x = 1
>>> print((x > 0 and "+") or (x < 0 and "-") or "0")
+
>>> x = 0
>>> print((x > 0 and "+") or (x < 0 and "-") or "0")
0
>>> x = -1
>>> print((x > 0 and "+") or (x < 0 and "-") or "0")
-
>>> 
```

```
>>> x = 10
>>> if (5 < x <= 10): print("haha!")
... 
haha!
>>> 
```

条件表达式不能包含赋值语句,
```
>>> if (x=1) > 0:pass
  File "<stdin>", line 1
    if (x=1) > 0:pass
         ^
SyntaxError: invalid syntax
>>>
```

### while
比我们熟悉的 while 多了个可选的 else 分支支。如果循环没有被中断,那么 else 就会执行。
```
>>> x = 3
>>> while x > 0:
...     x -= 1
... else:
...     print("over")
... 
over
>>> x 
0
>>> while True:
...     x += 1
...     if x > 3: break
... else:
...     print("over")
... 
>>> x
4
>>>
```

### for
更名为 foreach 可能更合适一一些,用用来循环处理序列和迭代器对象。
```
>>> for i in range(3): print(i)
... 
0
1
2
>>> for k,v in {"a":1,"b":2}.items(): print(k,v)
... 
a 1
b 2
>>> d = ((1,["a","b"]),(2,["x","y"]))
>>> for i ,(c1,c2) in d:
...     print(i,c1,c2)
... 
1 a b
2 x y
>>>
```

```
>>> for x in range(3):
...     print(x)
... else:
...     print("over")
... 
0
1
2
over
>>> for x in range(3):
...     print(x)
...     if x > 1: break
... else:
...     print("over")
... 
0
1
2
>>>
```
要实现传统的 for 循环,需要借助 enumerate() 返回序号。
```
>>> for i, c in enumerate("abc"):
...     print("s[{0}] = {1}".format(i,c))
... 
s[0] = a
s[1] = b
s[2] = c
>>> 
```

### pass
占位符,用来标记空代码块。
```
>>> def test():
...     pass
... 
>>> class User(object):
...     pass
... 
>>> 
```

### break / continue
break 中断循环,continue 开始下一次循环。
没有 goto、label,也无法用 break、continue 跳出多层嵌套循环。
```
>>> while True:
...     while True:
...         flag = True
...         break
...     if "flag" in locals(): break
... 
>>>
```

如果嫌 "跳出标记" 不好看,可以考虑抛出异常。
```
>>> class BreakException(Exception): pass
... 
>>> try:
...     while True:
...         while True:
...             raise BreakException()
... except BreakException:
...     print("越狱成功!")
... 
越狱成功!
>>> 
```

### del
可删除名字、序列元素、字典键值,以及对象成员。
```
>>> x = 1
>>> "x" in globals()
True
>>> del x
>>> "x" in globals()
False
>>> 
>>> x = list(range(10))
>>> del x[1]
>>> x
[0, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> x = list(range(10))
>>> del x[1:5]
>>> x
[0, 5, 6, 7, 8, 9]
>>> 
>>> d = {"a":1,"b":2}
>>> del d["a"]        # key 不存在时,会抛出异常。
>>> d
{'b': 2}
>>> 
>>> class User(object): pass
... 
>>> o = User()
>>> o.name = "user1"
>>> hasattr(o,"name")
True
>>> del o.name
>>> hasattr(o,"name")
False
>>> 
```

### Generator
用一种优雅的方式创建列表、字典或集合。
```
>>> [x for x in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> {x for x in range(10)}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> 
>>> {c:ord(c) for c in "abc"}
{'a': 97, 'b': 98, 'c': 99}
>>> 
>>> (x for x in range(10))
<generator object <genexpr> at 0x7f7b2d31f938>
>>> 
>>> [x for x in range(10) if x % 2]
[1, 3, 5, 7, 9]
>>> 
>>> 
>>> ["{0}{1}".format(c,x) for c in "abc" for x in range(3)]
['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']
>>>
>>> n = []
>>> for c in "abc":
...     for x in range(3):
...         n.append("{0}{1}".format(c,x))
... 
>>> n
['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']
>>> 
>>> ["{0}{1}".format(c,x)       \
...     for c in "aBcD" if c.isupper() \
...     for x in range(5) if x % 2     \
... ]
['B1', 'B3', 'D1', 'D3']
>>> 
>>> def test(it):
...     for i, x in enumerate(it):
...         print("{0} = {1}".format(i,x))
... 
>>> test(hex(x) for x in range(3))
0 = 0x0
1 = 0x1
2 = 0x2
>>> 
```

## 3.5 运算符
这东西没啥好说的,只要记得没 "++"、"--" 就行。

### 切片
序类型支持 "切片 (slice)" 操作,可通过两个索引序号获取片段。
```
>>> 
>>> x = list(range(10))
>>> x[2:6]
[2, 3, 4, 5]
>>> 
>>> x[2:-2]
[2, 3, 4, 5, 6, 7]
>>> 
>>> x[2:6:2]
[2, 4]
>>> 
>>> x[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> x[:6]
[0, 1, 2, 3, 4, 5]
>>> 
>>> x[7:]
[7, 8, 9]
>>> 
>>> x[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> x[7:3:-2]
[7, 5]
>>> 
```

```
>>> x = list(range(10))
>>> del x[4:8]; x
[0, 1, 2, 3, 8, 9]
>>> 
>>> x = list(range(10))
>>> del x[::2]; x
[1, 3, 5, 7, 9]
>>> 
>>> a = [1,2,3]
>>> a[:1] = ['a','b','c']
>>> a
['a', 'b', 'c', 2, 3]
>>> 
```

### 布尔
and 返回短路时的最后一个值,or 返回第一个真值。要是没短路的话,返回最后一个值。
```
>>> 1 and 2
2
>>> 1 and 2 and 0
0
>>> 1 and 0 and 2
0
>>> 
>>> 1 or 0
1
>>> 0 or [] or 1
1
>>> 0 or 1 or ["a"]
1
>>> 
```
用 and、or 实现 "三元表达式 (?:)"。
```
>>> x = 5
>>> print(x > 0 and "A" or "B")
A
>>>
```

用 or 提供默认值。
```
>>> x = 5
>>> y =x or 0
>>> y
5
>>> 
>>> x = None
>>> y = x or 0
>>> y
0
>>> 
```

### 相等
操作符 "==" 可被重载,不适合用来判断两个名字是否指向同一对象。
```
>>> import operator
>>> 
>>> class User(object):
...     def __init__(self,name):
...         self.name = name
...     def __eq__(self,o):
...         if not o or not isinstance(o,User): return False
...         return operator.eq(self.name, o.name)
... 
>>> a, b = User("tom"), User("tom")
>>> 
>>> a is b     # is 总是判断指针是否相同。
False
>>> 
>>> a == b     # 通过 __eq__ 进行行判断。
True
>>> 
```
## 3.6 类型转换
各种类型和字符串间的转换。
```
>>> str(123), int('123')                        # int
('123', 123)
>>> 
>>> bin(17), int('0b10001',2)
('0b10001', 17)
>>> 
>>> oct(20), int('024',8)
('0o24', 20)
>>> 
>>> hex(22), int('0x16', 16)
('0x16', 22)
>>> 
>>> str(0.9), float("0.9")                      # float
('0.9', 0.9)
>>> 
>>> ord('a'), chr(97)                           # char
(97, 'a')
>>> 
>>> str([0,1,2]), eval("[0,1,2]")               # list
('[0, 1, 2]', [0, 1, 2])
>>> 
>>> str((0,1,2)), eval("(0,1,2)")               # tuple
('(0, 1, 2)', (0, 1, 2))
>>> 
>>> str({"a":1,"b":2}), eval("{'a':1, 'b':2}")  # dict
("{'a': 1, 'b': 2}", {'a': 1, 'b': 2})
>>> 
>>> str({1,2,3}), eval("{1,2,3}")               # set
('{1, 2, 3}', {1, 2, 3})
>>>
```

## 3.7 常用用函数
### print
Python 2.7 可使用用 print 表达式,Python 3 就只能用用函数了。
```
root@jhy-linux:~/python_note/003# python2
Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> 
>>> print >> sys.stderr, "Error!", 456
Error! 456
>>> 
>>> from __future__ import print_function
>>> 
>>> print("Hello","World",sep=",", end="\r\n", file=sys.stdout)
Hello,World
>>> 
>>> import os
>>> print("Hello","World",sep=",", end="\r\n", file=open(os.devnull,"w"))
>>> 
```
用标准库中的 pprint.pprint() 代替 print,能看到更漂亮的输出结果。要输出到 /dev/null,可以使用 open(os.devnull, "w")。


### input
input 直接返回用用户输入的原始字符串。
```
root@jhy-linux:~/python_note/003# python
Python 3.6.3 |Anaconda custom (64-bit)| (default, Oct 13 2017, 12:02:49) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> input("$ ")
$ 1 + 2 + 3
'1 + 2 + 3'
>>> 
>>> eval(input("$ "))
$ 1 + 2 + 3
6
>>> 
```
用标准库 getpass 输入入密码。
```
>>> from getpass import getpass, getuser
>>> 
>>> pwd = getpass("%s password: " % getuser())
root password: 
>>> 
>>> pwd
'shanghai'
>>> 
```

### exit
exit([status]) 调用所有退出函数后终止进程,并返回 ExitCode。
- 忽略或 status = None,表示正常退出, ExitCode = 0。
- status = <number>,表示 ExiCode = <number>。
- 返回非数字对象表示失败,参数会被显示, ExitCode = 1。
```python
#!/usr/bin/env python
#coding=utf-8

import atexit

def clean():
    print('clean...')

def main():
    atexit.register(clean)
    exit("Failure")

if __name__ == '__main__':
    main()

# output
#Failure
#clean...
```
sys.exit() 和 exit() 完全相同。os._exit() 直接终止进程,不调用退出函数,且退出码必须是数字。

### vars
获取 locals 或指定对象的名字空间。
```
>>> vars() is locals()
True
>>> 
>>> import sys
>>> 
>>> vars(sys) is sys.__dict__
True
>>>
```

### dir
获取 locals 名字空间中的所有名字,或指定对象所有可访问成员 (包括基类)。
```
>>> set(locals().keys()) == set(dir())
True
>>> 
```
