from ..app import calculate_total

def test_calculate_total_adds_two_numbers():
    assert calculate_total(2, 3) == 5
