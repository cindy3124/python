#! /usr/bin/env python
# coding=utf-8

import random


def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)
    return random.choice([nums, None, 10])


if __name__ == '__main__':
    print(bubble_sort([3, 1, 7, 4, 0, 8, 6]))
