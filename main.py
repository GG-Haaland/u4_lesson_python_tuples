def create_tuple(list_of_nums):
    # Create a tuple from a list and return it.
    #list_of_nums = [1,2,4,5,6,8,9]
    new_tuple = tuple(list_of_nums)
    return new_tuple


def get_value(tup):
    # Return the 3rd value in the provided tuple
    #tup = ("apple", "orange", "watermelon", "grape", "banana")
    return tup[2]


def get_values(tup):
    # return the values from index 1-3
    # 3 should be inclusive
    #tup = ("apple", "orange", "watermelon", "grape", "banana")
    return tup[1:3]


def get_max(tup):
    # return the largest number in the provided tuple
    #tup = (1,2,4,5,6,8,9)
    return max(tup)

