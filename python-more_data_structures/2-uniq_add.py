#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    sorted_list = sorted(set(my_list))
    for i in range(len(sorted_list)):
        sum += sorted_list[i]
    return (sum)
