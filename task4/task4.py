import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy.misc import derivative

def fn_plot1d(fn, x_min, x_max, filename):
    num_values = 1000
    x = np.linspace(x_min, x_max, num_values)
    fnv = np.vectorize(fn)
    y = fnv(x)
    Xlabel = "X axis"
    Ylabel = fn.__name__ + "(x)"
    Title = "1D plot of " + Ylabel
    plt.plot(x, y)
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.title(Title)
    #plt.show()
    plt.savefig(filename)
    plt.clf()

def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
    num_x = 1000
    num_y = 1000
    x = np.linspace(x_min, x_max, num_x)
    y = np.linspace(y_min, y_max, num_y)
    X,Y = np.meshgrid(x,y)
    fnv = np.vectorize(fn)
    Z = fnv(X,Y)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.plot_surface(X,Y,Z)
    Xlabel = "X axis"
    Ylabel = "Y axis"
    Zlabel = fn.__name__ + "(x,y)"
    Title = "2D plot of " + Zlabel
    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_zlabel(Zlabel)
    ax.set_title(Title)
    #plt.show()
    ax.figure.savefig(filename)
    #plt.gca(projection = 'rectilinear')
    plt.clf()

def nth_derivative_plotter(fn, n, x_min, x_max, filename):
    num_values = 1000
    x = np.linspace(x_min, x_max, num_values)
    fnv = np.vectorize(fn)
    y = derivative(fnv,x,dx = 1e-3, n = n)
    strn = str(n)
    Xlabel = "X axis"
    Ylabel = fn.__name__ + fr'$^{{({strn})}}$' + '(x)'
    Title = "nth derivative plotter (n = " + strn + ")" 
    plt.plot(x,y)
    plt.xlabel(Xlabel)
    plt.ylabel(Ylabel)
    plt.title(Title)
    plt.savefig(filename)
    plt.clf()

def h(x):
    if x > 0:
        return np.exp(-1/(x*x))
    else:
        return 0

def g(x):
    return (h(2-x)/(h(2-x)+h(x-1)))

def b(x):
    if x < 0:
        x = -x
    return g(x)

def sinc(x,y):
    if (x == 0 and y == 0):
        return 1
    else:
        norm = (x**2 + y**2) ** (0.5)
        return (np.sin(norm)/norm)


if __name__ == '__main__':
    #fn_plot1d(b,-2,2,'fn1plot.png')
    #fn_plot2d(sinc, -1.5*np.pi, 1.5*np.pi, -1.5*np.pi, 1.5*np.pi, 'fn2plot.png')
    #nth_derivative_plotter(b, 1, -2, 2, 'bd_1.png')
    #nth_derivative_plotter(b, 2, -2, 2, 'bd_2.png')
