# 输入您的等级，输出对应的成绩范围
#    A ：  >= 90
#    B ：70 ~ 90
#    C : 60 ~ 70
#    D :  < 60
from unittest import case

# match-case : Python3.10及以上版本 switch-case
# 了解
n = input("请输入等级(A/B/C/D)")
match n:
    case 'A':
        print("A")
    case 'B':
        print("B")
    case 'C':
        print("C")
    case 'D':
        print("D")
