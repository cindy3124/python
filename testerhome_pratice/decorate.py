# coding:utf-8

import time


def time_count(func):
    def wrap(*args, **kwargs):
        time_flag1 = time.time()
        temp_result = func(*args, **kwargs)
        time_flag2 = time.time()
        print("time cost:", time_flag2-time_flag1)
        return temp_result
    return wrap


@time_count
def print_num(x):
    for i in range(x):
        print(i)


print_num(100)

