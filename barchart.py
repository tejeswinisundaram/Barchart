import numpy as np
import matplotlib.pyplot as plt

N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.15      # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [209.093, 16.544, 54.941, 6.143, 3193.08/5]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [55.581, 17.133, 50.227, 5.245, 2700.95/5]
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [210.926, 16.649, 438.139, 25.572, 169.122/5]
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('Time in milli seconds')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('bgfg_segm', 'hog', 'pylr_opt', 'square','clahe') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Host', 'GPGPU', 'MIC') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()
