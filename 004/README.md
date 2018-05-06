
# 第 4 章 函数

当编译器遇到 def,会生生成创建函数对象指令。也就是说 def 是执行行指令,而而不仅仅是个语法关键字。可以在任何地方方动态创建函数对象。

函数声明: 

```
def name([arg,... arg = value,... *arg, **kwarg]):
    suite
```

## 4.1 创建
包括函数在内的所有对象都是第一类对象,可作为其他函数的实参或返回值。
- 在名字空间中,名字是唯一主键。因此函数在同一范围内不能 "重载 (overload)"。
- 函数总是有返回值。就算没有 return,默认也会返回 None。
- 支持递归调用用,但不进行尾递归优化。最大大深度 sys.getrecursionlimit()。
```
>>> def test(name):
...     if name == 'a':
...         def a(): pass
...         return a
...     else:
...         def b(): pass
...         return b
... 
>>> test("a").__name__
'a'
>>> 
```
不同于用 def 定义复杂函数,lambda 只能是有返回值的简单的表达式。使用用赋值语句会引发语法错误,可以考虑用用函数代替。
```
>>> 
>>> add = lambda x,y = 0: x + y
>>> 
>>> add(1,2)
3
>>> add(3)
3
>>> list(map(lambda x:x, range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

## 4.2 参数
函数的传参方式灵活多变,可按位置顺序传参,也可不关心顺序用命名实参。
```
>>> def test(a,b):
...     print(a,b)
... 
>>> test(1,"a")             # 位置参数
1 a
>>> test(b = 'x', a = 100)  # 命名参数
100 x
>>> 
>>> 
```


支持参数默认值。不过要小小心心,默认值对象在创建函数时生成,所有调用用都使用同一对象。如果该默认值是可变类型,那么就如同 C 静态局部变量。
```
>>> def test(x, ints = []):
...     ints.append(x)
...     return ints
... 
>>> test(1)
[1]
>>> test(2)
[1, 2]
>>> test(1,[])
[1]
>>> test(3)
[1, 2, 3]
>>>
```
默认参数后面面不能有其他位置参数,除非是变参。
```
>>> def test(a, b = 0, c): pass
... 
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
>>> 
>>> 
>>> def test(a, b = 0, *args, **kwargs): pass
... 
>>> 
```
用 *args 收集 "多余" 的位置参数,**kwargs 收集 "额外" 的命名参数。这两个名字只是惯例,可自由命名。
```
>>> 
>>> def test(a,b,*args, **kwargs):
...     print(a,b)
...     print(args)
...     print(kwargs)
... 
>>> test(1,2,'a','b','c',x=100,y=200)
1 2
('a', 'b', 'c')
{'x': 100, 'y': 200}
>>>
```
变参只能放在所有参数定义的尾部,且 **kwargs 必须是最后一个。
```
>>> def test(*args, **kwargs):         # 可以接收任意参数的函数。
...     print(args)
...     print(kwargs)
... 
>>> test(1,'a',x='x', y='y')           # 位置参数,命名参数。
(1, 'a')
{'x': 'x', 'y': 'y'}
>>> 
>>> test(1)                            # 仅传位置参数。
(1,)
{}
>>> 
>>> test(x='x')                        # 仅传命名参数。
()
{'x': 'x'}
>>> 
>>> 
```
可 "展开" 序列类型和字典,将全部元素当做多个实参使用用。如不展开的话,那仅是单个实参对象。
```
>>> def test(a, b, *args, **kwargs):
...     print(a, b)
...     print(args)
...     print(kwargs)
... 
>>> test(*range(1,5), **{'x':'Hello', 'y':'World'})
1 2
(3, 4)
{'x': 'Hello', 'y': 'World'}
>>> 
```
单个 "*" 展开序列类型,或者仅是字典的主键列表。"**" 展开字典键值对。但如果没有变参收集,展开后多余的参数将引发异常。
```
>>> def test(a,b):
...     print(a)
...     print(b)
... 
>>> d = dict(a = 1, b = 2)
>>> 
>>> test(*d)                    # 仅展开 keys(),test("a"、"b")。
a
b
>>> test(**d)                   # 展开 items(),test(a = 1, b = 2)。
1
2
>>> d = dict(a = 1, b = 2, c = 3)
>>> test(*d)                    # 因为没有位置变参收集多余的 "c",导致出错。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: test() takes 2 positional arguments but 3 were given
>>> 
>>> test(**d)                   # 因为没有命名变参收集多余的 "c = 3",导致出错。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: test() got an unexpected keyword argument 'c'
>>> 
```

lambda 同样支持默认值和变参,使用用方方法完全一致。
```
>>> test = lambda a, b = 0, *args, **kwargs: sum([a, b] + list(args) + list(kwargs.values()))
>>> 
>>> test(1,*[2,3,4],**{'x':5,'y':6})
21
>>> 
```

## 4.3 作用用域

函数形参和内部变量都存储在 locals 名字空间中
```
>>> def test(a, *args, **kwargs):
...     s = 'Hello, World!'
...     print(locals())
... 
>>> test(1,'a','b',x=10,y='hi')
{'s': 'Hello, World!', 'kwargs': {'x': 10, 'y': 'hi'}, 'args': ('a', 'b'), 'a': 1}
>>>
```

除非使用 global、nonlocal 特别声明,否则在函数内部使用用赋值语句,总是在 locals 名字空间中新建一个对象关联。注意:"赋值" 是指名字指向新的对象,而非通过名字改变对象状态。
```
>>> x = 10
>>> hex(id(x))
'0x55841ecbbe00'
>>> 
>>> def test():
...     x = 'hi'
...     print(hex(id(x)))
... 
>>> test()          # 两个 x 指向不同的对象
0x7efdf59dfea0
>>> 
>>> x               # 外部变量没有被修改。
10
>>>
```
如果仅仅是引用外部变量,那么按 LEGB 顺序在不同作用用域查找该名字。
```
名字查找顺序: locals -> enclosing function -> globals -> __builtins__
```

- locals: 函数内部名字空间,包括局部变量和形参。
- enclosing function: 外部嵌套函数的名字空间。
- globals: 函数定义所在模块的名字空间。
- __builtins__: 内置模块的名字空间。

想想看,如果将对象引入入 __builtins__ 名字空间,那么就可以在任何模块中直接访问,如同内置函数那样。不过鉴于 __builtins__ 的特殊性,这似乎不是个好主意。
```
>>> __builtins__.b = 'builtins'
>>> b
'builtins'
>>> 
>>> g = 'globals'
>>> 
>>> def enclose():
...     e = 'enclosing'
...     def test():
...         l = 'locals'
...         print(l)
...         print(e)
...         print(g)
...         print(b)
...     return test
... 
>>> t = enclose()
>>> t()
locals
enclosing
globals
builtins
>>>
```
现在,获取外部空间的名字没问题了,但如果想将外部名字关联到一一个新对象,就需要使用用 global 关键字,指明要修改的是 globals 名字空间。Python 3 还提供了 nonlocal 关键字,用用来修改外部嵌套函数名字空间,
```
>>> x = 100
>>> hex(id(x))
'0x563e4e6b4940'
>>> 
>>> def test():
...     global x, y
...     x = 1000
...     y = 'Hello, World!'
...     print(hex(id(x)))
... 
>>> test()
0x7f2115f93d70
>>> print(x, hex(id(x)))
1000 0x7f2115f93d70
>>> 
>>> x, y
(1000, 'Hello, World!')
>>>
```
nonlocal
```
>>> def make_counter():
...     count = 0
...     def counter():
...         nonlocal count
...         count += 1
...         return count
...     return counter
... 
>>> mc = make_counter()
>>> print(mc())
1
>>> print(mc())
2
>>> print(mc())
3
>>>
```

## 4.4 闭包
闭包是指:当函数离开创建环境后,依然持有其上下文状态。比如下面的 a 和 b,在离开 test 函数后,依然持有 test.x 对象。
```
>>> def test():
...     x = [1, 2]
...     print(hex(id(x)))
...     
...     def a():
...         x.append(3)
...         print(hex(id(x)))
...     
...     def b():
...         print(hex(id(x)), x)
...     
...     return a, b
... 
>>> a, b = test()
0x7f4c9769a608
>>> 
>>> a()
0x7f4c9769a608
>>> 
>>> b()
0x7f4c9769a608 [1, 2, 3]
>>> 
>>> 
```

```
>>> def test(x):
...     def a():
...         print(x)
...     
...     print(hex(id(a)))
...     return a
... 
>>> a1 = test(100)
0x7f4c9768ee18
>>> 
>>> a2 = test("hi")
0x7f4c976ac048
>>> 
>>> a1()
100
>>> a2()
hi
>>> 



