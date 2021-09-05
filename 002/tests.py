from code import *

# encode 
assert encode("a i am sam",1,0) == [1,0,9,0,1,13,0,19,1,13]
assert encode("eurisko",10,7) == [57, 217, 187, 97, 197, 117, 157]
assert encode("be more chill",4,5) == [13, 25, 5, 57, 65, 77, 25, 5, 17, 37, 41, 53, 53]

#decode
assert decode([13, 25, 5, 57, 65, 77, 25, 5, 17, 37, 41, 53, 53], 4, 5) == "be more chill"
assert decode([57, 217, 187, 97, 197, 117, 157],10,7) == "eurisko"
assert decode([1,0,9,0,1,13,0,19,1,13],1,0) == "a i am sam"
assert decode( [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71,377, 547, 717, 751, 683, 785, 513, 241, 547, 751],34,71) == "is mayonnaise an instrument"
## found because 547 is the most repeating, and 71 is the lowest


#calc_nth_root
assert calc_nth_root(3,2,20) == 1.7320489883422852 
assert calc_nth_root(8,3,5) == 2
assert calc_nth_root(27,4,50) == 2.279507056954798


#calc_minimum 
assert calc_minimum([0,3,45,6,0,1]) == 0
assert calc_minimum([100,32,1,2,3]) == 1
assert calc_minimum([101,103,50,40,200]) == 40

#simple_sort 
assert simple_sort([10,9,60,88,100,4]) == [4,9,10,60,88,100] 
assert simple_sort([0,3,45,6,0,1]) == [0,0,1,3,6,45]
assert simple_sort([9,9,9,9,9]) == [9,9,9,9,9]

#stack
stack = Stack()
stack.push(1)
stack.push("some")
stack.push(2)
stack.push("stack")
stack.pop()
stack.push(5)
#assert stack.print == [1, 2, 'some', 5]

#queue
ex_queue = Queue()
ex_queue.enqueue(1)
ex_queue.enqueue(4)
ex_queue.enqueue(5)
ex_queue.dequeue()
ex_queue.enqueue(6)
ex_queue.enqueue(7)
ex_queue.dequeue()
#assert ex_queue.print() == [5, 6, 7]

