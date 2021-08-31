from helperfunctions import convert_to_numbers

def encode(string, a, b):
    trivial_encode = convert_to_numbers(string)
    linear_encode = []
    for nums in trivial_encode: 
        linear_encode.append(nums * a + b)
    return linear_encode
