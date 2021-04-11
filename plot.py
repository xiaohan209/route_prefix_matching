from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def plot(abscissa, set_up_times, match_times):
    generate_times = []
    find_times = {}

    for i in abscissa:
        generate_times.append(set_up_times[i])
        find_cost = []
        for j in abscissa:
            find_cost.append(match_times[i][j])
        find_times[i] = find_cost

    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    ax.set_title("route set-up time")
    ax.set_xlabel("count in route-table(line)")
    ax.set_ylabel("time(s)")
    ax.plot(abscissa, generate_times, label="set-up-time")

    ax1 = fig.add_subplot(2, 1, 2)
    ax1.set_title("find route time")
    ax1.set_xlabel("count of finding scale(line)")
    ax1.set_ylabel("time(s)")
    for i in abscissa:
        ax1.plot(abscissa, find_times[i], label="count: " + str(abscissa) + " line")
    plt.xscale('log')
    plt.show()
    fig.savefig("match.png",dpi=800)
