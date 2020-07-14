


 1, 1 ==> 2

 1, 1, 2, 3, 5, 8, 13, 21, 34

 write a function fib that takes an int and returns the int-th digit of fib seq.

 fib(0) => 1
 fib(4) => 5


params around index max


create a list with 1, 1
for number of times equal to the index
add the last two numbers and append the sum

return the value at the index called


def fib_fun(my_int):
	fib_list = [1, 1]

	for num in range(my_int-1):
		new_num = fib_list[-1] + fib_list[-2]
		fib_list = [fib_list[-2], fib_list[-1], new_num]

	return fib_list[-1]


fib_fun(3) => 3


fib_list = [1, 1, 2, 3, 5]


num = 


new_num = 5


version with O(n) for runtime and O(1) on memory
recursive version --> time and memory complexity?

which approach?

recursive version
---
fib_seq(index)
counter = index
while counter > 0 base case = index is reached (int minus 1)

if not lst:
		list = [1, 1]
else:
	take the last two items of list and add together
	decrease counter
	return curr_list, index



----
def fib(n)
	if n <= 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
