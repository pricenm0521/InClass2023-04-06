# demo.py
import numpy as np
from functionsPackage.functions import *

def demo():
    '''
    demonstrate all of the functions we'll write
    '''
    print(find_common_values(np.array([1,2,3]),np.array([2,4,6])))
    # one line vs many lines below
    find_common_values("a", 42)
    answer = F_to_C(42) # this is not a correct type to pass to the function
    print(answer)
    some_data = np.arange(5) # 5 element array
    some_data[0] = 100
    some_data[1] = 0
    some_data[2] = 32
    some_data[3] = 212
    some_data[4] = -40
    answer = F_to_C(some_data) # the value returned by F_to_c is stored in answer
    print(answer)
    
    test1 = np.arange(20,40).reshape(4,5)
    test2 = np.arange(10,30).reshape(4,5)
    test = find_common_values(test1, test2)
    print(test)
    
    oddtest = np.arange(10,20).reshape(5,2)
    otest = get_odd_values(oddtest)
    print(otest)
    
    print(get_odd_values(np.arange(20,30).reshape(5,2)))