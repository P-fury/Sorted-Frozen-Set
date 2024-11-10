from sorted_frozen_set import SortedFrozenSet


def test_construct_empty_list():
    SortedFrozenSet([])


def test_construct_from_not_empty_list():
    SortedFrozenSet([7, 8, 3, 1])


def test_construct_with_no_args():
    SortedFrozenSet()


def test_construct_from_iterator():
    items = [7, 8, 3, 1]
    iterator = iter(items)
    SortedFrozenSet(iterator)
