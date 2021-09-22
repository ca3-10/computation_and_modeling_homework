from code import *

#new_raph_root_calc
assert newt_raph_root_calc(2, 3, 100) == 1.2599210498948732
assert newt_raph_root_calc(1000, 3, 100) == 10

#merge_sort
assert merge_sort([1, 2, 5, 7], [0, 0, 4, 10]) == [0, 0, 1, 2, 4, 5, 7, 10]
assert merge_sort([-10, -2, 0, 1],[5, 7]) == [-10, -2, 0, 1, 5, 7]
assert merge_sort([0], [1]) == [0, 1]