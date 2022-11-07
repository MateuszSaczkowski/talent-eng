import pytest
def add_values(val_1, val_2):
    '''
    Function that returns sum of two values
    '''
    return val_1 + val_2


#positive tests

def test_positive_float():
    assert isinstance(30/6, float)


def test_positive_bool():
    value_1 = True
    assert value_1
    

def test_positive_add_values():
    assert add_values(2, 2) == 4



# negative tests

def test_negative_str():
    assert 'a' == 'g'


def test_negative_equality():
    a = 3
    b = 2
    assert a == b

def test_negative_tuple():
    assert isinstance({'a': 2}, tuple)