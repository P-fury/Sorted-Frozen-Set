from itertools import islice
from timeit import timeit
from recaman import recaman
from sorted_frozen_set import SortedFrozenSet

# print(list(islice(recaman(), 50)))

s = SortedFrozenSet(r for r in islice(recaman(), 1000) if r < 1000)
print(len(s))
print(s)

print([s.count(i) for i in range(1000)])


result = timeit(setup='from __main__ import s',stmt='[s.count(i) for i in range(1000)]', number=200)
print(result)                                             