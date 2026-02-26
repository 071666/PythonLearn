# 1. print输出,打印内容, 在控制台输出内容
print(100)
print(200, 300)

# sep=" " 分隔符,默认是空格, 打印多个内容时的连接符号
# 可以查看Python函数源码: ctrl + 鼠标左键
print(400, 500, 600)

# end="\n" 结束符,默认是\n表示换行符
#     \n : 表示换行
#     \t : 表示制表符
print(700, 800, 900, end="\t")
print(1000, end="---")

# 练习: 打印以下内容,使用sep将唱,跳,rap连接
#     "唱+跳+rap"
print("\n唱", "跳", "rap", sep="+")

# 2.输入: input()
#  方便我们测试代码时自定义输入值
# Python中比较常见的3种类型: int整数, float小数, str字符串 "hello"
# name = input("请输入您的姓名：")
# print("您的名字是：" + name)

# 特点:
#    1.会让程序暂停,等待用户输入内容,且按enter键
#    2.input会得到一个str字符串类型,如果输入的是数字,则需要使用int或float来转换
# 快速添加或取消注释: ctrl + /
# age = input("请输入您的年纪：")
# print(age + 5)
# print(type(age))
# print(type(int(age)))
# print(int(age) + 20)
# 示例:
#    输入1个数,然后将这个数 乘以 3.14
# num = int(input("请输入数字："))
# print(num * 3.14)

# 练习:
# 1、输入1个名字, 用一个变量接收该名字，然后输出该变量的值
# 2、输入任意两个数字,计算他们的和
# name = input("输入1个名字：")
# print(name)
num1 = input("输入num1：")
num2 = input("输入num2：")
print(num1 + num2)
