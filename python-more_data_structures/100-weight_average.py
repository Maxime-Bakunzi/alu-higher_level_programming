#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weight = sum(list(num[1] for num in my_list))
    total = sum(num[0] * num[1] for num in my_list)
    return total / total_weight
