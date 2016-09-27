#coding=utf-8
print 'hello world.'
print '中文字符.'

#单行注释
print ('hello world.')
print ('中文字符.')

'''
多行注释
'''

#一行多句;
import sys; name = 'sf'; sys.stdout.write(name + '\n')

#代码组
if True:
    print 'true'
elif False:
    print 'false'
else:
    print 'error'

#变量
num = 1
fnum = 1.1
boo = True
str = 'sf'
print num
print fnum
print boo
print str

#多个变量
a = b = 1
c, d = 2, 'sf'
print a
print b
print c
print d

'''
python标准数据类型
Numbers: 数字,存储数值. int, long, float, complex
String: 字符串,存储一串字符.
List: 列表,存储集合.
Tuple: 元组,类数组，不能二次赋值.
Dictionary: 字典,存储对象.
'''
num = 1 #创建
del num #删除

str = 'ilovecode'
print str
print str[0]
print str[1:5]
print str[1:]
print str * 2
print str + 'ing'

list = [1, 'sf', 3]

tup = (1, 'sf', 3)

dic = {name: 'sf'}

#python任何非0非null的值为true，0和null为false
#python不支持switch语句

#按键交互
raw_input('\n\npress enter to exit.')