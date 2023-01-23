"""
Write a python function to remove duplicate elements from a given list (TSRS)
"""

# defining a function "remove_duplicate()" which takes a list as an argument
# and returns a list of distinct element list
def remove_duplicate(list):
    disnt_list = []
    i = 0
    while i < len(list):
        if i == list.index(list[i]):
            disnt_list.append(list[i])
        i += 1
    
    return disnt_list


# printing a list of distinct element
print("Removed duplicate elements from the list :", remove_duplicate([1,2,34,6,4,5,6,7,84,3,3,2,54,6,4,3,5,3,5,]))
