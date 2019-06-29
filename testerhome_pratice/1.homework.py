# -*- coding: utf-8 -*-

# 一、课后作业

# 1.利用pip, 安装第三方模块requests, 描述你用什么方法来确认安装是成功的。
# 安装：pip install requests
# 验证：import requests，可以识别

# 2.把2.918 转化为整形
print(int(2.918))

# 3.把10进制数 18 转化为2进制数
print(bin(18))

# 4.用java 替换字符串：”Python is popular” 里面的Python，并 把java 变换成JAVA
str = "Python is popular"
print(str.replace("Python", "java").replace("java", "JAVA"))

# 5.把列表 [1, 2, 3,4 5,6,7,8]里面的2, 4, 6,8 打印出来
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(list_1)):
    if i % 2 != 0:
        print(list_1[i])

# 6.创建一个字典，字典的key分别是name, sex, province , 修改原始province 的值 为新值”江苏”
dic_1 = {'name': u'stella', 'sex': u'女', 'provice': u'福建'}
dic_1['provice'] = u'江苏'
print(dic_1)

'''
# 7.Test_str=“Python was created in 1989, Python is using in AI, big data, IOT.”
按下列要求对上面文字做出处理。
(1)把上面文字中的所有大写转化为小写
(2)把这段话每个单词放到列表里面，不能包含空格。
(3)把列表最中间的一个单词打印出来。
'''
Test_str = "Python was created in 1989, Python is using in AI, big data, IOT."
print(Test_str.upper())
print(Test_str.replace(',', '').replace('.', '').replace(' ', ''))
list_2 = Test_str.replace(',', '').replace('.', '').split(' ')
print (list_2[int(len(list_2)/2)])

'''
# 8.List1=[“python”, 5,6, 8], list2=[“python”,”5”, 6, 8,10], 对list1和list2做出如下处理：
(1)把上面2个list的内容合并成一个
(2)利用set里面的方法，对合并后的list，去除重复元素。最后输出是还是list =“python”, 5,6, 8,”5”,10
'''
List1 = ["python", 5, 6, 8]
list2 = ["python", "5", 6, 8, 10]
List1.extend(list2)
print(set(List1))

# 9.实现一个函数，要求对一个列表里面所有数字求和，如果里面含有非数字的元素。直接跳过。
# 比如[1,2,3] 输出是5， 如果 是[1,2,4,”a”] 输出是7。 并在另外一个包（目录）里面调用这个函数


def sum_num(lst):
   sum = 0
   for i in lst:
       if type(i) in (int, float):
           sum += i
       else:
           print("%s非数字，跳过")%i
   print("列表数字和是%d")%sum


a = [1, 2, 4, "a"]
sum_num(a)


'''
# 10.实现一个不定长参数的函数def flexible(aa, *args, **kwargs):，
把传入的参数和值打印出来。比如传入参数是
flexible(aa, 2, 3, x = 4, y = 5, *[1, 2, 3], **{'a':1,'b': 2})
输出结果：(2, 3, 1, 2, 3)，{'a': 1, 'y': 5, 'b': 2, 'x': 4}
'''


def flexible(aa, *args, **kwargs):
    print(aa, args, kwargs)


flexible('aa', 2, 3, x = 4, y = 5, *[1, 2, 3], **{'a':1,'b': 2})

# 11.面试题：*args, **kwargs 有什么作用
# *args：传入无命名参数（无命名参数存储的是元组）
# **kwargs：传入不定长的命名参数（命名参数存储的是字典）
# 位置：从左至右：关键参数,默认参数,*args，**kwargs

















