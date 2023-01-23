"""
Write a python function to find numbers in a given text, store numbers in a list
and return list (TSRS)
"""

# defining a function "find_numbers()" which takes string as an argument and 
# returns a list of numbers exist in string
def find_numbers(string):
    # creating an empty list
    num_list = []
    
    for e in string:
        if e.isdigit():
            num_list.append(e)
    
    return num_list


# taking input from the user
string = input("Enter a string : ")

# printing a list of numbers
print("List of numbers in string :", find_numbers(string))