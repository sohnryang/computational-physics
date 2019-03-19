import numpy as np
import pylab as pl

A = np.arange(1, 7, 1)
B = np.array([2, 4, 3, 5, 2, 3])
C = np.array([2, 3, 1, 4, 2, 5])

pl.figure()
pl.subplot(121)
pl.plot([2, 3, 4, 5], '-')
pl.subplot(122)
pl.plot([1, 2, 3, 4], '-')
pl.show()
