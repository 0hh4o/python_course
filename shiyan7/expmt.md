# 实验七 Python面向对象编程

班级： 21计科03

学号： B20210302325

姓名： 欧阳浩

Github地址：<https://github.com/0hh4o/python_course>

CodeWars地址：<https://www.codewars.com/users/0hh4o>

---

## 实验目的

1. 学习Python类和继承的基础知识
2. 学习namedtuple和DataClass的使用

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

Python面向对象编程

完成教材《Python编程从入门到实践》下列章节的练习：

- 第9章 类

---

### 第二部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：面向对象的海盗

难度： 8kyu

啊哈，伙计!

你是一个小海盗团的首领。而且你有一个计划。在OOP的帮助下，你希望建立一个相当有效的系统来识别船上有大量战利品的船只。
对你来说，不幸的是，现在的人很重，那么你怎么知道一艘船上装的是黄金而不是人呢？

你首先要写一个通用的船舶类。

```python
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
```

每当你的间谍看到一艘新船进入码头，他们将根据观察结果创建一个新的船舶对象。

- `draft`吃水 - 根据船在水中的高度来估计它的重量
- `crew`船员 - 船上船员的数量

`Titanic = Ship(15, 10)`

任务

你可以访问船舶的 "draft(吃水) "和 "crew(船员)"。"draft(吃水) "是船的总重量，"船员 "是船上的人数。
每个船员都会给船的吃水增加1.5个单位。如果除去船员的重量后，吃水仍然超过20，那么这艘船就值得掠夺。任何有这么重的船一定有很多战利品!
添加方法
`is_worth_it`
来决定这艘船是否值得掠夺。

例如：

```python
Titanic.is_worth_it()
False
```

祝你好运，愿你能找到金子!

代码提交地址：
<https://www.codewars.com/kata/54fe05c4762e2e3047000add>

---

#### 第二题： 搭建积木

难度：7kyu

写一个创建Block的类（Duh.）
构造函数应该接受一个数组作为参数，这个数组将包含3个整数，其形式为`[width, length, height]`，Block应该由这些整数创建。

定义这些方法:

- `get_width()` return the width of the `Block`
- `get_length()` return the length of the `Block`
- `get_height()` return the height of the `Block`
- `get_volume()` return the volume of the `Block`
- `get_surface_area()` return the surface area of the `Block`

例子：

```python
b = Block([2,4,6]) # create a `Block` object with a width of `2` a length of `4` and a height of `6`
b.get_width() # return 2    
b.get_length() # return 4
b.get_height() # return 6
b.get_volume() # return 48
b.get_surface_area() # return 88
```

注意： 不需要检查错误的参数。

代码提交地址：
<https://www.codewars.com/kata/55b75fcf67e558d3750000a3>

---

#### 第三题： 分页助手

难度：5kyu

在这个练习中，你将加强对分页的掌握。你将完成PaginationHelper类，这是一个实用类，有助于查询与数组有关的分页信息。
该类被设计成接收一个值的数组和一个整数，表示每页允许多少个项目。集合/数组中包含的值的类型并不相关。

下面是一些关于如何使用这个类的例子：

```python
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid
```

代码提交地址：
<https://www.codewars.com/kata/515bb423de843ea99400000a>

---

#### 第四题： 向量（Vector）类

难度： 5kyu

创建一个支持加法、减法、点积和向量长度的向量（Vector）类。

举例来说：

```python
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
```

如果你试图对两个不同长度的向量进行加减或点缀，你必须抛出一个错误。
向量类还应该提供：

- 一个 `__str__` 方法，这样 `str(a) === '(1,2,3)'` 
- 一个equals方法，用来检查两个具有相同成分的向量是否相等。

注意：测试案例将利用用户提供的equals方法。

代码提交地址：
<https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4>

---

#### 第五题： Codewars风格的等级系统

难度： 4kyu

编写一个名为User的类，用于计算用户在类似于Codewars使用的排名系统中的进步量。

业务规则：

- 一个用户从等级-8开始，可以一直进步到8。
- 没有0（零）等级。在-1之后的下一个等级是1。
- 用户将完成活动。这些活动也有等级。
- 每当用户完成一个有等级的活动，用户的等级进度就会根据活动的等级进行更新。
- 完成活动获得的进度是相对于用户当前的等级与活动的等级而言的。
- 用户的等级进度从零开始，每当进度达到100时，用户的等级就会升级到下一个等级。
- 在上一等级时获得的任何剩余进度都将被应用于下一等级的进度（我们不会丢弃任何进度）。例外的情况是，如果没有其他等级的进展（一旦你达到8级，就没有更多的进展了）。
- 一个用户不能超过8级。
- 唯一可接受的等级值范围是-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8。任何其他的值都应该引起错误。

逻辑案例：

- 如果一个排名为-8的用户完成了一个排名为-7的活动，他们将获得10的进度。
- 如果一个排名为-8的用户完成了排名为-6的活动，他们将获得40的进展。
- 如果一个排名为-8的用户完成了排名为-5的活动，他们将获得90的进展。
- 如果一个排名-8的用户完成了排名-4的活动，他们将获得160个进度，从而使该用户升级到排名-7，并获得60个进度以获得下一个排名。
- 如果一个等级为-1的用户完成了一个等级为1的活动，他们将获得10个进度（记住，零等级会被忽略）。

代码案例：

```python
user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
```

代码提交地址：
<https://www.codewars.com/kata/51fda2d95d6efda45e00004e>

---

### 第三部分

使用Mermaid绘制程序的**类图**

安装VSCode插件：

- Markdown Preview Mermaid Support
- Mermaid Markdown Syntax Highlighting

使用Markdown语法绘制你的程序绘制程序类图（至少一个），Markdown代码如下：

![程序类图](/Experiments/img/2023-08-08-22-47-53.png)

显示效果如下：

```mermaid
---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
```

查看Mermaid类图的语法-->[点击这里](https://mermaid.js.org/syntax/classDiagram.html)

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果
### 第二部分：Codewars Kata挑战
#### 第一题：面向对象的海盗
![](7.2.1.png)
代码如下：
```python
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if self.draft - (1.5*self.crew) > 20 :
            return True
        else:
            return False
```
#### 第二题：搭建积木
![](7.2.2.png)
代码如下：
```python
class Block:
    def __init__(self,data):
        self.height = data[2]
        self.width = data[0]
        self.length = data[1]
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_volume(self):
        return (self.height*self.length*self.width)
    def get_surface_area(self):
        return ((self.height*self.width*2)+(self.height*self.length*2)+(self.length*self.width*2))
```
#### 第三题：分页助手
![](7.2.3.png)
代码如下：
```python
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return -(-len(self.collection) // self.items_per_page)

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1:
            if (len(self.collection) % self.items_per_page) == 0:
                return self.items_per_page
            else:
                return len(self.collection) % self.items_per_page
        else:
            return self.items_per_page

    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        else:
            return item_index // self.items_per_page
```
#### 第四题：向量(Vector)类
![](7.2.4.png)
代码如下：
```python
import math

class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return '(' + ','.join(map(str,self.components)) + ')'

    def __len__(self):
        return len(self.components)

    def add(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length")
        return Vector([x + y for x, y in zip(self.components,other.components)])

    def subtract(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length")
        return Vector([x - y for x, y in zip(self.components,other.components)])

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length")
        return sum(x * y for x, y in zip(self.components,other.components))

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def equals(self, other):
        return self.components == other.components
```
#### 第五题：Codewars风格的等级系统
![](7.2.5.png)
代码如下：
```python
class User:
    def __init__(self,rank = -8,progress = 0):
        self.rank = rank
        self.progress = progress
    def progress(self):
        return self.progress
    def rank(self):
        return self.rank
    def inc_progress(self,activity_rank):
        if activity_rank < -8 or activity_rank == 0 or activity_rank > 8:
            raise ValueError("Invalid activity rank")

        rank_diff = activity_rank - self.rank
        if (self.rank*activity_rank < 0) and (rank_diff == -2):
            rank_diff += 1
        elif self.rank*activity_rank < 0:
            rank_diff -= 1

        if rank_diff == 0:
            progress = 3
        elif rank_diff == -1:
            progress = 1
        elif rank_diff > 0:
            progress = 10 * rank_diff * rank_diff
        else:
            progress = 0

        if rank_diff < 0:
            progress = max(-50, progress)

        self.progress += progress

        while self.progress >= 100:
            self.progress -= 100
            if self.rank == -1:
                self.rank += 2
            else:
                self.rank += 1
                if self.rank == 0:
                    self.rank = 1

        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
```
### 第三部分：使用Mermaid绘制程序的类图
```mermaid
---
title: Building blocks(搭建积木)
---
classDiagram
    Block : get_width()
    Block : get_length()
    Block : get_height()
    Block : get_volume()
    Block : get_surface_area()
```
## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. Python的类中__init__方法起什么作用？
答：__init__方法是一个特殊的方法，用于初始化新创建的对象。当你实例化一个类时，__init__方法会被自动调用，用来初始化对象的属性。在__init__方法中，你可以设置对象的初始状态，为对象的属性赋初值，或者执行其他必要的初始化操作。这样，当你创建一个新的对象时，它就会自动进行初始化，而不需要在创建对象后手动设置属性。
2. Python语言中如何继承父类和改写（override）父类的方法。
答：在python中可以通过创建子类来继承父类并且通过定义一个同名的方法来改写父类的方法，在子类中定义了一个与父类同名的方法时，子类的方法会覆盖父类的方法，这样可以根据需要在子类中定制特别的行为而不会影响父类的其他实例。
3. Python类有那些特殊的方法？它们的作用是什么？请举三个例子并编写简单的代码说明。
答：
1、__init__方法：用于初始化新创建的对象，当一个新对象被创建时这个方法会自动调用。
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建一个Person对象
person = Person("Alice", 25)
```
2、__str__: 用于返回对象的字符串表示，当你使用print函数或str函数时，会自动调用__str__方法。
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"

# 创建一个Person对象并打印它
person = Person("Alice", 25)
print(person)  # 输出结果为 "Person: Alice, 25 years old"****
```
3、用于定义对象的加法操作，当你对两个对象使用加法运算符时，会自动调用__add__方法。
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# 创建两个Point对象并进行加法运算
p1 = Point(1, 2)
p2 = Point(3, 4)
result = p1 + p2
print(result.x, result.y)  # 输出结果为 "4 6"
```
## 实验总结
这次实验中我学习了如何在python中创建类，使用类，创建实例并调用实例的方法来实现目的，还学会了一些python的类中的特殊方法，如init、add、str等。
