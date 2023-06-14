#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
import re,math

name = "410365"
# 读取空columns的以第一列为行索引的除去最后一列第122列的数据
data = pd.read_csv(f'{name}.csv',index_col = 0, header = None).drop(columns = [122])


# In[29]:


data


# In[30]:


# 多线程方差求解
import threading
import queue
from tqdm import tqdm

q = queue.Queue()
result_q = queue.Queue()

for elem in range(1,len(data.columns)+1):
    q.put(elem)

mean_list = []
for i in data.columns:
    mean_list.append(data[i].mean())

def temp_f():
    while True:
        if q.qsize() != 0:
            elem = q.get()
            tp = []
            mean = mean_list[elem-1]
            for j in list(data[elem]):
                ttpp = np.square(j - mean)
                tp.append(ttpp)
            result_q.put((elem, tp))
        else:
            break

threads = []
for i in tqdm(range(len(data.columns))):
    t = threading.Thread(target=temp_f)
    threads.append(t)
    t.start()

print('主程序运行中...')

# 等待所有线程任务结束。
for t in threads:
    t.join()

print("所有线程任务完成")


# In[31]:


# 栈反解数据列表
result_list = []
for i in range(result_q.qsize()):
    j = result_q.get()
    result_list.append(j)
result_list.sort(key=lambda x:x[0]) # 乱序排序


# In[32]:


# 生成方差dataframe  data2
data2_list = []
for i in result_list:
    data2_list.append(i[1])
data2 = pd.DataFrame(data2_list,columns=data.index,index=data.columns).T
data2


# In[33]:


# for i,j in data2.iterrows():
#     p = sum( k > j.mean() for k in j)
#     if p > 61:
#         print("Y")


# In[34]:


# 多线程判断求解
import threading
import queue
from tqdm import tqdm

g = queue.Queue()
result_g = queue.Queue()

for elem in range(len(data2.index)):
    g.put(elem)

rows_list = []
for i,j in data2.iterrows():
    rows_list.append((i,j))

def temp_g():
    while True:
        if g.qsize() != 0:
            elem = g.get()
            yuzhi = rows_list[elem][1].mean()
            p = sum( i > yuzhi for i in rows_list[elem][1])
            result_g.put((elem, p))
        else:
            break

threads = []
for i in tqdm(range(len(data2.index))):
    t = threading.Thread(target=temp_g)
    threads.append(t)
    t.start()

print('主程序运行中...')

# 等待所有线程任务结束。
for t in threads:
    t.join()

print("所有线程任务完成")

# 栈反解数据列表
result2_list = []
for i in range(result_g.qsize()):
    j = result_g.get()
    result2_list.append(j)
result2_list.sort(key=lambda x:x[0]) # 乱序排序

#result2_list


# In[35]:


drop_name_list = []
for i in result2_list:
    if i[1] > 15:
        # print(data2.index[i[0]])
        drop_name_list.append(data2.index[i[0]])
data3 = data.drop(drop_name_list)


# In[38]:


data3


# In[37]:


data3.to_csv(f"{name}_drop_by_variance.csv",header = None)


# In[ ]:


# tp_list = []
# for i in data.columns:
#     mean = data[i].mean()
#     tp = []
#     for j in list(data[i]):
#         ttpp = np.square(j - mean)
#         tp.append(ttpp)
#     tp_list.append(tp)
# pd.DataFrame(tp_list)


# In[ ]:




