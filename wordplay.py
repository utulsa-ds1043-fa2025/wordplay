import timeit
import sys
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
    positions: list[int] = [0, 0]  # Keeps track of current position in a and b
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
    return seq[1:-1]  # the [] operator with a slice creates a new object


def chop(seq: list) -> None:
    "Removes the first and last elements of seq"
    seq.pop(0)   # seq refers to a list in memory
    seq.pop(-1)  # calling seq.pop modifies that list
    return


def is_sorted(seq: list) -> bool:
    "Tests whether the sequence is sorted in ascending order"
    # Compare element 0 with element 1, element 1 with element 2, etc (n-1 comparisons)
    # Since we are comparing the current element with the next element,
    # only iterate through the first n-1 elements to avoid an IndexError
    for index, element in enumerate(seq[:-1]):
        if element > seq[index + 1]:
            return False
    return True


def reverse_pairs(words: Collection[str]) -> list[tuple[str]]:
    "Find all pairs of words which are reverse-related"
    pairs: list[tuple[str]] = []
    for word in words:  # we do this block n times
        # We can search for an item in a collection using `in`
        # If words is a list, `in` takes ~n operations
        # If words is a set, `in` takes ~1 operation
        if word[::-1] in words:
            pairs.append((word, word[::-1]))
    return pairs


def reverse_pairs_list(words: list[str]) -> list[tuple[str]]:
    "Find all pairs of words which are reverse-related"
    pairs = []
    ops = 0
    for index, word in enumerate(words):  # we do this block n times
        # This block mimics the in/contains operator #
        for candidate in words:
            ops += 1
            if word[::-1] == candidate:
        ##############################################
                pairs.append((word, word[::-1]))
                break
    print(f'Total Comparisons = {ops}')
    return pairs


def reverse_pairs_set(words: set[str]) -> list[tuple[str]]:
    "Find all pairs of words which are reverse-related"
    ops = 0
    pairs = []
    for word in words:  # we do this block n times
        ops += 1
        # We can search for an item in a collection using `in`
        if word[::-1] in words:  # This is one operation
            pairs.append((word, word[::-1]))
    print(f'Total Comparisons = {ops}')
    return pairs


def compare_list_set_search(filename: str) -> None:
    """Uses timeit to compare the performance of searching lists and sets using the `in` operator"""
    word_list: list[str] = []
    word_set: set[str] = set()
    with open(filename, 'r', encoding='utf-8') as wordfile:
        for word in (line.strip() for line in wordfile):
            word_list.append(word)
            word_set.add(word)
    print('WARNING: This may take a few minutes!')
    list_time = timeit.timeit(f"reverse_pairs({word_list})",
                              globals=globals(),
                              number=2)
    set_time = timeit.timeit(f"reverse_pairs({word_set})",
                             globals=globals(),
                             number=2)
    print("| data structure | elements | memory used (B) | search time (s) |")
    print("|----------------|----------|-----------------|-----------------|")
    print(f'| list           | {len(word_list):>8} | {sys.getsizeof(word_list):>15} | {list_time:>15} |')
    print(f'| set            | {len(word_set):>8} | {sys.getsizeof(word_set):>15} | {set_time:>15} |')
