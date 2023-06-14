#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([sc * wt for sc, wt in my_list]) / sum(wt for sc, wt in my_list)
