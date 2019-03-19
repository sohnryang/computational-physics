def function(x):
    a = x * x
    return a

import numpy as np
import pylab as pl
x = np.linspace(0, 10)
y = function(x)
pl.plot(x, y, '-')
pl.show()
