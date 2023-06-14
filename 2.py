#1
num = int(input("请输入一个正整数："))
checknum = int(input("请输入要判断的正整数："))
zlist = []
while True:
  if num <= 1:
    break
  tp = 2
  status = True
  while tp < num:
    if num % tp == 0:
      status = False
    tp += 1
  if status:
    zlist.append(num)
  num -= 1
if checknum in zlist:
  print(f"{checknum}是素数")
else:
  print(f"{checknum}不是素数")
#2
import sys

temp = {}
t = int(input('阶数：'))
for i in range(t, -1, -1):
  tt = int(input('请输入多项式的' + str(i) + '阶系数：'))
  if tt == 0:
    print('系数不为0')
    sys.exit()
  temp['第' + str(i) + '阶系数'] = tt
print(temp)

print("PLUS")
t = int(input('请输入总阶数：'))
tempdict1 = {}
for i in range(t, -1, -1):
  tt = int(input('请输入第一个多项式的' + str(i) + '阶系数：'))
  if tt == 0:
    print('系数不为0')
    sys.exit()
  tempdict1['第' + str(i) + '阶系数'] = tt

tempdict2 = {}
for i in range(t, -1, -1):
  tt = int(input('请输入第二个多项式的' + str(i) + '阶系数：'))
  if tt == 0:
    print('系数不为0')
    sys.exit()
  tempdict2['第' + str(i) + '阶系数'] = tt

sumdict = {}
for i in range(t, -1, -1):
  sumdict['第' + str(i) +
          '阶系数'] = tempdict1['第' + str(i) + '阶系数'] + tempdict2['第' + str(i) +
                                                               '阶系数']
print('第一个多项式：')
print(tempdict1)
print('第二个多项式：')
print(tempdict2)
print('sum：')
print(sumdict)

#3
infodict = {}
checkstatus = 0
while True:
  if checkstatus == 1:
    break
  key = input("输入名字：")
  value1 = input("20200322是否提交：")
  value2 = input("20200401是否提交：")
  infodict[key] = {"20200322": value1, "20200401": value2}
  checkstatus = int(input("是否继续输入，输入1表示退出输入："))
print(infodict)
