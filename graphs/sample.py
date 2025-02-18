#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

f = open("./seq-huge/seq-huge2.res", "r")
lines = f.readlines()
time_huge_1 = []
for line in lines:
    time_huge_1.append(float(line))

'''
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 8
plt.rcParams['font.family'] = 'sans-serif'
'''

fig, ax = plt.subplots()

fig.set_size_inches(4.5, 2.5)

ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x/1000), ',')))
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))

last = 16000
mcsec = 1e6

large1_x = np.cumsum(time_large_1[:last]) / mcsec
print((large1_x[-1] + large2_x[-1] + large3_x[-1]) / 3)

nolarge1_x = np.cumsum(time_nolarge_1[:last]) / mcsec
print((nolarge1_x[-1] + nolarge2_x[-1] + nolarge3_x[-1]) / 3)

huge1_x = np.cumsum(time_huge_1[:last]) / mcsec
print((huge1_x[-1] + huge2_x[-1] + huge3_x[-1]) / 3)

plt.plot(huge1_x, label='Hugepage', color='C0')
plt.plot(nolarge1_x, label='Basepage', color='C1')
plt.plot(large1_x, label='Hyperpage', color='C2')

plt.grid(linestyle='dotted', linewidth=0.5)

#plt.title('Page Allocation Latency')
plt.xlabel('Allocated Memory (GiB)')
plt.ylabel('Time (second)')
plt.legend(loc='upper left', ncol=1, prop={'size': 8})

plt.tight_layout()
plt.savefig('seq-huge.pdf')
