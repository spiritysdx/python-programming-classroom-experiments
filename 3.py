# 1
grade1 = {'刘达': 89, '王尔': 95, '李珊': 67, '陈思': 75}
grade2 = {'刘达': 75, '王尔': 79, '李珊': 79}
grade3 = {'李珊': 87, '陈思': 91, '张悟': 75}
grade4 = {'刘达': 89, '王尔': 86, '张悟': 99}
name_list = []
grades = [grade1, grade2, grade3, grade4]
for i in grades:
  for j in i:
    if j not in name_list:
      name_list.append(j)
scores = {}
for i in name_list:
  score = 0
  count = 0
  for j in grades:
    try:
      score = score + j[i]
      count += 1
    except:
      continue
  scores[i] = score / count
scores = sorted(scores.items(), key=lambda x: x[1], reverse=False)
print(scores)

# 2
for i in range(5, 1, -1):
  for j in range(1, i):
    print(" ", end="")
  for k in range(5):
    print("*", end="")
  print("\n")

# 3
i = 1
for j in range(7, 0, -1):
  print(f'第{j}天的桃子数为{i}个')
  i = 2 * (i + 1)

# 4
MonthDays_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MonthDays_leapy = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
twelfthMonth = [1, 3, 5, 7, 8, 10, 12]


def leap_year(year):
  if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
    return True
  else:
    return False


def yeardays(year):
  day1 = 0
  if year >= 1900:
    for i in range(1900, year):
      if leap_year(i) == 1:
        day1 += 366
      else:
        day1 += 365
  else:
    for i in range(year, 1900):
      if leap_year(i) == 1:
        day1 += 366
      else:
        day1 += 365
  return day1


def monthdays(year, month):
  if month == 2:
    if leap_year(year):
      days = 29
    else:
      days = 28
  elif month in [4, 6, 9, 11]:
    days = 30
  else:
    days = 31
  return days


def monthdays1(year, month):
  day2 = 0
  if leap_year(year) == 1:
    for i in range(0, month - 1):
      day2 = day2 + MonthDays_leapy[i]
  else:
    for i in range(0, month - 1):
      day2 = day2 + MonthDays_year[i]
  return day2


def thisMonthDays(year, month):
  if month in twelfthMonth:
    return 31
  elif leap_year(year) == 1 and month == 2:
    return 29
  elif leap_year(year) == 0 and month == 2:
    return 28
  else:
    return 30


def CaculateWeekDay(year, month, days):
  week = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期日'}
  m = 0
  yeardays(year)
  monthdays(year, month)
  m = yeardays(year) + monthdays1(year, month) + days - 1
  print('输入日期为：', week[(m % 7)])


def totaldays(year, month):
  yearday = 0
  for i in range(1990, year):
    if leap_year(i):
      yearday += 366
    else:
      yearday += 365
  for i in range(1, month):
    yearday += monthdays(year, i)
  return yearday


def week(year, month):
  thisDay = 0
  yDays = yeardays(year)
  mDays = monthdays1(year, month)
  if year >= 1900:
    sumDays = yDays + mDays
    thisDay = (sumDays % 7) + 1
  else:
    sumDays = yDays - mDays
    thisDay = 7 - (sumDays % 7)
  return thisDay


def Caculatemonth(year, month):
  week = (totaldays(year, month)) % 7
  print("\n")
  print('日\t一\t二\t三\t四\t五\t六\t')
  for i in range(0, week):
    print("\t", end="")
  for i in range(1, monthdays(year, month) + 1):
    if (totaldays(year, month) + i) % 7 == 0:
      print(i, end="\n")
    else:
      print(i, end="\t")


def Caculateyear(year):
  for i in range(1, 13):
    Caculatemonth(year, i)
    print()


def Caculate():
  year = int(input('请输入要查询的年份:'))
  month = int(input('请输入要查询的月份，若仅查年请输入0:'))
  days = int(input('请输入要查询的日期，若仅查月历或年历输入0:'))
  if year != 0 and month != 0 and days != 0:
    CaculateWeekDay(year, month, days)
  elif year != 0 and month != 0 and days == 0:
    Caculatemonth(year, month)
  else:
    Caculateyear(year)


Caculate()
