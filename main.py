import numpy as np
import time
import dataload
import random
import tree
import plot

set_up_times = {}
match_times = {}
abscissa = [90, 900, 9000, 90000, 900000]
if __name__ == '__main__':

    # load data
    dataload.load()
    # simulate
    for route_basic_count in abscissa:
        # generate
        [route_numbers, route_lengths] = dataload.get_with_random(route_basic_count)
        new_tree = tree.Tree(numbers=route_numbers, lengths=route_lengths)
        set_up_time = new_tree.generate()
        set_up_times[route_basic_count] = set_up_time
        # match
        match_cost = {}
        for route_match_count in abscissa:
            match_time = new_tree.match_all(route_match_count)
            match_cost[route_match_count] = match_time
        match_times[route_basic_count] = match_cost
    # plot
    print(set_up_times)
    print(match_times)
    plot.plot(abscissa=abscissa, set_up_times=set_up_times, match_times=match_times)
