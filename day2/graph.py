import numpy as np
import pylab as pl

time = np.linspace(0.0, 10.0, 10000)
height = np.exp(-time / 3.0) * np.sin(time * 3)
pl.figure()
pl.plot(time, height, 'm-')
pl.plot(time, 0.3 * np.sin(time * 3), 'g-')
pl.legend(['damped', 'constant amplitude'], loc='upper right')
pl.xlabel('Time (s)')
pl.show()
