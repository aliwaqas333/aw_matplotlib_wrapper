# mympl/plotter.py

import matplotlib.pyplot as plt


def setup_mpl():
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman']
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.grid'] = False


def my_plot(*args, **kwargs):
    setup_mpl()  # Apply custom settings
    plt.plot(*args, **kwargs)
    plt.show()
