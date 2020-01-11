---
layout: post
categories: Python
tag: []
date: 2019-10-09
---



Copied article 

目前，[Doxygen](http://www.stack.nl/~dimitri/doxygen/) 对 python的支持有限。 它可以识别 python 注释，但其他情况下将该语言视为是 Java。 它不理解基本的python 语法结构，如字符串。关键字参数。生成器。嵌套函数。decorator或者lambda表达式。 它同样不理解传统的结构，比如doctest或者zope风格接口。 但是它支持内联过滤器，它可以用来使输入源代码更像它所期望的。

优秀的 [doxypy插件使得在文档中嵌入Doxygen命令，并按照Doxygen输入过滤过程的规则将这些文档文件转换为Doxygen可以识别注释。](https://github.com/Feneric/doxypy) 然而，它并没有解决以前提到过的任何困难领域。

这个项目开始于doxypy的fork，但很快就变得非常明显了。 它在这一点上共享了很少的相同代码的( 如果有的话)。 它是为了支持所有相同的命令行 选项作为 doxypy，但是处理除了，之外的它的他 python 语法。



## 支持的附加语法

python 可以在函数和类中具有函数和类。 Doxygen通过它的名称空间的概念理解这个概念。 这个过滤器可以提供Doxygen标记标记每个函数和类上的名称空间。 这解决了Doxygen合并内部函数'文档和父文档的文档的问题。

名称以双下划线开头的python 类成员会被破坏，并由语言保持 private。 Doxygen还不理解本机，因此这个过滤器还提供了Doxygen标签来标记诸如 private 这样的变量。

python 经常在文档文档中嵌入 doctest。 这个过滤器使标记文档的这些部分很简单，以便它们显示为代码。

to将类定义重载为接口定义，使用嵌入变量分配来识别属性，并使用特定的函数调用。 而且，它们经常没有代码表之外的代码，所以如果删除文档文件，将导致损坏的代码。 这里过滤器对这些接口有基本的理解并相应地处理它们，并提供了。

从根本上讲，python 文档是用于人类和非机器的，不应该超过传统结构文本的特殊标记。 这个过滤器以启发式方式检查 python 文档，或者类似于 [PEP 257中复杂的示例的示例，或者通常遵循更严格的Google python 风格指南](http://www.python.org/dev/peps/pep-0257/)会自动添加适当的Doxygen标记。



## 工作原理

这个项目采用了与doxypy完全不同的方法。 我们使用 python 抽象语法树 MODULE 来提取感兴趣的项目，而不是使用 正规表达式 绑定到状态机。 如果启用了AUTOBRIEF选项，则通过一组 正规表达式 和一组协同程序/使用者对来解析 of。



## 示例

这里过滤器将正确处理代码，如下面的工作( 虽然做作) 示例：

复制代码

```
defmyfunction(arg1, arg2, kwarg='whatever.'):
 """ Does nothing more than demonstrate syntax. This is an example of how a Pythonic human-readable docstring can get parsed by doxypypy and marked up with Doxygen commands as a regular input filter to Doxygen. Args: arg1: A positional argument. arg2: Another positional argument. Kwargs: kwarg: A keyword argument. Returns: A string holding the result. Raises: ZeroDivisionError, AssertionError, & ValueError. Examples:>>> myfunction(2, 3) '5 - 0, whatever.'>>> myfunction(5, 0, 'oops.') Traceback (most recent call last):. . . ZeroDivisionError: integer division or modulo by zero>>> myfunction(4, 1, 'got it.') '5 - 4, got it.'>>> myfunction(23.5, 23, 'oh well.') Traceback (most recent call last):. . . AssertionError>>> myfunction(5, 50, 'too big.') Traceback (most recent call last):. . . ValueError"""assertisinstance(arg1, int)
 if arg2 >23:
 raiseValueErrorreturn'{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```

有几点需要注意：

1.不使用特殊标记。 最佳实践人员可以阅读节标题。

2.允许一些灵活性。 部分常见的名称被接受，项和描述可以用冒号或者划线分隔。

- 必须是第一个项目，并且不能超过一行。

4.引入示例部分的所有内容都将被视为代码，因这里它是for的完美位置。

其他更全面的例子可以在测试区域中找到。



## 安装 doxypypy

可以使用 `pip` 或者 `easy_install` 进行安装。 运行其中之一：

复制代码

```
pip install doxypypy
```

或者：

复制代码

```
easy_install doxypypy
```

具有管理员特权应该执行以下操作。



## 预览doxypypy输出

成功安装后，可以从 命令行 运行 doxypypy，以预览过滤后的结果：

复制代码

```
doxypypy -a -c file.py
```

通常，要将输出重定向到文件，以便在文本编辑器中查看：

复制代码

```
doxypypy -a -c file.py > file.py.out
```



## 从Doxygen调用 doxypypy

要使Doxygen通过doxypypy运行你的python 代码，请在你的Doxyfile中设置FILTER_PATTERNS标记，如下所示：

复制代码

```
FILTER_PATTERNS = *.py=py_filter
```

py_filter必须在路径中可用作为 shell script ( 或者 Windows 批处理文件)。 如果你希望在特定目录中运行 py_filter，可以包括完整路径或者相对路径。

对于unix操作系统，py_filter应该喜欢类似这样的东西：

复制代码

```
#!/bin/bashdoxypypy -a -c $1
```

在 Windows 中，批处理文件应该命名为 py_filter.bat,，并且只需要包含一行：

复制代码

```
doxypypy -a -c %1
```

正常运行Doxygen现在应该通过doxypypy运行所有的python 代码。 一定要仔细浏览and输出，以确保正确地找到了arraylist并执行了 doxypypy。