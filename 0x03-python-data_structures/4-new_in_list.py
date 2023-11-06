#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listlength = len(my_list) - 1
    dup_list = my_list[:]
    if idx < 0 and idx > listlength:
        return (my_list)
    else:
        dup_list[idx] = element
        return dup_list
