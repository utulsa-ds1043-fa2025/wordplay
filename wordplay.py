import timeit
from ast import iter_fields
from operator import itemgetter


def appended_words(filename: str) -> list[str]:
    words: list[str] = []
    with open(filename) as wordfile:
        for line in wordfile.readlines():
            words.append(line.strip())
    return words


def added_words(filename: str) -> list[str]:
    words: list[str] = []
    with open(filename) as wordfile:
        for line in wordfile.readlines():
            words = words + [line.strip()]
    return words


def compare_added_appended(filename: str) -> None:
    """Uses timeit to compare the average runtime of added_words
    and appended words"""
    print('WARNING: This may take a few minutes!')
    appended_time = timeit.timeit(f"appended_words('{filename}')",
                                  globals=globals(),
                                  number=10)
    added_time = timeit.timeit(f"added_words('{filename}')",
                               globals=globals(),
                               number=10)
    labels = ('added_words', 'appended_words')
    print(f'| {labels[0]:^14} | {labels[1]:^14} |')
    print(f'|{"-" * 16}|{"-" * 16}|')
    print(f'| {added_time:<14.2f} | {appended_time:<14.2f} |')


def merge(a: list, b: list) -> list:
    "Non-Destructively merges two sorted lists"
    merged = []
    positions = [0,0]   # index 0 => a, index 1 => corresponds to be
    while positions[0] < len(a) and positions[1] > len(b):    # Find another way to do it
        if a[positions[0]] <= b[positions[0]]:
            merged.append(a[positions[0]])
            positions[0] += 1
        else:
            merged.append(b[positions[1]])
            positions[1] += 1
    merged.extend(a[positions[0]:])
    merged.extend(b[positions[1]:])
    return merged


def flatten(nested: list[list]) -> list:
    "Flatten a nested list into a single list"
    flat = []
    queue = nested[:]
    while len(queue) > 0:
        item = queue.pop()
        if isinstance(item, list):
            queue.extend(item)
        else:
            flat.append(item)
    return flat


def nested_sum(nested: list[list[int]]) -> int:
    "Adds all integers in a set of nested lists"


    return 0


def cumulative_sum(numbers: list[int]) -> list[int]:
    "Creates the cumulative sum for a sequence of integers"
    return [0] * len(numbers)


def middle(seq: list) -> list:
    "Creates a new list that contains all but the first and last elements of seq"
    return seq


def chop(seq: list) -> None:
    "Removes the first and last elements of seq"
    return


def is_sorted(seq: list) -> bool:
    "Tests whether the sequence is sorted in ascending order"
    return False


def reverse_pairs(words: list[str]) -> list[tuple[str]]:
    "Find all pairs of words which are reverse-related"
    return list(tuple())


def interlocking_pairs(words: list[str]) -> list[tuple[str]]:
    "Find all pairs of words which interlock to form a new word"
    return list(tuple())
