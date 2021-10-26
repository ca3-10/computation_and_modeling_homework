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