#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    nums = tuple(map(int, input('Введите ряд из чисел через пробел:').split()))
    pos = 0

    for i in range(len(nums)):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            pos = i
        if nums[i] == nums[-1]:
            for j in range(len(nums)):
                if j == pos - 1:
                    break
                else:
                    print(nums[j])

