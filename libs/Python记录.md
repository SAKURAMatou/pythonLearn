

单行注释#，多行注释'''  '''包裹的内容。

python注释的PEP8规范：1、单行注释#+空格开头；2、代码文件最后一行是空行

数据类型：数据类型              结构类型
         int float bool str  list set map tuple

## 数据类型

Number（数字）：有符号整形（int）；长整型（long，python2中的数据类型，python3中合并至整形）；浮点型（float，默认小数点后六位）；复数（complex）

布尔类型（bool）：True，False

字符类型（str）

元祖（Tuple)

字典（dictionary）

通过函数type来获取变量的数据类型

## 关键字，标识符

标识符：由字母、数字、下划线组成的且不是由下划线开头，标识符区分大小写

查看关键字：

```python
import keyword
print(keyword.kwlist)
```

## 运算符

### 算数运算符

| 运算符 | 描述   | 备注                                                         |
| ------ | ------ | ------------------------------------------------------------ |
| +      | 加     | 两数相加                                                     |
| -      | 减     | 可以得到负数                                                 |
| *      | 乘     | a*b：1、若其中一个是字符串则得到重复一定次数的字符串；2、a,b都为数据类型（整数，浮点，复数等）时得到数据类型，自动转化；3、a,b都为字符串时异常； |
| /      | 除     | 结果是小数整除时保留一位小数，不是整除时最多保留16位         |
| //     | 取整除 | 返回商的整数部分，9//2返回4,9.0//2返回2.0自动转化浮点        |
| %      | 取余   | 返回商的余数部分                                             |
| **     | 指数   | 2`**`3返回8；2.0`**`3返回8.0                                 |

优先级：`**`高于`*` `/` `%` `//`  高于 + - ；不同数据类型运算时会转化整形到浮点

### 赋值运算符

```
= ：将右边值赋值给左边变量
```

### 复合运算符

```
+=；-=；/=；//=；%=；等
```

### 比较运算符

```
==  != < ; >  >=  <= 
```



### 逻辑运算符

```
逻辑运算符可以连接两个表达式进行逻辑运算决定整体结果
and 逻辑与；有短路现象
or  逻辑或；有短路现象
not 逻辑非
```



## 输出

```python
print() 
1、可以打印多个参数‘，’区分，
2、入参表达式输出表达式的结果
3、格式化输出：%s字符串，%d int；%f 浮点；通过%标识需要输出的内容
name="Tom"
print("欢迎%s加入"%name)
多个入参需要使用（）
print('我是%s,年龄%d，身高%f' %(name,age,height))
浮点型%.nf指定保留的小数位数
print('浮点%f,保留小数%.2f'%(ft,ft))
注：格式化输出的字符串模板中不能有单独的%,要打印%时需要使用%%才行；
4、3.6版本开始支持f-string，通过{}占位，
print(f'我是{name},年龄{age}，身高{height}')
#我是Tom,年龄45，身高175.6
5、end参数可以指定打印结束的字符，默认的值是换行\n
sep参数可以指定多个参数之间的分隔符
空：None 对空的判断使用 is not is

可迭代器（不产生数据，需要驱动器驱动才能产生数据） ：range list        
range(min,max)取不到max


```

## 输入

从键盘获取输入内容存入程序，通过input()函数实现，

input可以有入参，如餐位给用户的提示字符，遇到回车后表示输入结束；并且输入获取到字符串

```python
name = input('输入:')
```

## 类型转换

int()：转整形

float()：转浮点型

eval():还原数据类型（将字符串的引号去掉）

变量

Python中没有数据类型，变量保存数据的地址。

变量比较 == > < >= <= !=

值的类型：

整形（数据长度可变包含int lang）、 浮点类型 、科学计数型、布尔类型 True 和False（True 本质是数字1 False是0，True+false=0）

int() 转化为整形数据； float()转化为浮点型； str()转字符串；

赋值，连续赋值以及配对赋值

```python
i=j=100#从右向左连续赋值
i,j=1,2#i=1,j=2
```

## 条件语句

```python
1、基本结构
if condition:
    #满足条件时执行的代码块，通过缩进区分
2、if else 结构
if condition:
    pass
else:
    pass
3、else if 结构
if condition:
    pass
elif:
    pass
else:
    pass
#三元表达式
值1 if 条件  else 值2 #满足条件时 取值1 否则取值2

```

```python
# 条件基本结构
# age = input('输入年龄')
# age=int(age)
# if age >= 18:
#     print('哥已经%d了，为所欲为' % age)
# print('判断结束')
# if else 结构
# age = input('输入年龄')
# age=int(age)
# if age >= 18:
#     print('哥已经%d了，为所欲为' % age)
# else:
#     print('不满18岁回家玩吧')
# print('判断结束')
# else if结构
# grand = input('请输入分数：')
# grand = int(grand)
# if grand > 100:
#     print('无效分数')
# elif grand >= 90:
#     print('成绩优秀')
# elif grand >= 70:
#     print('成绩良好')
# elif grand >= 60:
#     print('成绩一般')
# else:
#     print("不及格")
# print('运行结束')
# # 条件嵌套
# money = int(input('投币:'))
# count = int(input('上车人数:'))
# if money//count >= 2:
#     if count < 5:
#         print('成功上车！')
#     else:
#         print('座位不足')
# else:
#     print('上车失败！')
import random
print(random.randint(1, 5))
# 三目运算
age = int(input('输入年龄'))
print('哥已经%d了，为所欲为' % age) if age >= 18 else print('不满18岁回家玩吧')
print('判断结束')
```



## 循环语句

```python
1，while循环
s,i=0,1
while i<=100:
    s+=i
    i+=1
2、for 循环，又称for遍历
for 变量 in 列表或者其他可迭代对象
3、循环else结构
for xx in XX:
    循环体
else :
    xxx # for 循环代码运行结束，且不是被break终止而结束时执行
```

```python
# a = int(input('输入累加数:'))
# b, c = 0, 0
# while b <= a:
#     if(b%2==0):
#       c += b
#     b += 1
# print("求和结果：%d" % c)
# 对偶数进行累加
a = int(input('输入累加数:'))
b, c = 0, 0
while b <= a:
    c += b
    b += 2
print("求和结果：%d" % c)
# for 循环
# str='hello world'
# for i in str:
#     print(i)
# for 和 range函数结合;range函数单入参时从0开始
# for i in range(5):
#     print(i)
# range函数双入参a,b取值范围[a,b)
# for i in range(2,6):
#     print(i)
# range函数三入参a,b,c取值范围[a,b)，步长为c，即数据间隔为步长
for i in range(2,6,2):
    print(i)
```



## 字符串

通过单引号，双引号，三引号包裹的内容为字符串；若想要在字符串中出现单引号或双引号，则外层需要使用不一样的引号包裹即可，或者使用三引号

### 原始字符串

原始字符串符号r，取消字符串中的转义字符效果

```python
my_str = '''字符串测试，包含单引号'',包含双引号""'''
print(type(my_str), my_str)
s2=r"hello \n world"
输出hello \n world
```

repr():获取原始字符串方法

### 字符串格式化

1、占位符；2、f-string

### 常用操作以及内置方法

#### 按索引取值

下标又称索引，可以为正数，负数；正数下标从0开始，负数下标从-1开始；

从0开始，取字符串对应的字符，如果索引为负数表示从最右边开始取值

```python
str='hello word'
print(str[1])
print(str[-2])
#输出
e
r
```

#### 切片[初始值:终止值:步长]

取字符串中指定的一段，不同于java中的取字符串子串的方法，python的切片方法，取到第一个值取不到最后一个值（顾头不顾尾），截取的字符长度为(终止值-初始值)/步长的结果（不为整数时+1）

步长的默认值为1，可以不写；

切片的初始值和终止值可以不写，不写时初始值默认0，终止值默认len()的结果

```python
str='0123456789'
print('双入参',str[1:5])#输出1234
print('三入参',str[1:5:1])#输出1234
print('三入参',str[1:5:2])#输出13
步长默认值时初始值大于终止值时返回空字符串
print(my_str[5:1])#打印空字符串，也是str类型
print(my_str[5:1:-1])#步长为负时逆序切片字符串。输出5432
```

#### 计算字符串长度len方法

成员运算 in ，not in 

字符串运算，

加法：拼接

乘法：字符串重复

```python
s3="字符串"*3等效s3="字符串字符串字符串"
```

### 字符串函数

#### find(sub_str,strat,end) 

查找是否包含某个子串,sub_str:要查找的子串；strat：起始位置；end：结束位置

```python
my_str="hello word, this is my python"
#find函数返回查找到的子串的第一个字符下标（从左开始）
#rfind表示从右边开始查找
print(my_str.find('ll'))#输出2
print(my_str.rfind('ll'))#输出2
print(my_str.find('l'))#输出2
print(my_str.rfind('l'))#输出3
```

#### index(sub_str,strat,end) 

同find但，子串不存在时异常

```python
my_str="hello word, this is my python ll "
print(my_str.index('ll'))#输出2
print(my_str.rindex('ll'))#输出30
```

#### count(sub_str,strat,end) 

参数含义同find，count函数返回查找的子串出现的次数，没有时返回0；

```python
my_str="hello word, this is my python ll "
print(my_str.count("is"))#返回2
```

#### replace(old_str,new_str,count) 

替换字符串中的指定子串old_str为new_str

count是替换次数，默认全部替换

```python
my_str="hello word, this is my python ll "
print(my_str.replace("is","IS",1))#输出hello word, thIS is my python ll
```

#### split(sub_str,count)

将字符串按照sub_str进行切割，count分割次数，默认全部分割；

rsplit()从右边开始切割

```python
my_str="hello word, this is my python ll "
print(my_str.split())
#输出['hello', 'word,', 'this', 'is', 'my', 'python', 'll']
print(my_str.split(" ",1))
#输出['hello', 'word, this is my python ll ']
print(my_str.rsplit(" ",1))
#输出['hello word, this is my python ll', '']
```

join(可迭代对象)

将字符串添加至可迭代对象的每个元素之间

```python
my_str="_".join('hello')
print(my_str)
#输出h_e_l_l_o
my_list=['hello','my','python']
print("_*_".join(my_list))
#输出hello_*_my_*_python
```

#### 其他不常用函数

capitalize()：字符串开头字母变大写

title()：单词首字母大写

upper()，lower()：字母大小写转化

startswith()，endswith()：判断字符串开头和结尾

center()，ljust()，rjust()：字符串位置函数，入参为整数

strip()，lstrip()，rstrip()：去除字符串左右的空格，不能删除字符串中间的空格

partition(sub_str)：根据sub_str把字符串分割为包含sub_str的三部分

```python
my_str = "hello word- this is my python LL "
print(my_str.partition("-"))
#输出('hello word', '-', ' this is my python LL ')
```

## 容器

### 列表

一种数据类型，存放多个数据，列表的数据类型可以是任意类型

#### 列表的定义

```python
my_list1=[]
my_list2= list()
```

列表支持切片和下标操作；列表可以使用下标操作修改数据

```python
my_list = ['P']
my_list[1:] = list('ython')
print(my_list)
#输出
['P', 'y', 't', 'h', 'o', 'n']
```



#### 列表添加数据

append() ：尾部追加数据

insert(下标，元素)：在指定下标位置插入元素，原元素后移 

extend(可迭代对象)：把可迭代对象中的数据逐个添加至列表末尾

```python
my_list1=['a','b','c']
str='1230'
my_list1.extend(str)
print(my_list1)
#输出['a', 'b', 'c', '1', '2', '3', '0']
```

#### 列表的查询

index()：查询数据的下标，不存在时异常

count():统计元素出现次数

in/not in :是否在列表中存在

```python
my_list1 = ['a', 2, 3.14, True,False]
num1= 3.14 in my_list1
num2=3.14 not in my_list1
print(num1,num2)
print(my_list1.index(3.14))
print(my_list1.count(0))
```

#### 列表删除

直接删除原列表中的数据

remove(要删除的元素)：若元素不存在会异常

pop(index)： 栈操作，指定下标时弹出对应下标元素，即删除的数据的内容并返回

del arr[index] ：删除列表的指定的下标的元素

```python
my_list1.remove('a')
print(my_list1)
my_list1.pop()
print(my_list1)
my_list1.pop(1)
print(my_list1)
del my_list1[2]
print(my_list1)
```

#### 列表排序

前提：列表中数据类型一致

sort()：排序默认升序排序、

sort(reverse=True)：降序排序

```python
my_list2=[1,2,4,9,6,2,5]
# my_list2.sort()
my_list2.sort(reverse=True)
print(my_list2)
```

sorted(列表)：对列表排序并返回一个新列表，不改变源列表；

sorted(列表,reverse=True)

```python
my_list2=[1,2,4,9,6,2,5]
my_list3=sorted(my_list2)
my_list4=sorted(my_list2,reverse=True)
print(my_list2,my_list3)
```

#### 逆置

通过列表切片或者reverse()实现列表逆置；切片不改变源列表，列表的内置方法改变源列表

```python
#逆置
print(my_list2[::-1])
my_list2.reverse()
print(my_list2)
```

### 元祖

使用小括号包裹，数据不能修改，故元祖没有增删改操作

查询：支持下标和切片访问，和数组的查询一样，

```python
#定义空元祖
my_tuple1=()
my_tuple2=tuple()
#定义单元素元祖必须要加逗号
my_tuple3=('a')#为小括号内的元素的数据类型
my_tuple4=('a',)#为元祖
```

### 字典

字典：dict，使用{}包裹的键值对{key1:value1,key2:value2,...}

字典的key可以是字符串和数字（int，float）

```python
#定义空字典
my_dict1={}
my_dict2=dict()
```

字典没有下标的概念，通过key访问字典内的元素；若key不存在时异常

```python
my_dict1={'name':"Tom",'age':18,"like":['学习','游戏']}
my_dict1['name']#获取到Tom
my_dict1['nam']#key不存在，抛异常
my_dict1.get('like')#返回['学习','游戏']，且key不存在时返回none
```

#### get()方法:

get(key,value)，key存在时返回对应的值不存在时返回vlaue，类似java中map的getOrDefault方法

```python
school=my_dict1.get("school","南邮")
print(my_dict1.get("school"),school)
#输出：None 南邮
get方法不会对不存在的key赋值，只会返回给定的值
```

len()方法

返回字典重元素个数：len(my_dict1)

#### 字典的修改

使用key进行增加和修改

字典[key]=value进行赋值以及修改

注意：int的1和float的1.0在字典中是同一个key；字典[1]和字典[1.0]指向同一个值

#### 字典的删除

del 字典[key]：删除指定的k-v

del 字典名：直接删除该字典的定义，

字典.pop(key)

字典.clear()：将字典全部数据删除，清空

#### 字典的遍历

for循环遍历获取字典的key

字典.keys()方法，获取dict_keys类型的对象

​        dict_keys对象可以使用list()方法转化为列表，也可以使用for循环遍历

字典.values()：获取所有的value，返回dict_values类型对象；同dict_keys对象

字典.items()：获取所有的k-v对象，返回dict_items对象，存放key和value，dict_items中每一个元素是一个元祖存放了key和value

```python
dict_items([('name', 'Tom'), ('age', 18), ('like', ['学习', '游戏'])])
```

拆包方式访问

```python
for k,v in my_item:
    print(k,v)
```



```python
my_dict1={'name':"Tom",'age':18,"like":['学习','游戏']}
for i in my_dict1:
    print(i)
#输出所有的key
my_key=my_dict1.keys()
print(type(my_key),my_key)
#输出<class 'dict_keys'> dict_keys(['name', 'age', 'like'])
```

### enumerate

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

enumerate9(可迭代对象,[start])：可选入参start表示开始的下标，指定开始的下标

```python
for i in enumerate(my_dict1):
    print(i)
    
#输出：
(0, 'name')
(1, 'age')
(2, 'like')    
```

### 公共方法

#### 运算符

| 运算符 | python示例     | 结果                                 | 描述           | 支持的数据类型                      |
| ------ | -------------- | ------------------------------------ | -------------- | ----------------------------------- |
| +      | [1,2]+[3,4]    | [1, 2, 3, 4]                         | 合并操作       | 字符串，列表，元祖                  |
| *      | ['hello']*4    | ['hello', 'hello', 'hello', 'hello'] | 复制           | 字符串，列表，元祖                  |
| in     | 1 in [1,2]     | 返回布尔类型                         | 判元素是否存在 | 字符串，列表，元祖，字典（操作key） |
| not in | 1 not in [1,2] | 返回布尔类型                         | 判元素是否存在 | 字符串，列表，元祖，字典（操作key） |

#### 其他方法

max()：字典操作的是key，key是字符串时比较的是第一个字符的ASCII码（第一个不同的字符）

min()：字典操作的是key，key是字符串时比较的是第一个字符的ASCII码（第一个不同的字符）

len()：

## 导包

随机数包

```python
 import random 
 random.randint(min，max)
#;min和max均可取到
```

## 函数

定义：def 函数名():

规范：函数体前后各有两行空格，函数的说明要放在函数定义的函数名下一行写，三引号包裹

help()：入参函数名，查看函数的说明文档

### 函数变量

在函数内无法直接修改全局变量（可以直接使用 ）；需要使用global关键字在函数内重新定义全局变量之后才能操作全局变量

```python
num =100


def func1():
    print(num) #改行报错，函数内没有定义num对象
    num=1      #相当于在函数内部定义一个局部变量num
    print(num)  

print(num)  
func1()  



num =100


def func1():
    global num
    print(num)
    num=1
    print(num)  
    
    
print('外部打印1',num)  
func1()  
print('外部打印2',num)
外部打印1 100
100
1
外部打印2 1
```

### 返回值

return 关键字进行返回值；代码遇到return关键字时会停止运行

return 可以返回多个数据，默认返回数据的类型的元祖

```python
def func3(a, b):
    c = a+b
    d = a-b
    return c, d


print(type(func3(8,6)))
<class 'tuple'>
```

### 入参

位置传参：顺序一致

关键字传参：顺序无所谓

```python
def func3(a, b, c):
    print("入参测试")
    
func3(1, 2, 3)
func3(4, c=4, b=6)    
```

### 缺省参数

在函数定义时，给形参默认值，该形参即为默认值；缺省参数定义在参数的最后，

在调用时，给缺省参数赋值的话，会使用传递的值

```python

def func4(a,b,c=5):
    print(a+b+c)


func4(1,2)#8
func4(1,2,3)#6
```

### 不定长入参

形参前添加*，形参转化为不定长，且通过元祖保存接收到的位置参数，

形参前添加**，形参转化为不定长，且通过字典保存接受到的参数，通过关键字传参

```python
def func5(*a,**k):
    print(type(a),a)
    print(type(k),k) 


func5(1,2,a=8,b=9)
#输出
<class 'tuple'> (1, 2)
<class 'dict'> {'a': 8, 'b': 9}
```

### 形参完整格式

普通形参，不定长的元祖形参，缺省形参，不定长字典形参

### 匿名函数

无参无返回值

```python
定义
lambda: print("无参无返回值函数")
运行：
(lambda: print("无参无返回值函数"))()
定义
f1=lambda: print("无参无返回值函数")
f1()
```

无参有返回值

```python
定义
lambda :1+2
f= lambda :1+2
print(f())
```

有参无返回值

```python
定义
lambda name:print(name*2)
f= lambda name:print(name*2)  #a=f2的话a为none
f("Tom")
输出
TomTom
```

有参有返回值

```python
定义
lambda a,b:a+b
f2= lambda a,b:a+b #a=f2的话a不为none
print(f2(1,2))
```

匿名函数的使用

作为入参中的函数使用

```python
def my_calc(a, b, fun):
    '''
    a 第一个数；b第二个数
    fun：要执行的运算
    :return 返回运算结果
    '''
    print("复杂的逻辑")
    num = fun(a, b)
    print("结果:", num)

my_calc(10,10,lambda a,b:a+b**2)
```

对字典排序

```python
my_list=[{'name':'clie','age':18,'salary':8500},
{'name':'Tom','age':18,'salary':8600},
{'name':'Alice','age':18,'salary':8400}]
#key指定排序的字段 
my_list.sort(key=lambda d:d['salary'])
print(my_list)
#对字符串的字符的字符数进行排序
my_list=['a','sfds','sdf', 'ewfdssdgs']
my_list.sort(key=len)
print(my_list)
```

按照多个条件排序时，sort(key=lambda a:(规则1，规则2，规则3,...)）

### 高阶函数

把函数作为入参传入的函数

`abs()`：求绝对值

`round()`：四舍五入

`map(func,list)`：将列表中的每一个元素都执行func方法运算，并将结果返回一个新的列表

`reduce(func,list)`：将func计算单结果和列表的下一个元素计算；要求func必须是双入参

```python
import functools
my_list1=[1,2,3,4,5]
print(functools.reduce(lambda a,b:a+b, my_list1))
```

`filter(func,list)`：通过func过滤得到满足func中条件的函数

## 拆包

组包：将多个数据放入容器中构成一个数据

拆包：将容器中的元素拆开给对象赋值。对象需要和容器数据数量一致；字典拆包时获取到key

```python
my_dict={'name':'Tom','age':165}
name,age=my_dict
print(name,age)
#输出：name age
```

## 引用

可以使用id()查看变量的引用，

赋值运算可以改变引用

```python
a=[1,2]
b=a        #将a的地址给b，所以a和b指向相同的地址
a.append(3)
print(b)
#输出[1, 2, 3]

my_list1=[1,2,3,4]
my_list2=my_list1
my_list2[1]=9
print(my_list1,id(my_list1))
print(my_list2,id(my_list2))
#输出
[1, 9, 3, 4] 2062449857032
[1, 9, 3, 4] 2062449857032
```

可变不可变

可变：在不改变引用（内存地址）的前提下改变变量的数据；

不可变类型：int float str bool tuple

可变类型：list dict

交互终端中有小整数概念，范围-5到255，范围外的数据会重新开辟内存

引用和拆包组合

```python
def func(*args, **kwargs):
    print('args',args)
    print('kwargs',kwargs)
    return sum
func(my_list) #将my_list作为一个入参传入
# 输出args ([1, 2, 3, 4, 5],)
# kwargs {}
func(*my_list) #将my_list拆包，列表中的每一个元素作为入参传入
# 输出
# args (1, 2, 3, 4, 5)
# kwargs {}
func(my_dict) #将my_dict作为一个入参传入args位置
# 输出
# args ({'a': 6, 'b': 7, 'c': 8},)
# kwargs {}
func(*my_dict)#将my_dict拆包，把对应的key传入args位置
# 输出
# args ('a', 'b', 'c')
# kwargs {}
func(**my_dict)#将my_dict拆包,把字典内的元素传入关键字参数kwargs
# 输出
# args ()
# kwargs {'a': 6, 'b': 7, 'c': 8}
```

## 列表推导式

快速生成一个列表

变量=[数据生成规则 for 临时变量 in 可迭代对象 [if 条件]]

```python
my_list1=[i for i in range(5)]
print(my_list1)
# [0, 1, 2, 3, 4]

my_list2=[i*10 for i in range(5)]
print(my_list2)
#[0, 10, 20, 30, 40]

my_list3=[f'num{i*10}' for i in range(5)]
print(my_list3)
#['num0', 'num10', 'num20', 'num30', 'num40']

my_list4=[f'num{i*10}' for i in range(5) if i%2==0]
print(my_list4)
#['num0', 'num20', 'num40']
```

变量=[数据生成规则 for i in 可迭代对象 for j in 可迭代对象 [if 条件]]

字典推导式，类似列表推导式，

变量={数据生成规则 for 临时变量 in 可迭代对象 [if 条件]}

变量={数据生成规则 for i in 可迭代对象 for j in 可迭代对象 [if 条件]}

```python
my_dict={f'name_{i}':i*10 for i in range(5)}
print(my_dict)
# {'name_0': 0, 'name_1': 10, 'name_2': 20, 'name_3': 30, 'name_4': 40}
```

## 文件操作

### file对象

一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。

以下是和file对象相关的所有属性的列表：

| 属性           | 描述                                                         |
| :------------- | :----------------------------------------------------------- |
| file.closed    | 返回true如果文件已被关闭，否则返回false。                    |
| file.mode      | 返回被打开文件的访问模式。                                   |
| file.name      | 返回文件的名称。                                             |
| file.softspace | 如果用print输出后，必须跟一个空格符，则返回false。否则返回true。 |

### file 对象内置函数

file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

| 序号 | 方法及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [file.close()](https://www.runoob.com/python/file-close.html)关闭文件。关闭后文件不能再进行读写操作。 |
| 2    | [file.flush()](https://www.runoob.com/python/file-flush.html)刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。 |
| 3    | [file.fileno()](https://www.runoob.com/python/file-fileno.html)返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。 |
| 4    | [file.isatty()](https://www.runoob.com/python/file-isatty.html)如果文件连接到一个终端设备返回 True，否则返回 False。 |
| 5    | [file.next()](https://www.runoob.com/python/file-next.html)返回文件下一行。 |
| 6    | [file.read([size\])](https://www.runoob.com/python/python-file-read.html)从文件读取指定的字节数，如果未给定或为负则读取所有。 |
| 7    | [file.readline([size\])](https://www.runoob.com/python/file-readline.html)读取整行，包括 "\n" 字符。**一次读取一行** |
| 8    | [file.readlines([sizeint\])](https://www.runoob.com/python/file-readlines.html)读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。**一次读取所有行** |
| 9    | [file.seek(offset[, whence\])](https://www.runoob.com/python/file-seek.html)设置文件当前位置 |
| 10   | [file.tell()](https://www.runoob.com/python/file-tell.html)返回文件当前位置。 |
| 11   | [file.truncate([size\])](https://www.runoob.com/python/file-truncate.html)截取文件，截取的字节通过size指定，默认为当前文件位置。 |
| 12   | [file.write(str)](https://www.runoob.com/python/python-file-write.html)将字符串写入文件，返回的是写入的字符长度。 |
| 13   | [file.writelines(sequence)](https://www.runoob.com/python/file-writelines.html)向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。 |

### 打开

使用open函数实现打开存在的文件或创建一个文件

```python
open(name,mode)
```

#### 文件打开模式

带b :二进制操作文件；带+：可读可写

r：只读打开，文件不存在报错，所有带r的操作同样，文件不存在报错

| 模式   | 描述                                                         |
| :----- | :----------------------------------------------------------- |
| t      | 文本模式 (默认)。                                            |
| x      | 写模式，新建一个文件，如果该文件已存在则会报错。             |
| b      | 二进制模式。                                                 |
| +      | 打开一个文件进行更新(可读可写)。                             |
| U      | 通用换行模式（不推荐）。                                     |
| **r**  | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb     | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 |
| **r+** | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+    | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。 |
| **w**  | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb     | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| **w+** | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除（**打开文件时已经删除原有内容**）。如果该文件不存在，创建新文件。 |
| wb+    | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| a      | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab     | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+     | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+    | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

### 关闭

`close()`：File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件

### 读

`read()`：方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

```python
fileObject.read([count])
```

### 写

`write()`：方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。

write()方法不会在字符串的结尾添加换行符('\n')：

语法：

```python
fileObject.write(string)
```

`readlines([sizeint])`：读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。会去读换行符

```python
file = open('test.text', 'r')
content = file.readlines()
print(content)
file.close()
#['明天要上班了明天要上班了\n', 'aaaa\n', 'bbbb\n', 'cccc\n', 'dddd']
```



### 文件定位

`tell()`：方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头多少字节之后。

`seek(offset，[whence])`：修改文件指针位置;

offset -- 开始的偏移量，也就是代表需要移动偏移的字节数

whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

## 文件夹操作

python通过os模块进行文件夹操作,需要导入os模块

```python
import os
```

操作方式os.函数名

### 重命名

rename（）方法需要两个参数，当前的文件名和新文件名。

```python
os.rename(current_file_name, new_file_name)
```

### remove()方法

remove()方法删除文件，需要提供要删除的文件名作为参数

```python
os.remove(file_name)
```

### 创建文件夹

mkdir()

可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。

语法：

```python
os.mkdir("newdir")
```

### 删除文件夹

rmdir()方法删除目录，目录名称以参数传递。

在删除这个目录之前，它的所有内容应该先被清除。

```python
os.rmdir('dirname')
```

### 目录操作

`getcwd()`方法显示当前的工作目录。

语法：

```python
os.getcwd()
```

chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。

将文件夹操作的目录修改

语法：

```python
os.chdir("newdir")
```

例子：

下例将进入"/home/newdir"目录。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 将当前目录改为"/home/newdir"
os.chdir("/home/newdir")
```

os.listdir(path)：方法用于返回指定的文件夹包含的文件或文件夹的名字的列表

```python
os.listdir(path)
path -- 需要列出的目录路径
```

## 类，对象

类：抽象概念

类的定义：

class 类名():

  类内部逻辑

定义类中的方法时必须要有self入参，self指调用该函数的对象（实例化的对象）

```python
class Washer():
    def wash(self):
        print("洗衣服")


w=Washer()
print(w)
w.wash()
```

### 访问类中属性

类中的方法要访问类的属性需要使用self.属性

```python
class student():
    '学生'
    name=""
    age=int()
    def getStudent(self):
        print(f'姓名{self.name}，年龄{self.age}')


student=student()
print(student.name)
student.name='Alice'
student.age=18
print(student.name)
student.getStudent()
```

### 魔法方法

python中定义  `_方法名_()`的方法为魔法方法，具有特殊功能的函数

#### `_init()_`

对象实例化时会先执行的方法；python会自动给init方法传self参数，所以定义init方法至少要有一个self入参

init方法只能有一个

```python

class student():
    '学生'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getStudent(self):
        print(f'姓名{self.name}，年龄{self.age}')


student=student("Alice",18)
student.getStudent()
```

#### `_str_()`

python直接输出时，输出内存地址，（类似java中的toString方法，默认打印内存地址），通过`_str_()`方法自定义返回的内容，类型java重写toString方法

```python
class student():
    '学生'

    def __init__(self, name, age):
        # 学生属性
        self.name = name
        self.age = age

    def __str__(self):
        return(f'姓名{self.name}，年龄{self.age}')


student2 = student("Tom", 19)
print(student2)
#姓名Tom，年龄19
```

#### `__del__()`

对象销毁时执行的方法

#### `__dict__`

字典形式返回类或者实例对象的属性以及方法

```python
prentice = Prentice()
print(prentice.__dict__)
#实例对象返回实例属性和对应值的字典（__init__方法中的属性）
{'m': '[独创的配方]'}
#类对象返回类内部所有属性和方法构成的字典（值为地址）
{'__module__': '__main__', '__init__': <function Prentice.__init__ at 0x000002853658AB88>, 'make_cake': <function Prentice.make_cake at 0x000002853658AC18>, 'make_school_cake': <function Prentice.make_school_cake at 0x000002853658ACA8>, 'make_master_cake': <function Prentice.make_master_cake at 0x000002853658AD38>, '__doc__': None}
```



#### 内置类属性

- `__dict__ `: 类的属性（包含一个字典，由类的数据属性组成）
- `__doc__` :类的文档字符串
- `__name__`: 类名
- `__module__`: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
- `__bases__` : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

### 继承

不由任意内置类型派生出的类称为经典类

```python
class 类名:
      代码
```

新式类

```python
class 类名([object]):
      代码
```

```python
class student():
    '学生'

    def __init__(self, name, age):
        # 学生属性
        self.name = name
        self.age = age

    def __str__(self):
        return(f'姓名{self.name}，年龄{self.age}')


class stu(student):
    pass

#stu继承student，拥有student的所有属性和方法
stu=stu("Alice",18)
print(stu)

# 输出姓名Alice，年龄18
```

多继承

class stu(父类1，父类2，...)；多继承时，父类有相同的属性和方法，默认使用第一个父类的属性和方法

- issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(子类class,父类class)
- isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是Class的某个子类的实例对象则返回true。

查看继承关系

```python
print(student.__mro__)
print(stu.__mro__)
#输出
(<class '__main__.student'>, <class 'object'>)
(<class '__main__.stu'>, <class '__main__.student'>, <class 'object'>)
```

#### 重写父类方法

子类重写父类方法时会使用子类的方法而不是用父类方法

```python
class Master():
    def __init__(self):
        self.m="[师傅的配方]"

    def make_cake(self):
        print(f'使用{self.m}制作')


class School():
    def __init__(self):
         self.m="[学校的配方]"

    def make_cake(self):
        print(f'使用{self.m}制作')

class Prentice(School,Master):
    def __init__(self):
         self.m="[独创的配方]"

    def  make_cake(self):
        # 重写父类的同名方法,调用时会使用子类的方法
         print(f'使用{self.m}制作')
    

prentice=Prentice()
prentice.make_cake()
#使用[独创的配方]制作
```

#### 子类调用父类方法

若要子类使用父类的同名方法，类名.方法 实现需要在子类中定义新的方法，在放法中调用父类的方法

```python
class Master():
    def __init__(self):
        self.m = "[师傅的配方]"

    def make_cake(self):
        print(f'使用{self.m}制作')


class School():
    def __init__(self):
        self.m = "[学校的配方]"

    def make_cake(self):
        print(f'使用{self.m}制作')


class Prentice(School, Master):
    def __init__(self):
        self.m = "[独创的配方]"

    def make_cake(self):
        #没有
        self.__init__()
        print(f'使用{self.m}制作')

    def make_master_cake(self):
        #子类调用父类方法时，会初始化一个父类
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


prentice = Prentice()    #实例化子类会调用子类的__init__方法，给属性m赋值
prentice.make_master_cake() #为了调用父类方法，且使用父类中的属性值，需要初始化父类的__init__方法，此时m中为父类的值，所以为了保证再次调用子类方法时使用的是子类的值，需要make_cake方法中重新初始化子类
prentice.make_school_cake()
prentice.make_cake()
#输出
使用[师傅的配方]制作
使用[学校的配方]制作
使用[独创的配方]制作
```

super（）

```python
class Master():
    def __init__(self):
        self.m = "[师傅的配方]"
        print('Master初始化')

    def make_cake(self):
        print(f'使用{self.m}制作')


class School(Master):
    def __init__(self):
        self.m = "[学校的配方]"
        print('School初始化')

    def make_cake(self):
        print(f'使用{self.m}制作')

    def make_master_cake(self):
        #调用父类方法
        # 有参写法
        # super(School, self).__init__()
        # super(School, self).__init__()
        #无参写法
        super().__init__()
        super().make_cake()


class Prentice(School):
    def __init__(self):
        self.m = "[独创的配方]"
        print('子类初始化')

    def make_cake(self):
        self.__init__()
        print(f'使用{self.m}制作')

    def make_school_cake(self):
        #调用父类方法
        # 有参写法
        super(Prentice, self).__init__()
        super(Prentice, self).make_cake()
        #无参写法
        super().__init__()
        super().make_cake()

    def make_master_cake(self):
        #调用父类方法
        # 有参写法
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_master_cake()
        #无参写法
        super().__init__()
        super().make_master_cake()
    

prentice = Prentice()
prentice.make_master_cake()
prentice.make_school_cake()
prentice.make_cake()
```

### 私有

子类无法继承父类的私有属性和方法 

类的属性或者方法名前有两个下划线时，该属性或者方法为私有,子类无法继承

### 单下划线、双下划线、头尾双下划线说明：

- **`__foo__`**: 定义的是特殊方法，一般是系统定义名字 ，类似 **`__init__()`** 之类的。
- **`_foo`**: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 **from module import \***
- **`__foo`**: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

### 多态

- 父类提供公共方法
- 子类继承父类，并重写父类的公共方法
- 调用者通过接受不同的子类入参从而执行不同的具体方法

```python
class Dog():
    def work(self):
        pass


class ArmyDog(Dog):
    def work(self):
        print('ArmyDog')


class DrugDog(Dog):
    def work(self):
        print('DrugDog')


class Person():
    def work_with_Dog(self, dog):  # 根据入参对象的不同，使用不同的方法
        dog.work()


p = Person()
dog = DrugDog()
p.work_with_Dog(dog)
#DrugDog
```

### 类属性和实例属性

类属性：类拥有的属性，被类的所有实例化对象共有

实例属性：类实例化之后产生实例对象的属性

类属性的修改：类名.属性名=值；类属性修改之后所有类的实例化中的该属性也会修改

```python
class Dog():

    # 类属性
    tooth = 10

    def work(self):
        pass
        
        
dog1 = Dog()
dog2 = Dog()
print(dog1.tooth,dog2.tooth)
Dog.tooth=20
print(dog1.tooth,dog2.tooth)
#输出
10 10
20 20
```

实例属性修改：类的实例化对象.属性=值

```python
class Dog():

    # 类属性
    tooth = 10

    def work(self):
        pass
        
        
dog1 = Dog()
dog2 = Dog()
print(dog1.tooth,dog2.tooth)
dog2.tooth=30
print(dog1.tooth,dog2.tooth)
#输出
10 10
10 30
```

### 静态方法、类方法

#### 类方法

类方法：@classmethod标识的方法为类方法；第一个方法必须是类对象，入参名称一般为`cls`

类方法一般和类属性配合使用，在需要操作私有属性等时定义类方法

```python
class Dog():

    # 私有类属性
    __tooth = 10

    @classmethod
    def get_Tooth(cls):
        return cls.__tooth


dog=Dog()
print(dog.get_Tooth())
#输出
10
```

#### 静态方法

静态方法：通过@staticmethod修饰，静态方法不需要传递类对象cls也不需要传递实例对象self

静态方法可以通过**实例对象**，**类对象**访问

当方法中既不需要使用实例对象，也不需要使用类对象时，定义静态方法

取消不需要的入参，减少不必要的内存

```python
class Dog():

    @staticmethod
    def get_info():
        print('这是静态方法')


dog=Dog()
dog.get_info()
Dog.get_info()
#输出
这是静态方法
这是静态方法
```

### 序列和映射协议

协议通常指的是规范行为的规则  

序列和映射基本上是元素（ item）的集合，要实现它们的基本行为（协议），不可变对象需
要实现2个方法，而可变对象需要实现4个  

`__len__(self)`：这个方法应返回集合包含的项数，对序列来说为元素个数，对映射来说
为键值对数。如果`__len__`返回零（且没有实现覆盖这种行为的`__nonzero__`），对象在布尔上下文中将被视为假（就像空的列表、元组、字符串和字典一样）。
`__getitem__(self, key)`：这个方法应返回与指定键相关联的值。对序列来说，键应该是0~n -1的整数（也可以是负数，这将在后面说明），其中n为序列的长度。对映射来说，
键可以是任何类型。
`__setitem__(self, key, value)`：这个方法应以与键相关联的方式存储值，以便以后能够使用`__getitem__`来获取。当然，仅当对象可变时才需要实现这个方法。
` __delitem__(self, key)`：这个方法在对对象的组成部分使用`__del__语`句时被调用，应删除与key相关联的值。同样，仅当对象可变（且允许其项被删除）时，才需要实现这个方法。  

```python
def check_index(key):
    """指定的键是否是可接受的索引？键必须是非负整数，才是可接受的。如果不是整数，
    将引发TypeError异常；如果是负数，将引发Index
    Error异常（因为这个序列的长度是无穷的）"""
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """初始化序列
        changed：一个字典，包含用户修改的信息"""
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """从序列中获取元素"""
        check_index(key)
        try:
            return self.changed[key]
        except:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """修改值"""
        check_index(key)
        self.changed[key] = value
```

#### 自定义属性property

property的四个参数get set del doc

property其实并不是函数，而是一个类。它的实例包含一些魔法方法，而所有的魔法都是由这些方法完成的。这些魔法方法为`__get__`、` __set__`和`__delete__`，它们一道定义了所谓的描述符协议。 只要对象实现了这些方法中的任何一个，它就是一个描述符。描述符的独特之处在于其访问方式。例如，读取属性（具体来说，是在实例中访问类中定义的属性时，如果它关联的是一个实现了`__get__`的对象，将不会返回这个对象，而是用方法`__get__`并将其结果返回。   

```python
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)
    
r = Rectangle()
r.set_size((12, 4))
print(r.size)
#输出(12, 4)
```



## 异常

### 语法：

```python
try:
	代码体
except 异常名称:
	捕获异常后执行代码体
	
	
try:
    print(num)
except NameError:
    print("发生异常NameError")
    
#捕获多个异常,获取异常描述
try:
	代码体
except (异常名称1,异常名称2,...) as result: 
	捕获异常后执行代码体
    
#捕获所有异常
try:
	代码体
except Exception as result: 
	捕获异常后执行代码体
```

try except捕获异常一般只放一行代码捕获异常

Exception：是所有异常的父类

### 异常的else

```python
try:
	代码体
except Exception as result: 
	捕获异常后执行代码体
else:
    没有异常时执行的代码
```

```python
try:
	print(1)
except Exception as result: 
	print(f'发生异常NameError{result}')
else:
    print("没有异常发生")
    
#输出
1
没有异常发生
```

### finally

无论是否异常的都会执行的代码

```python
try:
	代码体
except Exception as result: 
	捕获异常后执行代码体
else:
    没有异常时执行的代码
finally:
    代码体
```

### 自定义异常

python中抛出自定义异常的语法为`raise` 异常类对象

```python
#自定义异常继承Exception类
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        #设置抛出异常的描述信息，一定要有
        return f"输入的字符串长度为{self.length}，小于{self.min_len}"


def main():
    try:
        con = input("输入密码：")
        if len(con) < 5:
            raise ShortInputError(len(con), 5)   #通过raise抛出自定义异常
    except Exception as e:
        print(f"发生异常{e}")
    else:
        print("登陆成功")


main()
```

### 异常抛出

发生异常的地方通过raise 异常将异常抛出，发生异常的地方不处理，在调用的地方处理

```python
def func():
    try:
        return 1 / 0
        print('无异常')
    except Exception as e:
        print('异常发生行')
        raise e


try:
    func()
except:
    print('调用的方法发生异常')

```

### 警告warings

使用模块warnings中的函数war 函数可以指出可能到异常而不是等异常发生；通常警告只打印一条日志

## 包和模块

### 模块（moudle）

python的模块是一个python文件，包含了对象的定义以及其他python语句；

模块可以定义函数，类，变量，可执行代码

#### 导入模块

- import 模块名1， 模块名2，...
- import 模块名 as 别名
- from 模块名 import 功能名1，功能名2，...
- from 模块名 import *

```python
#导入math模块，并使用sqrt函数开平方
import math
print(math.sqrt(9))
#输出3.0
import math as m 
print(m.sqrt(9))
#输出3.0
from math import sqrt
print(sqrt(9))
#输出3.0
from math import *
print(sqrt(9))
#输出3.0
```

#### 别名

import 模块名 as 别名

from  模块名 import 功能名 as 别名

```python
import math as m
print(m.sqrt(10))

from math import sqrt as sq
print(sq(9))
```



#### 定义模块

每个python文件都可以作为一个模块，模块名字就是文件名字。要求自定义模块名必须符合命名规则

`__name__`系统变量：模块标识符，在当前文件中值为`__main__`，若是被其他模块引用时，值为引用的那个模块名称

```python
#测试信息,为了防止每次导入模块都会调用到测试方法
#其他地方导入模块，不符合条件时不执行
if __name__ =='__main__':
    print('这是测试',testA(4,5))
```

#### 模块定位顺序

当导入一个模块时，python解释器对模块的搜索顺序是：

1、当前目录

2、不过当前目录没有，搜索在shell变量PYTHONPATH下的每一个目录

3、都没有则搜索默认目录，不同系统默认路径不同

模块搜索路径存储在system模块的sys.path变量中，变量包含当前目录、PYTHONPATH、默认目录

注意：

- 自定义模块不要和已有模块重名，只会导入路径最近的模块
- 使用 from方式导入模块功能时，功能名字重复，则会调用最后一次定义（导入的代码行号最大的哪行锁引用的）的或者导入的功能

```python

from time import sleep

#定义一个函数
def sleep(a):
    print(f"自定义sleep,{a}")

#调用sleep函数，会调用自定义的函数，而不是从time模块中导入的
sleep(2)
#输出
自定义sleep,2
```

#### 重新导入

importlib  模块的relaod函数可以在运行时重新导入，入参数是模块

#### `__all__`

当模块有`__all__`变量时，使用`from xxx import *`导入模块全部功能时，只能导入`__all__`这个数组中有的功能

注意，`__all__`变量数组中的元素必须是模块中有的方法，变量，否则会报错

```python
#指定模块以及功能名称导入时不会受影响
from my_moudle2 import testA,testB
testA()
testB()
```

模块定义

```python
__all__=['testA','b','这是__all__']

def testA():
    print('这是testA')

def testB():
    print('这是testB')
```

导入模块

```python
from my_moudle2 import *
testA()
#这是testA
testB()
NameError: name 'testB' is not defined
```

### 包

将有联系的模块放在同一个文件夹下，并在文件夹下创建一个名字是`__init__.py`的文件，那么该文件夹即为包

#### 导入包

import 包名  方式导入包时，会调用`__init__.py`文件中的方法；

```python
#__init__.py中定义
print("导入my_pakage1模块")
#调用文件
import my_pakage1
#引入包时会输出；导入my_pakage1模块
```

import 包名.模块名

包名.模块名.目标

```python
#定义包下模块
def method1():
    print("moudle1中的method1")
#引用包
import my_pakage1.moudle1

my_pakage1.moudle1.method1()
#输出：moudle1中的method1
```

from 包名 import * 方式导入包；

必须在`__init__.py`文件中设置`__all__`列表，控制允许导入的模块

```python
#__init__.py设置__all__变量
__all__ = ['moudle1']

#moudle1
def method1():
    print("moudle1中的method1")

#moudle2
def method2():
    print("moudle2中的method2")


#引用
from my_pakage1 import *
moudle1.method1()
#输出moudle1中的method1
moudle2.method2()
#无法导入
```

## 函数编程

### 高阶函数

接收其它函数作为入参的函数为高阶函数

## 迭代器、生成器

### 迭代器

实现`__iter__`的类可以作为一个迭代器。方法`__iter__`返回一个迭代器，它是包含方法`__next__`的对象，而调用这个方法时可不提供任何参数。当你调用方法`__next__`时，迭代器应返回其下一个值。如果迭代器没有可供返回的值，应引发StopIteration异常。 

迭代器的类应该包含 `__iter__`和`__next__`方法；`__next__`方法中定义迭代规则；

```python
#求斐波拉切数的迭代器
class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


f = Fibs()
for i in f:
    if i > 100:
        print(i)
        break
```

### 生成器

包含yield语句的函数都被称为生成器 ，调用时返回一个迭代器

生成器不是使用return返回一个值，而是可以生成多个值，每次一个。每次使用yield生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒。被重新唤醒后，函数将从停止的地方开始继续执行  

#### 递归式生成器

```python
#将列表的所有元素展开
def flatten(nested):
    try:
        try:
            nested + ""
        except TypeError:
            pass
        else:
            TypeError
        for sub_List in nested:
            for e in flatten(sub_List):
                yield e
    except TypeError:
        yield nested


for i in flatten(nested):
    print(i, end="-")

```

## 时间

### time

time模块操作时间；获取当前时间、操作时间和日期、从字符串中读取日期、将日期格式化为字符串的函数 。日期可表示为实数 ，也可表示为包含9个整数的元组  

日期元祖字段含义：

| 索引 | 字段含义 | 取值范围        |
| ---- | -------- | --------------- |
| 0    | 年       | 如2021          |
| 1    | 月       | 1~12            |
| 2    | 日       | 1~31            |
| 3    | 时       | 0~23            |
| 4    | 分       | 0~59            |
| 5    | 秒       | 0~61            |
| 6    | 日期     | 0~6 0表示星期一 |
| 7    | 儒略日   | 1~366           |
| 8    | 夏令时   | 0、1、-1        |

函数：

```python
t1 = (2021, 10, 30, 20, 47, 30, 6, 1, 0)
time.asctime(t1)#将时间元组转换为字符串
time.mktime(t1)#将时间元组转换为当地时间,返回秒数
sleep(5)#解释器暂停指定秒数
time.time()#获取当前时间，秒数
time.localtime(秒数)#把秒转化为时间字符串（所在地）
```

### datetime

datetime模块提供了时间和日期的算术计算

### timeit 

timeit 模块计算代码运行时间



## Shelve和json

Shelve是一个文件持久化保存方法，将对象二进制方式保存到文件中

### json

操作字json

| json.dumps（dump） | 将 Python 对象编码成 JSON 字符串         |
| ------------------ | ---------------------------------------- |
| json.loads（load） | 将已编码的 JSON 字符串解码为 Python 对象 |

```python
json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
```

sort_keys：根据key排序

indent：非负的整数，表示打印的缩进

dumps和dump区别在于，dump函数除了要转化的对象还需要一个文件操作对象fp用于进行文件操作

loads和load区别类似

```python
#默认输出
print(json.dumps(data))
[{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]
# key排序
print(json.dumps(data, sort_keys=True))
[{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]
#格式化缩进
print(json.dumps(data, indent=4))
[
    {
        "a": 1,
        "c": 3,
        "b": 2,
        "e": 5,
        "d": 4
    }
]
```

转化为json对象loads

```python
json.loads(s, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```



## 正则表达式

re模块提供了正则表达式的支持

## 网络编程

socket模块用于处理请求，提供了两个方法： send和recv（表示receive）。要发送数据，可调用方法send并提供一个字符串；要接收数据，可调用recv并指定最多接收多少个字节的数据。如果不
确定该指定什么数字， 1024是个不错的选择  

```python
发送数据
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()
    
#接收数据

import  socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print(s.recv(1024))
```

