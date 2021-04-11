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
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("路由建立时间图")
    ax.set_xlabel("路由表数量(条)")
    ax.set_ylabel("建立时间(s)")
    ax.plot(abscissa, generate_times, label="建立时间")
    plt.show()
    fig.savefig("setup.png", dpi=800)
    fig2 = plt.figure()
    ax1 = fig2.add_subplot(1, 1, 1)
    ax1.set_title("查找路由时间图")
    ax1.set_xlabel("查找数量(条)")
    ax1.set_ylabel("查找时间(s)")
    for i in abscissa:
        ax1.plot(abscissa, find_times[i], label="路由表" + str(abscissa) + "条")
    plt.show()
    fig2.savefig("match.png",dpi=800)
