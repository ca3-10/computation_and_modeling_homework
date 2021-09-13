from helperfunctions import *

def swap_sort(numbers):
    sorted = False
    while not sorted:
        sorted = True
        for nums in range(0, len(numbers) - 1):
            if numbers[nums] > numbers[nums + 1]:
                numbers[nums], numbers[nums + 1] = numbers[nums + 1], numbers[nums]
                sorted = False
    return numbers

def tally_sort(numbers):
    minimum = calc_minimum(numbers)
    shifted_list = [num - minimum for num in numbers]
    tally = [0] * (calc_maximum(shifted_list) + 1)
    new_sorted = []

    for values in shifted_list: 
        tally[values] += 1

    for n in range(len(tally)):
        new_sorted.append([n] * tally[n])

    single_list = one_list(new_sorted)
    final_sorted_list = [i + minimum for i in single_list]

    return final_sorted_list

def card_sort(numbers):
    for i in range(1, len(numbers)):
        sorting_value = numbers[i]
         
        while i - 1 >= 0 and sorting_value < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1
    return numbers

  

