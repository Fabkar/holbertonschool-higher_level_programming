#!/usr/bin/python3
def weight_average(my_list=[]):
        x = 0
        count = 0
        for i in my_list:
                count += i[1]
                x += i[0] * i[1]
        return x/count
