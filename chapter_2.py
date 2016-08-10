#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
'''
2-1:
question: 变量，print和字符串格式化运算符。启动交互式解释器。给一些变量赋值
(并通过输入变量名字和它们的值。在用print语句做同样的事。这二者有何区别？尝试实用字符串格式运算符%)
answer : 本题自己练练哦。
'''

'''
2-2:
P程序输出，阅读下面的python脚本
'''
result = 1+2*4
'''
question a: 你认为这段脚本是用来做什么的？
b: 你认为这段脚本会输出什么？
c:输入以上代码，并保存为脚本，然后运行它。
answer a: 这段脚本是一个简单的数学运算
b: 输出结果为 9
c: 保存为脚本运行时需要用print 打印出结果，不然没有输出。
d: 改进见下面的代码
'''


def math_operate(numa, numb, numc):
	value = (numa+numb)*numc
	return value

'''
2-3:
question:启用交互解释器，使用python对两个数进行数学运算
answer: 自己动手试试吧
'''
'''
2-4:
question:实用raw_input()函数得到用户输入
'''


def get_user_input():
	print u'请输入：'
	value = raw_input()
	v_type = type(value)
	if v_type == str:
		pass
	return value

'''
2-5 循环和数字
分别用while和for循环创建一个循环
(a) 输出0到10.
(b)用range输出0到10
'''

loop_w_result = []
loop_w_i = -1
while len(loop_w_result) < 11:
	loop_w_i += 1
	loop_w_result.append(loop_w_i)

loop_for_result = []
for loop_for_i in range(11):
	loop_for_result.append(loop_for_i)

'''
2-6 判断一个数是正数，负数，或者0
'''


def judge_num(args):
	if type(args) != int and type(args) != float:
		print(u'请输入一个数字：')
	elif args > 0:
		print(str(args) + u"是一个正数" )
	elif args < 0:
		print(str(args) + u'是一个负数')
	else:
		print(str(args) + u'是零')

'''
2-7 从用户那里得到一个字符串输入，然后逐字显示该字符串
'''
# getchar = get_user_input()
# for i in getchar:
# 	print(i)

'''
2-8 循环和运算符，创建一个包含五个固定数值的列表和元组，输出他们的和
'''
char_list = [2, 3, 4, 6, 10]
charsum = 0
for i in char_list:
	charsum += i

charavg = float(charsum)/len(char_list)
print(charavg)


'''
2-10 使用raw_input()函数来提示用户输入一个1-100之间的数，如果满足条件
退出，否则提示错误信息，让用户继续输入
'''


def check_user_input():
	print u'请输入：'
	value = float(raw_input())
	if value >= 1 and value <= 100:
		print(value)
		print(u'恭喜！输入正确')
	else:
		check_user_input()
	return value

'''
2-11 带文本菜单的程序,写一个带文本菜单的程序，菜单项如下（1）取五个数的和，（2）取
五个数的平均值，X退出
'''


'''
2.x 定义一个函数，比较数字的大小
'''


def compare_num(*args, **kwargs):
	pass









