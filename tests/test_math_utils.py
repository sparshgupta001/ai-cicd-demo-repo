from math_utils import add
from database import connect

def test_add():
    assert add(2, 3) == 5

def test_database():
    assert connect() == "Connected"