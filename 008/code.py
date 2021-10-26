def merge_sorted_lists(a, b):
    result = []
    total_length = len(a) + len(b)
    a_index = 0
    b_index = 0
    while total_length > len(result):
        if a_index == len(a):
            result += b[b_index:]
            break
        elif b_index == len(b):
            result += a[a_index:]
        elif a[a_index] < b[b_index]:
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1
    return result


def merge_sort(input_list): 

        half_index = len(input_list) // 2 

        first_half = input_list[:half_index]
        second_half = input_list[half_index:]

        if len(first_half) == 1 or len(second_half) == 1:
            return merge_sorted_lists(first_half, second_half)

        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        return merge_sorted_lists(sorted_first_half, sorted_second_half)
        
