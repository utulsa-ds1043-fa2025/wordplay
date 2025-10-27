import wordplay

def test_merge():
    a = list(range(0, 10, 2)) # Even numbers 0..8, 5 total
    b = list(range(1, 10, 2)) # Odd numbers 1..9, 5 total
    merged = wordplay.merge(a, b)
    assert merged == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert len(a) == 5 and len(b) == 5
    assert len(merged) == 10
