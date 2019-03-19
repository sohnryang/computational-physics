from projectile_graph import *
import pylab as pl
import numpy as np

x = 0
y = 0
vx = 100
vy = 100
y = np.array([x, vx, y, vy])
def projectile(y, t):
    ay = -9.8
    ax = 0
    vx = y[1]
    vy = y[3]
    f = np.array([vx, ax, vy, ay])
    return f

b = RK2(projectile, 0, 15, y, 100)
X = b[0][:,0]
Y = b[0][:,2]
t = b[1]

pl.plot(X, Y, '-')
pl.legend(['Projectile'])
pl.xlabel('X')
pl.ylabel('Y')
pl.title('Projectile')
pl.show()
