from code import check_for_symmetry
print (check_for_symmetry("racecar"))
print (check_for_symmetry("batman"))
print (check_for_symmetry("  @@#8#@@  "))

from code import convert_to_numbers
print (convert_to_numbers("a cat"))
print (convert_to_numbers(" !! "))
print (convert_to_numbers("R *#&R*#^^^&R"))
print (convert_to_numbers("Hello "))
print (convert_to_numbers("supercalifragilisticexpialidocious"))

from code import convert_to_letters
print (convert_to_letters([1,12,3,4,5,16,17]))

from code import is_prime
print (is_prime(7))
print (is_prime(25))
print (is_prime(16))
print (is_prime(81))
print (is_prime(31))

from code import get_intersection
print (get_intersection([1, 2, 3,4,5,1], [1,15,20,4,50]))
print (get_intersection([1,1, 2, 23, 34, 45, 67], [34,67,1,1,2,4]))

from code import get_union
print (get_union([1,1,3,4,56,78,10], [76,8,9,0,2,1,3]))
print (get_union([0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,0]))

from code import count_characters
print (count_characters("a cat"))
print (count_characters("     aaaaabbbbbaa     "))
print (count_characters("343434387878"))
