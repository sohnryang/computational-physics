"""
differntial_equation
====================

A module containing two algorithms for solving differntial equation.
"""
import numpy as np

def euler_method(func, t_start, t_end, y_init, step):
    """
    euler_method(func, t_start, t_end, y_init, step)

    Solve a differntial equation with Euler Method.

    Parameters
    ----------
    func: function
        A function which gets a numpy array [x, v] and t, and returns numpy
        array [v, a].
    t_start: float
        The time to start solving DE.
    t_end: float
        The time to finish solving DE.
    y_init: float
        The initial value of y.
    step: float
        The step to take while solving DE.
    """
    time = np.linspace(t_start, t_end, step)
    h = time[1] - time[0]
    y_arr = np.array([y_init])
    y = y_init
    n = 0
    while len(y_arr) < len(time):
        y = y + h * func(y, time[n])
        y_arr = np.append(y_arr, [y], axis=0)
        n += 1
    return y_arr, time


def rk2_algorithm(func, t_start, t_end, y_init, step):
    """
    rk2_algorithm(func, t_start, t_end, y_init, step)

    Solves a DE with RK2 algorithm. This is more accurate than Euler Method.

    Parameters
    ----------
    func: function
        A function which gets a numpy array [x, v] and t, and returns numpy
        array [v, a].
    t_start: float
        The time to start solving DE.
    t_end: float
        The time to finish solving DE.
    y_init: float
        The initial value of y.
    step: float
        The step to take while solving DE.
    """
    time = np.linspace(t_start, t_end, step)
    h = time[1] - time[0]
    y_arr = np.array([y_init])
    y = y_init
    n = 0
    while len(y_arr) < len(time):
        y_rk2 = y + h * func(y, time[n]) / 2
        y = y + h * func(y_rk2, time[n] + h / 2)
        y_arr = np.append(y_arr, [y], axis=0)
        n += 1
    return y_arr, time
