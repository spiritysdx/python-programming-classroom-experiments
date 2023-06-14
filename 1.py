# 1
while True:
  a = input("Please input number:")
  if len(a) > 3 or len(a) < 1:
    print("Error len, please input new number")
    continue
  else:
    print(f"个位：{str(a)[-1]}，十位：{str(a)[-2]}，百位：{str(a)[-3]}")
    break
# 2
while True:
  num = int(input("请输入一个正整数："))
  if num <= 1:
    print("素数必须大于1")
    continue
  tp = 2
  status = True
  while tp < num:
    if num % tp == 0:
      status = False
    tp += 1
  if status:
    print(f"{num}是素数")
  else:
    print(f"{num}不是素数")
  break


#3
def TP(a):
  return 1 / a


i = int(input("i:"))
temp = 1
for j in range(1, i + 1):
  temp *= TP(j)
print(f"第{i}项为：{temp}")
# 4
for i in range(1000, 10000):
  if str(i)[0] == str(i)[1] and str(i)[-1] == str(
      i)[-2] and str(i)[0] != str(i)[-1] and len(str(i)) == 4:
    if int(str(i)) in [a**2 for a in range(10, 100)]:
      print(i)
# 5
a = int(input("a:"))
b = int(input("b:"))
while True:
  t = min(a, b)
  if a != b:
    tp = []
    for i in range(1, t + 1):
      if max(a, b) % i == 0 and min(a, b) % i == 0:
        tp.append(i)
    print(max(tp))
    break
  elif a == b:
    print(a)
    break
