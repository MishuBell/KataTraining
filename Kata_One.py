# Return Two Highest Values in List

# In this kata, your job is to return the two distinct highest values in a list. 
# If there're less than 2 unique values, return as many of them, as possible.
# The result should also be ordered from highest to lowest.

highest = 0
second_highest = 0

# Check element 1, add it to highest
# Compare to element 2, if element 2 is higher, assign it to highest
# check element 3, compare it to highest - if it is higher, assign it
# if it is lower, compare it two second_highest - if it is higher, assign it
# if it is lower, move on to element 4

# probably in a for loop? Ughh??

def two_highest(arg1):
    arg1_sorted_desc = sorted(arg1, reverse=True)
    

    pass