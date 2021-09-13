
def calc_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def calc_maximum(numbers): 
    maximum = numbers[0]
    for num in numbers: 
        if num > maximum: 
            maximum = num
    return maximum

def one_list(new_sorted):
    single = []
    for elements in new_sorted:
        if type(elements) == list: 
            for element in elements:
                single.append(element)
    return single
                
        
