def check_for_symmetry(input_string):
    return input_string[::-1] == input_string


def convert_to_numbers(input_string):
    alphabet = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
                "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
                "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
                "y": 25, "z": 26}
    input_string = list(input_string)
    number_list = []
    for letters in input_string:
        if letters not in "abcdefghijklmnopqrstuvwxyz ":
            return ("Error: only input spaces and lowercase letters")
            break

        number_list.append(alphabet[letters])
    return number_list


def convert_to_letters(input_array):
    numbers_to_letters_dict = {0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e",
                               6: "f", 7: "g", 8: "h", 9: "i", 10: "j",
                               11: "k", 12: "l", 13: "m", 4: "n", 15: "o",
                               16: "p", 17: "q",  18: "r", 19: "s", 20: "t",
                               21: "u", 22: "v", 23: "w", 24: "x", 25: "y",
                               26: "z"}

    word_list = []
    word = ""

    for numbers in input_array:
        if numbers > 27 or numbers < 0:
            return "Only numbers 0-26"
            break
        word_list.append(numbers_to_letters_dict[numbers])
    return (word.join(word_list))


def is_prime(n):
    for numbers in range(2, n):
        if n % numbers == 0:
            return "number is not prime"
        elif n == numbers + 1:
            return "number is prime"


def get_intersection(list1, list2):
    intersecting_elements = []
    for elements in list1:
        if elements in list2:
            intersecting_elements.append(elements)
    return list(dict.fromkeys(intersecting_elements))


def get_union(list1, list2):
    combined_list = list1
    for elements in list2:
        combined_list.append(elements)
    return list(dict.fromkeys(combined_list))


def count_characters(input_string):
    char_counter = {}
    for elements in input_string:
        if elements in char_counter.keys():
            char_counter[elements] += 1
        else:
            char_counter[elements] = 1
    return char_counter


def get_nth_terms_nonrecursive(n):
    a_1 = 5
    a_2 = 0
    nth_terms = [a_1]
    if n == 0:
        return "n >= 1 only"
    for n in range(1, n):
        a_2 = 3*a_1 - 4
        nth_terms.append(a_2)
        a_1 = a_2
        a_2 = 0
    return nth_terms


def get_nth_term_recursive(n):
    if n == 0:
        return "n >= 1 only"
    if n == 1:
        return 5
    return (3 * get_nth_term_recursive(n-1)) - 4


def convert_to_base_ten(binary):
    reverse_binary_list = list((str(binary)[::-1]))
    reverse_int_list = [int(x) for x in reverse_binary_list]
    for num in range(0, len(reverse_int_list)):
        if reverse_int_list[num] == 1:
            reverse_int_list[num] = 2 ** num
    return sum(reverse_int_list)


def convert_to_base_two(binary):
    binary_list = []
    if binary == 0:
        return 0
    while binary > 0:
        if binary % 2 == 0:
            binary_list.append(0)
            binary = binary // 2
        else:
            binary_list.append(1)
            binary = binary // 2
    binary_list = binary_list[::-1]
    binary_str = "".join([str(n) for n in binary_list])
    return binary_str

