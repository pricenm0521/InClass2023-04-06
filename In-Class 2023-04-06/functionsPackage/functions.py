# functions.py
import numpy as np

# write a function that accepts a numpy array and returns a new numpy array with just the odd values from the first array

def get_odd_values(some_array):
    return some_array[some_array %2 ==1]

# write a function that accepts 2 numpy arrays and returns the common values in them as another numpy array

def find_common_values(np1, np2):
    common_values = np.intersect1d(np1, np2)
    return common_values
# could be done as one statement as return np.intersect1d(np1,np2)

# write a function called F_to_C that accepts as a parameter a numpy array
# and converts all the elements from fareheit to centigrade
# then returns the converted array

def F_to_C(array_of_temperatures):
    # iterate over the individual elements in the array
    # add try/except logic around the loop and return some "flag" value in case of an error
    try:
        for i in range(0, len(array_of_temperatures)):
            # convert the element at index i to centigrade
            array_of_temperatures[i] = (array_of_temperatures[i] - 32)*(5/9)
        return array_of_temperatures
    except:
        # there was an exception, we caught it, now we need to return a "flag" value to indicate there was a problem
        return np.array([np.NaN])
# no print as the pseudo code does not call for printing

        