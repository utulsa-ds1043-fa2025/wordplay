import wordplay
import random

random.seed()


def test_merge():
    a: list[int] = list(range(0, 10, 2))  # Even numbers 0..8, 5 total
    b: list[int] = list(range(1, 10, 2))  # Odd numbers 1..9, 5 total
    merged: list[int] = wordplay.merge(a, b)
    assert merged == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert len(a) == 5 and len(b) == 5
    assert len(merged) == 10


def test_nested_sum():
    assert wordplay.nested_sum([[1,2], [3,4]]) == 10


def test_cumulative_sum():
    assert wordplay.cumulative_sum([1,2,3,4]) == [1, 3, 6, 10]


def test_middle():
    assert False


def test_chop():
    assert False


def test_is_sorted():
    a: list[int] = list(range(10))
    b: list[int] = a[:]
    assert wordplay.is_sorted(a)
    for _ in range(10):
        random.shuffle(b)
        if a == b:
            assert wordplay.is_sorted(b)
        else:
            assert not wordplay.is_sorted(b)


def test_reverse_pairs():
    assert False


def test_interlocking_pairs():
    assert False


def test_cumulative_sum():
    assert False
