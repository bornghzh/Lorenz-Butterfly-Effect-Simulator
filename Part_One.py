import pylab
from numpy import array, linspace
from scipy.integrate import solve_ivp
from mpl_toolkits import mplot3d

def f(t,r): ###lorenz
    x, y, z = r
    fi=28
    beta=2.67
    sig=10
    tx = sig * (y - x)
    ty = fi * x - y - x * z
    tz = x * y - beta * z
    return array([tx, ty, tz], float)

fig = pylab.figure()
paxes = pylab.axes(projection="3d")
h = solve_ivp(f, [0, 200], [1, 1, 1], t_eval=linspace(0, 200, 60000)) ### hal ba initial values
paxes.plot3D(h.y[0, :], h.y[1, :], h.y[2, :], linewidth=0.3 , color ="red" )
h2 = solve_ivp(f, [0, 200], [1 + 1e-6, 1 + 1e-6, 1 + 1e-6], t_eval=linspace(0, 200, 60000)) ###hal ba initial values + 1e-6 -->estbate lorenz
paxes.plot3D(h2.y[0, :], h2.y[1, :], h2.y[2, :], linewidth=0.3 , color ="blue" )
pylab.show()

