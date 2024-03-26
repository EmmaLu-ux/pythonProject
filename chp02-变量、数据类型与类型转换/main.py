import math

print('----------变量与常量----------')
UNIT = '3.65'
price = 10.5
weight = 7.5
money = price * weight
print('常量为：', UNIT)
print('付款金额为 %.2f 元' % money)

print('----------数据类型判断----------')
a = '23434f'
print(type(a))
print(isinstance(a, int))
print(isinstance(a, str))

print('----------整数类型----------')
# 整数类型
num1 = 7
num2 = input('请输入一个整数：')
print('默认整数为：', num1)
print('你输入的整数为：', num2)
print('相加的结果为：', num1 + int(num2))

print('----------浮点类型----------')
# 浮点类型
num3 = 0.548878888
num4 = 0.1
print('num3 + num4 =', num3 + num4)
num5 = 0.1
num6 = 0.2
print('num5 + num6', num5 + num6)
# 四舍五入
num31 = round(num3, 3)
print('num3四舍五入后为: ', num31)

# 向上取整ceil
num7 = math.ceil(num3 + num4)
print('向上取整的结果为：', num7)
# 向下取整floor
num8 = math.floor(num3 + num4)
print('向下取整的结果为：', num8)

print('----------布尔类型----------')
# 布尔类型
a = True
b = False
print('布尔类型： ', a, b)

print('----------字符串类型----------')
# 字符串
str1 = 'month'
str2 = '''www
weregstrfh
65
gg'''
str3 = "I'm a rabbit"
str4 = '123\'\"ghjk'
print('str1:', str1)
print('str2:', str2)
print('str3:', str3)
print('str4: ', str4)

# 字符串拼接
print(str3 + str4)
print(str1 + str2)
# 字符串乘法
print(str1 * 3)
# 字符串索引，从0开始
str5 = 'today 44 is a good day'
print('str5:', str5)
print('str5的第三个字符为：', str5[2])
print(str5[-1])
# 切片。包头不包尾
# 变量名[起始索引:结束索引+1:步数]
# 起始索引默认为0，可以省略不写
# 结束索引默认为-1，可以省略不写
print(str5[0:4])
str6 = '123456789'
print(str6[0:9:2])  # 隔两个取一个
print(str6[:9:2])
print(str6[::2])
print(str6[1:9:2])
# 字符串反转
print(str6[-1:-10:-1])
print(str6[::-1])

print('----------数据类型转换----------')
# str -> int
t1 = '90'
print(t1, int(t1))
# float => int
t3 = 5.782
print(t3, int(t3))
# bool -> int
t4 = True
print(t4, int(t4))

# str -> float
print(t1, float(t1))
# int -> float
print(num1, float(num1))
# bool -> float
print(t4, float(t4))

# str -> bool
print(str5, bool(str5))
t5 = ''
print(t5, bool(t5))
# int -> bool
print(1, bool(1))
print(0, bool(0))
# float -> bool
print(2.121, bool(2.121))
print(0.0, bool(0.0))

# int -> str
print(3, str(3), type(str(3)))
# bool -> str
print(True, str(True), type(str(True)))
# float -> str
print(4.221, str(4.221), type(str(4.221)))

print('----------进制转换----------')
# int(x, 基数)，基数指的是进制，比如二进制的2， 十进制的10， 八进制的8等等
print(int('10', 2))
