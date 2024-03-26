print('-' * 30, '算术运算符', '-' * 30)
# 算术运算符：+ - * / // % **
a = 10
b = 2
c = a + b
d = a - b
e = a * b
f = a / b
g = a // b
h = a % b
i = a ** 3
print(c, d, e, f, g, h, i)

print('-' * 30, '赋值运算符', '-' * 30)
# 赋值运算符: = += -= *= /= //= %= **=

print('-' * 30, '比较运算符', '-' * 30)
# 比较运算符：== != > < >= <=
print(ord('a'))  # 获取a的ASCII值

print('-' * 30, '逻辑运算符', '-' * 30)
# 逻辑运算符：and or not
# and
print(True and False)
print(True and True)
print(True and False and True)
print(1 == 1 and True and 2 < 3)
# and前后都不是True活着False，则会进入短路运算， 否则就不会
print('hello' and 'hi')  # hello为true，进入短路运算，返回后面的hi
print('' and 'hi')  # ''为false
print(False and 'hi')
print(0 and 1)  # 0为false，那么整个式子肯定都为false了，则进入短路运算，直接返回0
print('-' * 45)
# or
print(True or False)
print(False or False or True)
print(1 or 0)
print(2024 or 2025 or 0)
print(0 or '' or 888)
print('-' * 45)
# not
print(not True)
print(not 1)
print(not 'hello')
print(not '')

# 优先级:  一元运算符 > 二元运算符
# 优先级：not > and > or

print('-' * 30, '位运算符', '-' * 30)
# 位运算符：& | ^ ~ << >>
# &: 按位与（相同则为1，不同则为0）
'''
5: 101
7: 111
----
5: 101
'''
print(5 & 7)
# |: 按位或（相同则为0，不同则为1）
'''
3: 011
4: 100
----
7: 111
'''
print(3 | 4)
# ^: 按位异或（相同则为0， 不同则为1）
'''
2: 010
4: 100
----
6: 110
'''
print(2 ^ 4)
# ~：按位取反，0表示正数，1表示负数
'''
1: 01
---
   10（补码）
   110（10表示2）
'''
print(~1)

print('-' * 30, '成员运算符', '-' * 30)
# 成员运算符：in 和 not in
print('12' in '123')
print('hi' not in 'hello')

print('-' * 30, '成员运算符', '-' * 30)
# 身份运算符：is 和is not
a = 1
b = 2
print(a is b)
print(a is not b)

print('-' * 30, '运算符优先级', '-' * 30)
# ** > (~+-) > (* / % //) > (+ -) > (<< >>) > & > ` > (> < >= <=) > (== !=) > (= += -= *= /= //= %= **=) > (is 和 is not) > (in 和 not in) > (not or and)
