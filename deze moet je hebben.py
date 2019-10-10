import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import TISTNplot as fm

# Open data file.
df = pd.read_csv('tabelpython.csv', header=None, sep='.', decimal=',', delimiter=';')
print(df)

# Load different values from the .csv document and put it in dataframe.
u = np.array(df.values[:, 0])
i = np.array(df.values[:, 1])
r = np.array(df.values[:, 2])
b = np.array(df.values[:, 4])

# Load x- and y-values
y = 1/(r**2)
x = (b**2)/(2*u)

def plot_data():
    
    fig, ax = plt.subplots()
    
    # Make numbers axes two figures with commas.
    fm_x = fm.TNFormatter(2)
    fm_y = fm.TNFormatter(2)
    
    ax.yaxis.set_major_formatter(fm_y)
    ax.xaxis.set_major_formatter(fm_x)
    ax.set_abixbelow(True)
    
    # Data points with errorbars on the y-axis.
    ax.errorbar(x, y, yerr=y*0.2, fmt='o', c='k',
                 elinewidth=0.5, capsize=2.5, capthick=1, label='Geen idee')
    
    # Plot theory.
    plt.scatter(x, y, c='k', linewidth=1, label='Theorie')
    
    # The visual aspects of the plot.
    plt.xlabel('B^2/2*U', fontsize=10)
    plt.ylabel('1/r^2', fontsize=10)
    plt.grid(axis='both')
    plt.legend(loc='upper left')
    plt.savefig('Data.pdf')

    plt.show()

plot_data()
