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
    # positions = [0, 0] # index 0 corresponds to a, index 1 corresponds to b --- do this for lab 6
    while len(a) > 0 and len(b) > 0: # find another way to do this that doesn't remove items from the lists
    # while positions[0] < len(a) and positions[1] < len(b)
        if a[0] <= b[0]:
            merged.append(a.pop(0))
            # change pop to something that won't destroy a
            # if a[positions[0]] <= b[positions[1]]
                # if a in positions at index 0 is less than b in positions at index 1
                    # (a is at index 0, b is at index 1 [in positions])
                # merged.append(a[positions[0]])
                    # append to merged: a[index value at positions[0] (index 0 in positions)]
            # positions[0] += 1
                # add 1 to positions at index 0 -- it will check the next index of a, since the 0 index of a has already been used
        else:
            merged.append(b.pop(0))
            # merged.append(b[positions[1]])
            # positions[1] += 1
    merged.extend(a)
    # merged.extend(a[positions[0]:])
    merged.extend(b)
    # merged.extend(b[positions[1]:])
    # one of the lists will be destroyed, and the other list will be extended onto the head of the merged list we started to make
    return merged

# merged = []
#     while len(a) > 0 and len(b) > 0:
#         if a[0] <= b[0]:
#             merged.append(a.pop(0))
#         else:
#             merged.append(b.pop(0))
#     merged.extend(a)
#     merged.extend(b)
#     # one of the lists will be destroyed, and the other list will be extended onto the head of the merged list we started to make
#     return merged


def flatten(nested: list[list]) -> list:
    """Flatten a nested list into a single list"""
    flat = []
    queue = nested[:]
    # put everything in nested into a list called stack
    while len(queue) > 0:
        item = queue.pop(0)
            # take things off the front of the list, rather than the (stack)
        if isinstance(item, list):
        # for the item popped off the stack
        # is the item a list
            queue.extend(item)
            # add all the elements in the list to stack
        else:
            flat.append(item)
        # if the item is not a list, add it to the empty list flat
    return flat

    return []


def nested_sum(nested: list[list[int]]) -> int:
    """Adds all integers in a set of nested lists"""
    return 0


def cumulative_sum(numbers: list[int]) -> list[int]:
    """Creates the cumulative sum for a sequence of integers"""
    return [0] * len(numbers)


def middle(seq: list) -> list:
    """Creates a new list that contains all but the first and last elements of seq"""
    return seq


def chop(seq: list) -> None:
    """Removes the first and last elements of seq"""
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
