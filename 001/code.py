def check_for_symmetry(input_string): 
    return input_string[::-1] == input_string

print (check_for_symmetry("racecar"))
print (check_for_symmetry("batman"))
print (check_for_symmetry("  @@#8#@@  "))

def convert_to_numbers(input_string): 
    alphabet = { " " : 0, "a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h": 8, "i": 9, "j": 10, "k":11, "l":12, "m":13, "n": 14, "o":15, "p": 16, "q":17, "r":18, "s": 19, "t": 20,"u": 21,"v": 22,"w": 23,"x": 24,"y":25,"z":26}
    input_string = list(input_string)
    number_list = []
    for letters in input_string: 
        if letters not in "abcdefghijklmnopqrstuvwxyz ":
            return ("Error: only input spaces and lowercase letters")
            break

        number_list.append(alphabet[letters])
    return number_list

print (convert_to_numbers("a cat"))
print (convert_to_numbers(" !! "))
print (convert_to_numbers("R *#&R*#^^^&R"))
print (convert_to_numbers("Hello "))
print (convert_to_numbers("supercalifragilisticexpialidocious"))




  




