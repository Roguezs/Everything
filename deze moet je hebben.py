import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import TISTNplot as fm

# Open data file.
df = pd.read_csv('tabelpython.csv', header=None, sep='.', decimal=',')

# Load different values from the .csv document and put it in dataframe.
u = df.values[:, 0]
i = df.values[:, 1]
r = df.values[:, 2]
b = df.values[:, 3]

# Load x- and y-values
y = 1/(r^2)
x = (b^2)/(2*u)

# Make array from intensiteit and stroom.
y = np.array(y)
x = np.array(x)

def plot_data():
    
    # Data points with errorbars on the y-axis.
    plt.errorbar(x, y, yerr=y*0.2, fmt='o', c='k',
                 elinewidth=0.5, capsize=2.5, capthick=1, label='Geen idee')
    
    # Plot theory.
    plt.plot(x, y, c='k', linewidth=1, label='Theorie')
    
    # Make numbers axes two figures with commas.
    fm_x = fm.TNFormatter(2)
    fm_y = fm.TNFormatter(2)

    plt.axes().get_xaxis().set_major_formatter(fm_x)
    plt.axes().get_yaxis().set_major_formatter(fm_y)

    # The visual aspects of the plot.
    plt.xlabel('B^2/2*U', fontsize=10)
    plt.ylabel('1/r^2', fontsize=10)
    plt.grid(axis='both')
    plt.legend(loc='upper left')
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()

plot_data()
