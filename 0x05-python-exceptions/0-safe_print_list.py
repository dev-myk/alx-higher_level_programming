#!/usr/bin/python3

"""a function that prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in range(0, x):
            print(my_list[i], end="")
            count += 1
    except Exception:
        print()
        return count
    finally:
        print('')
        return count
