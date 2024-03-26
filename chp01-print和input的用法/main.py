print('----------print用法----------')
year = 2024
month = 3
day = 26
week = '二'
weather = '多云'
temp = 21.3

print('hello')  # print
print(year, '年，我要减肥', sep="")  # sep：设置打印多个内容的分隔符
print(end="*")  # end: 设置print执行结束后的操作
print(end="\n")
print(year, '年，我要看10次电影')
print(end="\n")
print("今天是 %d 年 %02d 月 %02d 日，星期%s，天气%s，温度%.1f摄氏度" % (year, month, day, week, weather, temp))  # %02d: 表示显示两位的十进制数字

print('----------input用法----------')

inputV = input("请输入内容（结束后请回车）：")
print('你输入的内容为：', inputV)
print(type(inputV))  # 检查inputV的类型。注意：用户输入的内容均为字符串类型
age = input('请输入你的年龄:')
print('你的出生时间为：', year - int(age))