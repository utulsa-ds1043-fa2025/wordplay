import wordplay

def test_merge():
    a = list(range(0, 10, 2)) # even numbers 0-8, 5 total
    b = list(range(1, 10, 2)) # odd numbers 1-9, 5 total
    merged = wordplay.merge (a, b)
    assert merged == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert len(a) == 0 or len(b) == 0


# def commented_test_merge():
#     a = list(range(0, 10, 2)) # even numbers 0-8, 5 total
#     b = list(range(1, 10, 2)) # odd numbers 1-9, 5 total
#     merged = wordplay.merge (a, b)
#     assert merged == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     assert len(a) == 5 and len(b) == 5
#     assert len(merged) == 10
# this code doesn't destroy one of the lists in order to merge them