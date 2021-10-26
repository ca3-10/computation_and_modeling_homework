from helper_functions import *

def merge_sort(input_list): 

        half_index = len(input_list) // 2 

        first_half = input_list[:half_index]
        second_half = input_list[half_index:]

        if len(first_half) == 1 or len(second_half) == 1:
            return merge_sorted_lists(first_half, second_half)

        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        return merge_sorted_lists(sorted_first_half, sorted_second_half)
        
