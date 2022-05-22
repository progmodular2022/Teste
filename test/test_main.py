import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

import main

def test_sum():
    assert main.sum(3, 4) == 7
    assert main.sum(3.5, 4) == 7.5
    assert main.sum(-1, 4) == 3
    assert main.sum(0, 4) == 4
    
def test_arr_to_str():
    assert main.arr_to_str([112]) == 'p'
    assert main.arr_to_str([72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100]) == 'hello, world'
    assert main.arr_to_str([97, 98, 97, 99, 97, 120, 105]) == 'abacaxi'
