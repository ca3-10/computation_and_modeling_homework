from code import check_for_symmetry
from code import convert_to_numbers
from code import convert_to_letters
from code import is_prime
from code import get_intersection
from code import get_union
from code import count_characters
from code import get_nth_terms_nonrecursive
from code import get_nth_term_recursive
from code import convert_to_base_ten
from code import convert_to_base_two

# from code import check_for_symmetry

if check_for_symmetry("racecar") is not True:
    print ('check_for_symmetry  failed  on  input  "racecar" ')
if check_for_symmetry("batman") is not False:
    print ('check_for_symmetry  failed  on  input  "racecar" ')
if check_for_symmetry("  @@#8#@@  ") is not True:
    print ('check_for_symmetry  failed  on  input  "  @@#8#@@  "')


# from code import convert_to_numbers
if convert_to_numbers("a cat") != [1, 0, 3, 1, 20]:
    print ('convert_to_numbers failed on input "a cat"')
if convert_to_numbers(" !! ") != "Error: only input spaces and lowercase letters":
    print ('convert_to_numbers failed on input "  !!  "')
if convert_to_numbers("R *#&R*#^^^&R") != "Error: only input spaces and lowercase letters":
    print ('convert_to_numbers failed on input "R *#&R*#^^^&R"')
if convert_to_numbers("Hello") != "Error: only input spaces and lowercase letters":
    print ('convert_to_numbers failed on input "Hello"')
if convert_to_numbers("supercalifragilisticexpialidocious") != [19, 21, 16, 5, 18, 3, 1, 12, 9, 6, 18, 1, 7, 9, 12, 9, 19, 20, 9, 3, 5, 24, 16, 9, 1, 12, 9, 4, 15, 3, 9, 15, 21, 19]:
    print ('convert_to_numbers failed on input "supercalifragilisticexpialidocious"')


# from code import convert_to_letters
if convert_to_letters([1, 2, 3, 26]) != "abcz":
    print("convert_to_letters failed for input [1, 12, 3, 4, 5, 16, 17, 26] ")
if convert_to_letters([1, 10, 11, -10]) != "Only numbers 0-26":
    print("convert_to_letters failed for input [1, 10, 11, -10]  ")
if convert_to_letters([1, 0, 11, 100]) != "Only numbers 0-26":
    print("convert_to_letters failed for input [1, 0, 11, 100] ")

# from code import is_prime
if is_prime(7) != "number is prime":
    print("is_prime failed for input 7")
if is_prime(25) != "number is not prime":
    print("is_prime failed for input 25 ")
if is_prime(16) != "number is not prime":
    print("is_prime failed for input 16")
if is_prime(81) != "number is not prime":
    print("is_prime failed for input 81")
if is_prime(31) != "number is prime":
    print("is_prime failed for input 31")

# from code import get_intersection
if get_intersection([1, 2, 3, 4, 5, 1], [1, 15, 20, 4, 50]) != [1, 4]:
    print ("get_intersection failed for input [1, 2, 3, 4, 5, 1], [1, 15, 20, 4, 50] ")
if get_intersection([1, 1, 2, 23, 34, 45, 67], [34, 67, 1, 1, 2, 4]) != [1, 2, 34, 67]:
    print ("get_intersection failed for input [1, 1, 2, 23, 34, 45, 67], [34, 67, 1, 1, 2, 4] ")

# from code import get_union
if get_union([1, 1, 3, 4, 56, 78, 10], [76, 8, 9, 0, 2, 1, 3]) != [1, 3, 4, 78, 10, 76, 8, 9, 0, 2]:
    print("get_union failed for input [1, 1, 3, 4, 78, 10], [76, 8, 9, 0, 2, 1, 3]")
if get_union([0, 0, 0, 0, 0], [0, 0, 0, 0]) != [0]:
    print("get_union failed for input ([0, 0, 0, 0, 0],[0, 0, 0, 0] ")


# from code import count_characters
if count_characters("a cat") != {'a': 2, ' ': 1, 'c': 1, 't': 1}:
    print('count_characters failed for input "a cat" ')
if count_characters("     aaaaabbbbbaa     ") != {' ': 10, 'a': 7, 'b': 5}:
    print('count_characters failed for input "     aaaaabbbbbaa     " ')
if count_characters("343434387878") != {'3': 4, '4': 3, '8': 3, '7': 2}:
    print('count_characters failed for input "343434387878" ')


# from code import get_nth_terms_nonrecursive
if get_nth_terms_nonrecursive(9) != [5, 11, 29, 83, 245, 731, 2189, 6563, 19685]:
    print("get_nth_terms_nonrecursive failed for input 9 ")
if get_nth_terms_nonrecursive(0) != "n >= 1 only":
    print("get_nth_terms_nonrecursive failed for input 0 ")
if get_nth_terms_nonrecursive(20) != [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051, 177149, 531443, 1594325, 4782971, 14348909, 43046723, 129140165, 387420491, 1162261469, 3486784403]:
    print("get_nth_terms_nonrecursive failed for input 20 ")


# from code import get_nth_term_recursive
if get_nth_term_recursive(0) != "n >= 1 only":
    print ("get_nth_term_recursive failed for input 0")
if get_nth_term_recursive(14) != 4782971:
    print ("get_nth_term_recursive failed for input 14 ")
if get_nth_term_recursive(7) != 2189:
    print ("get_nth_term_recursive failed for input 7 ")

# from code import convert_to_base_ten
if convert_to_base_ten(10) != 2:
    print("convert_to_base_ten failed for input 10 ")
if convert_to_base_ten(0) != 0:
    print("convert_to_base_ten failed for input 0 ")
if convert_to_base_ten(110110) != 54:
    print("convert_to_base_ten failed for input 110110 ")


# from code import convert_to_base_two
if convert_to_base_two(200) != "11001000":
    print ("convert_to_base_two failed for input 200 ")
if convert_to_base_two(54) != "110110":
    print ("convert_to_base_two failed for input 14 ")
if convert_to_base_two(0) != 0:
    print ("convert_to_base_two failed for input 0")
if convert_to_base_two(33) != "100001":
    print ("convert_to_base_two failed for input 33")
