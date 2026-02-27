# Python算术运算符：
#    +  -  *  /  %  //（整除:向下取整）   **
a = 9
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(-a // b)  # -3 向下取整
print(a ** b)
# 科学计数法
c = 3.14 * 10 ** 5
print(c)
c = 3.14e5
print(c)
# 常见内存单位：
# 1bit = 0 或 1
# 1Byte = 8bit
# 1KB = 1024Byte
# 1MB = 1024KB
# 1GB = 1024MB
# 1TB = 1024GB
# 1PB = 1024TB
# 1EB = 1024PB
# ...
# 练习：从控制台输入一个三位数，取出个位、十位、百位
n = int(input("请输入一个三位数："))
single = n % 10
ten = int(((n - single) / 10) % 10)
hundred = int((n - ten * 10 - single) / 100)

print(single, ten, hundred)

# 简单实现
hundred = n // 100
ten = n // 10 % 10
single = n % 10

print(single, ten, hundred)