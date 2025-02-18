#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

f = open("./sample-lines", "r")
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

plt.plot(data1, label='A', color='C0')
plt.plot(data2, label='B', color='C1')

plt.grid(linestyle='dotted', linewidth=0.5)

#plt.title('Page Allocation Latency')
plt.xlabel('X-axis')
plt.ylabel('Values (second)')
plt.legend(loc='upper left', ncol=1, prop={'size': 8})

plt.tight_layout()
plt.savefig('sample-lines.pdf')
