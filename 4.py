# 1
class Calendar(object):

  def __init__(self, year, month):

    self.year = year
    self.mouth = month

  def leap_year(self, year):
    tpyear = self.year
    if (tpyear % 4 == 0 and tpyear % 100 == 0) or (tpyear % 400 == 0):
      return True
    else:
      return False

  def monthdays(self, year, month):
    if month == 2:
      if self.leap_year(year):
        days = 29
      else:
        days = 28
    elif month in [4, 6, 9, 11]:
      days = 30
    else:
      days = 31
    return days

  def totaldays(self, year, month):
    yearday = 0
    for i in range(1990, year):
      if self.leap_year(i):
        yearday += 366
      else:
        yearday += 365
    for i in range(1, month):
      yearday += self.monthdays(year, i)
    return yearday

  def c_print(self, year, month):

    week = (self.totaldays(year, month)) % 7
    print("\n")
    print('日\t一\t二\t三\t四\t五\t六\t')
    for i in range(0, week):
      print("\t", end="")
    for i in range(1, self.monthdays(year, month) + 1):
      if (self.totaldays(year, month) + i) % 7 == 0:
        print(i, end="\n")
      else:
        print(i, end="\t")
    print("\n")


wnl = Calendar(2022, 10)
wnl.c_print(2022, 10)

# 2


class Person(object):

  def __init__(self, year, month):

    self.year = year
    self.mouth = month

  def leap_year(self, year):
    return Calendar.leap_year(self, year)

  def monthdays(self, year, month):
    return Calendar.monthdays(self, year, month)

  def totaldays(self, year, month):
    return Calendar.totaldays(self, year, month)

  def p_print(self, year, month):
    return Calendar.c_print(self, year, month)


p = Person(2022, 10)
p.p_print(2022, 10)

# 3


class Student(object):

  def __init__(self, name, course, scores):
    self.name = name
    self.course = course
    self.scores = scores

  def get_name(self):
    return self.name

  def get_course(self):
    return self.course

  def get_scores(self):
    return self.scores


stu = Student('小明', ["Chinese", "Math", "English"], [45, 80, 91])
print("姓名：%s" % (stu.get_name()))
print("课程：%s" % (stu.get_course()))
print("分数：%s" % (stu.get_scores()))

# 4


class ClassAnalyzer(object):

  def __init__(self, stu, course, scores):
    self.course = course
    self.scores = scores
    self.stu = stu

  def search(self):
    l = []
    for i in range(len(self.scores)):
      if self.scores[i] < 60:
        l.append(i)
    print('不及格同学信息：')
    for i in l:
      print(
        str(self.stu[i]) + " " + self.course[i] + " " + str(self.scores[i]))


tea = ClassAnalyzer(['小明', '小红', '小李'], ["Chinese", "Math", "English"],
                    [45, 80, 91])
tea.search()