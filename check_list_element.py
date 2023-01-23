"""
Write a python function to check if two given list have same elements in any order
or not. Return True or False (TSRS)
"""

# defining a function "check_lists()" which takes two list as an argument
# and returns True or False whether the elements are same or not
def check_lists(l1, l2):
    for e in l1:
        if e not in l2:
            return False
    return True

# creating two list
l1, l2 = [1,2,4,5,3], [1,5,4,2,3] #[3,5,4,1,2]

# printing true or false whether the elements are same or not
print(check_lists(l2, l1))