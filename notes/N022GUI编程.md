###GUI编程(Tkinter)

Python 提供了多个图形开发界面的库，几个常用 Python GUI 库如下：

- **Tkinter：** Tkinter 模块(Tk 接口)是 Python 的标准 Tk GUI 工具包的接口 .Tk 和 Tkinter 可以在大多数的 Unix 平台下使用,同样可以应用在 Windows 和 Macintosh 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。
- **wxPython：**wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能键全的 GUI 用户界面。
- **Jython：**Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython 使用 Java 的模块。Jython 几乎拥有标准的Python 中不依赖于 C 语言的全部模块。比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。Jython 可以被动态或静态地编译成 Java 字节码。

####Tkinter 编程

Tkinter 是 Python 的标准 GUI 库。Python 使用 Tkinter 可以快速的创建 GUI 应用程序。

由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库、而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。

> **注意**：Python3.x 版本使用的库名为 tkinter,即首写字母 T 为小写。
>
> ```
> import tkinter
> ```

创建一个GUI程序

- 1、导入 Tkinter 模块
- 2、创建控件
- 3、指定这个控件的 master， 即这个控件属于哪一个
- 4、告诉 GM(geometry manager) 有一个控件产生了。

实例:

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
top = Tkinter.Tk()
# 进入消息循环
top.mainloop()
```

以上代码执行结果如下图:

![tkwindow](http://www.runoob.com/wp-content/uploads/2013/12/tkwindow.jpg)

实例2：

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环
```

以上代码执行结果如下图:

![img](http://www.runoob.com/wp-content/uploads/2013/12/tk.jpg)

####Tkinter 组件

Tkinter的提供各种控件，如按钮，标签和文本框，一个GUI应用程序中使用。这些控件通常被称为控件或者部件。

目前有15种Tkinter的部件。我们提出这些部件以及一个简短的介绍，在下面的表:

| 控件           | 描述                                     |
| ------------ | -------------------------------------- |
| Button       | 按钮控件；在程序中显示按钮。                         |
| Canvas       | 画布控件；显示图形元素如线条或文本                      |
| Checkbutton  | 多选框控件；用于在程序中提供多项选择框                    |
| Entry        | 输入控件；用于显示简单的文本内容                       |
| Frame        | 框架控件；在屏幕上显示一个矩形区域，多用来作为容器              |
| Label        | 标签控件；可以显示文本和位图                         |
| Listbox      | 列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户     |
| Menubutton   | 菜单按钮控件，由于显示菜单项。                        |
| Menu         | 菜单控件；显示菜单栏,下拉菜单和弹出菜单                   |
| Message      | 消息控件；用来显示多行文本，与label比较类似               |
| Radiobutton  | 单选按钮控件；显示一个单选的按钮状态                     |
| Scale        | 范围控件；显示一个数值刻度，为输出限定范围的数字区间             |
| Scrollbar    | 滚动条控件，当内容超过可视化区域时使用，如列表框。.             |
| Text         | 文本控件；用于显示多行文本                          |
| Toplevel     | 容器控件；用来提供一个单独的对话框，和Frame比较类似           |
| Spinbox      | 输入控件；与Entry类似，但是可以指定输入范围值              |
| PanedWindow  | PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。 |
| LabelFrame   | labelframe 是一个简单的容器控件。常用与复杂的窗口布局。      |
| tkMessageBox | 用于显示你应用程序的消息框。                         |

####标准属性

标准属性也就是所有控件的共同属性，如大小，字体和颜色等等。

| 属性        | 描述    |
| --------- | ----- |
| Dimension | 控件大小； |
| Color     | 控件颜色； |
| Font      | 控件字体； |
| Anchor    | 锚点；   |
| Relief    | 控件样式； |
| Bitmap    | 位图；   |
| Cursor    | 光标；   |

####几何管理

Tkinter控件有特定的几何状态管理方法，管理整个控件区域组织，一下是Tkinter公开的几何管理类：包、网格、位置

| 几何方法    | 描述   |
| ------- | ---- |
| pack()  | 包装；  |
| grid()  | 网格；  |
| place() | 位置；  |





Python支持多种图形界面的第三方库，包括：

- Tk
- wxWidgets
- Qt
- GTK

等等。

但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。本章简单介绍如何使用Tkinter进行GUI编程。

### Tkinter

我们来梳理一下概念：

我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；

Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；

Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

所以，我们的代码只需要调用Tkinter提供的接口就可以了。

### 第一个GUI程序

使用Tkinter十分简单，我们来编写一个GUI版本的“Hello, world!”。

第一步是导入Tkinter包的所有内容：

```
from Tkinter import *

```

第二步是从`Frame`派生一个`Application`类，这是所有Widget的父容器：

```python
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

```

在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。

`pack()`方法把Widget加入到父容器中，并实现布局。`pack()`是最简单的布局，`grid()`可以实现更复杂的布局。

在`createWidgets()`方法中，我们创建一个`Label`和一个`Button`，当Button被点击时，触发`self.quit()`使程序退出。

第三步，实例化`Application`，并启动消息循环：

```python
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

```

GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。因此，如果消息处理非常耗时，就需要在新线程中处理。

运行这个GUI程序，可以看到下面的窗口：

![tk-hello-world](https://cdn.liaoxuefeng.com/cdn/files/attachments/00141049329759550860dddd40c49d0806bbf0b3cf7d2f7000)

点击“Quit”按钮或者窗口的“x”结束程序。

### 输入文本

我们再对这个GUI程序改进一下，加入一个文本框，让用户可以输入文本，然后点按钮后，弹出消息对话框。

```python
from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

```

当用户点击按钮时，触发`hello()`，通过`self.nameInput.get()`获得用户输入的文本后，使用`tkMessageBox.showinfo()`可以弹出消息对话框。

程序运行结果如下：

![tk-say-hello](https://cdn.liaoxuefeng.com/cdn/files/attachments/001410493505348d04f0ae2b4274939ab7cbad2c9301f2f000)

### 小结

Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。

源码参考：<https://github.com/michaelliao/learn-python/tree/master/gui>