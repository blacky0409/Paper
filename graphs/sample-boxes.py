#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

f = open("./sample-boxes", "r")
lines = f.readlines()
data1 = []
data2 = []
for line in lines:
    e = line.split()
    data1.append(float(e[0]))
    data2.append(float(e[1]))

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

x = np.arange(len(lines))
width = 0.3

plt.bar(x - 0.15, data1, width, edgecolor='black', color='C0', linewidth=0.5, label='A')
plt.bar(x + 0.15, data2, width, edgecolor='black', color='C1', linewidth=0.5, label='A')

plt.grid(linestyle='dotted', linewidth=0.5)

#plt.title('Page Allocation Latency')
plt.xlabel('X-axis')
plt.ylabel('Values (second)')
plt.legend(loc='upper left', ncol=1, prop={'size': 8})

plt.tight_layout()
plt.savefig('sample-boxes.pdf')
