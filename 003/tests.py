from code import *

# swap_sort
assert swap_sort([1, 5, 6, 40, 41, 3, 9]) == [1, 3, 5, 6, 9, 40, 41]
assert swap_sort([0, 0, 0, 1, 0, 1]) == [0, 0, 0, 0, 1, 1]
assert swap_sort([6, 5, 10, 11, 1, 0, 0]) == [0, 0, 1, 5, 6, 10, 11]

# tally_sort
assert tally_sort([1, 3, 2, 3, 4, 6, 4]) == [1, 2, 3, 3, 4, 4, 6]
assert tally_sort([0, -4, 10, 20, 7]) == [-4, 0, 7, 10, 20]
assert tally_sort([-1, 0, -20, 7, 5, 18, 20]) == [-20, -1, 0, 5, 7, 18, 20]

# card_sort
assert card_sort([20, 19, 0, 1, 4, -5, 7, 8, 10, -10]) == [-10, -5, 0, 1, 4, 7, 8, 10, 19, 20]
assert card_sort([0, 0, 0, -1, -1, -2]) == [-2, -1, -1, 0, 0, 0]
assert card_sort([-1, -10, 0, 9, 12, 5]) == [-10, -1, 0, 5, 9, 12]