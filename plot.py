from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def plot(abscissa,set_up_times,match_times):



    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    X = abscissa
    Y = abscissa
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)



    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()


