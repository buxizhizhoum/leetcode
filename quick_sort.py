#!/usr/bin/python
# -*- coding: utf-8 -*-


def quick_sort(numbers):
    if not numbers:
        return []

    if len(numbers) == 1:
        return numbers

    pivot = numbers[0]

    left = [item for item in numbers[1:] if item < pivot]
    right = [item for item in numbers[1:] if item > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    import random

    test_numbers = range(100)
    random.shuffle(test_numbers)
    print(test_numbers)
    print(quick_sort(test_numbers))





