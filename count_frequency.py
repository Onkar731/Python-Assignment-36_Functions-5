"""
Write a python function to count frequency of each element of the list and store
list elements in the dict object as keys and element frequency as data values (TSRS)
"""

# defining a function "count_frequency()" which takes list as an argument
# and returns dictionary object 
def count_frequency(list):
    dict_freq = dict()
    
    for e in list:
        dict_freq[e] = list.count(e)
    
    return dict_freq

# printing a dictionary of elements
for k,v in (count_frequency([1,2,4,5,2,3,5,6,4,6,8,9,8,89,10,2,3,4,5,6,7,85,4,3,2])).items():
    print(k, '-->', v)