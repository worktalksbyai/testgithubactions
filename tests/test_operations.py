from src.math_operations import add, sub

def test_ad():
    assert add(2,3) == 5
    assert add(-1,1) == 0
   
def test_sub():  
    assert sub(5,3) == 2
    assert sub(4,3) == 1
    assert (2,3) == -1



