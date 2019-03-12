from numpy import *
from pylab import *
x = linspace(1, 10, 50)
y = x * x
title('My 1st graph')
xlabel('Time (fortnights)')
ylabel('Distance (furlongs)')
xlim(0, 10)
ylim(0, 100)
plot(x, y, 'ro')
show()
