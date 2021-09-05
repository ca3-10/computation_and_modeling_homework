from helperfunctions import convert_to_numbers
from helperfunctions import convert_to_letters

def encode(string, a, b):
    trivial_encode = convert_to_numbers(string)
    linear_encode = []
    for nums in trivial_encode: 
        linear_encode.append(nums * a + b)
    return linear_encode


def decode(number, a, b):
    basic_list = []
    for nums in number:
        basic_list.append((nums - b)/a)
    if max(basic_list) >= 27:
        return False
    return convert_to_letters(basic_list)


def calc_nth_root(num,root,presicion):
    upper_bound = num
    lower_bound = 0
    while presicion > 0: 
        guess = (upper_bound + lower_bound)/2
        if guess ** root < num: 
            lower_bound = guess 
        elif guess ** root > num:
            upper_bound = guess
        presicion -= 1 
    return guess


def calc_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def simple_sort(numbers):
    sorted_list = []
    while len(numbers) > 0:
        miniMum = calc_minimum(numbers)
        sorted_list.append(miniMum)
        numbers.remove(miniMum)
    return sorted_list


class Stack:
    def __init__(self):
      self.elements = []
    
    def print(self):
        print(self.elements)

    def push(self,value):
        self.elements.append(value)
    
    def pop(self):
        self.elements.pop()


class Queue: 
    def __init__(self):
        self.items = []
    
    def print(self):
        print(self.items)

    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        self.items.pop(0)


