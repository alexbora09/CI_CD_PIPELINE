from src.math_operations import add, subtract



def test_add():
    assert add(2,4)==6
    assert add(-3,3)==0
    assert add(-5,2)==-3


def test_substract():
    assert subtract(5,2)==3
    assert subtract(4,6)==-2
    

