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
    "Non-destructively merges two sorted lists"
    merged: list = []
    positions: list[int] = [0, 0] # Keeps track of current position in a and b
    # Walk through a and b, adding the smallest element at the current position
    # for each list
    while positions[0] < len(a) and positions[1] < len(b):
        if a[positions[0]] <= b[positions[1]]:
            merged.append(a[positions[0]])
            positions[0] += 1
        else:
            merged.append(b[positions[1]])
            positions[1] += 1
    # Add all remaining elements after all of one list is exhausted
    merged.extend(a[positions[0]:])
    merged.extend(b[positions[1]:])
    return merged


def flatten(nested: list[list]) -> list:
    "Flatten a nested list into a single list"
    flat: list = []
    # This example uses a queue (first in, first out)
    # Alternatively, it could use a stack (first in, last out)
    queue: list[list] = nested[:]
    while len(queue) > 0:
        # Queue -> take from front of list
        # Stack -> take from end of list
        item: list | object = queue.pop(0)
        # if the item is a list, we need to examine its elements
        # in case of additional layers of nesting
        if isinstance(item, list):
            queue.extend(item)
        else:
            flat.append(item)
    return flat


def nested_sum(nested: list[list[int]]) -> int:
    "Adds all integers in a set of nested lists"
    # 'lazy' approach is `return sum(flatten(nested))`
    total = 0
    for item in nested:
        total += sum(item)
    return total


def cumulative_sum(numbers: list[int]) -> list[int]:
    "Creates the cumulative sum for a sequence of integers"
    if len(numbers) == 0:
        return list()
    sums = [numbers[0]]
    # we can use the index from enumerate(numbers[1:]) to get the previous sum
    for index, number in enumerate(numbers[1:]):
        sums.append(sums[index] + number)
    # Alternatively, we could keep a running total
    # total = 0
    # for number in numbers:
    #     total += number
    #     sums.append(total)
    return sums


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
