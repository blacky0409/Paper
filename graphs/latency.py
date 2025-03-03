#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

f = open("./latency", "r")
lines = f.readlines()
data1 = []
data2 = []
for line in lines:
    e = line.split()
    data1.append(float(e[0]))
    data2.append(float(e[1]))
#    data3.append(float(e[2]))

'''
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 8
plt.rcParams['font.family'] = 'sans-serif'
'''

fig, ax = plt.subplots()

fig.set_size_inches(4.5, 2.5)

'''
ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x/1000), ',')))
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))

data1 = np.cumsum(time_large_1[:last]) / mcsec
print((data1[-1] + large2_x[-1] + large3_x[-1]) / 3)
'''
x_values = [1, 10, 50, 100, 200, 400, 600, 800, 1000]

plt.plot(x_values[:len(data1)], data1, label='SQLite', color='C0')
plt.plot(x_values[:len(data2)], data2, label='Git', color='C1')
#plt.plot(data2, label='B', color='C1')

plt.grid(linestyle='dotted', linewidth=0.5)

#plt.title('Page Allocation Latency')
plt.xlabel('Round')
plt.ylabel('Latency (unit..)')
plt.legend(loc='upper right', ncol=1, prop={'size': 8})

plt.tight_layout()
plt.savefig('latency.pdf')
