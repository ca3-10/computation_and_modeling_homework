

def newt_raph_root_calc(number, root, presicion):
    x_0 = number/2
    x_n = x_0
    while presicion > 0:
        function = (x_n ** root) - number 
        prime_function = root * (x_n ** (root -1))
        x_k = x_n - (function / prime_function)
        x_n = x_k
        presicion -= 1
    return x_k

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