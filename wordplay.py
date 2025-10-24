import timeit
from collections.abc import Collection


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
    """Destructively merges two sorted lists"""
    merged = []
    while len(a) > 0 and len(b) > 0:
        if a[0]<=b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    merged.extend(a)
    merged.extend(b)
    return merged

def merge_2(a:list, b:list) -> list:
    """Non-destructively merges two sorted list"""
    merged = []
    indices = {
        'a': 0,
        'b': 0
    }
    while indices['a'] < len(a) and indices['b'] < len(b):
        if a[indices['a']] <= b[indices['b']]:
            merged.append(a[indices['a']])
            indices['a'] += 1
        else:
            merged.append(b[indices['b']])
            indices['b'] += 1
    merged.extend(a)
    merged.extend(b)
    return merged

def flatten(nested: list[list]) -> list:
   """Flatten a nested list into a single list"""
   flat = []
   queue = nested[:]
   while len(queue) > 0:
       item = queue.pop(0)
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
