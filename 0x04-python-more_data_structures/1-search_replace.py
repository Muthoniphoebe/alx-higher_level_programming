#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modif_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            modif_list[i] = replace
    return modif_list
