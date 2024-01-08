import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

random_numbers_1000 = [random.randint(1, 100) for _ in range(1000)]
random_numbers_5000 = [random.randint(1, 100) for _ in range(5000)]


print("Merge sort time for length     1000: {:>28}"
      .format(timeit.timeit(lambda: merge_sort(random_numbers_1000.copy()), number=5)))
print("Insertion sort time for length 1000: {:>28}"
      .format(timeit.timeit(lambda: insertion_sort(random_numbers_1000.copy()), number=5)))
print("Timsort sort time for length   1000: {:>28}"
      .format(timeit.timeit(lambda: random_numbers_1000.sort(), number=5)))
print("\nMerge sort time for length     5000: {:>28}"
      .format(timeit.timeit(lambda: merge_sort(random_numbers_5000.copy()), number=5)))
print("Insertion sort time for length 5000: {:>28}"
      .format(timeit.timeit(lambda: insertion_sort(random_numbers_5000.copy()), number=5)))
print("Timsort sort time for length   5000: {:>28}"
      .format(timeit.timeit(lambda: random_numbers_5000.sort(), number=5)))

# Як видно з результатів роботи, вище вказані функції витрачають на сортування різний час роботи.

# Найдовше сортує алгоритм сортування Insertion sort, особливо коли довжина списку 5000 елементів (більше 7 секунд)

# На другому місці алгоритм сортування Merge sort.

# Найшвидше працює алгоритм сортування Timsort, який поєднує у собі два вищевказаних алгоритми.
