#solution to problem 6
def fibonacci_iterative(num=10):
	fib_list = [1 ,2 ]
	#these two print statements are weird, the iterative solution is so weird
	print 1
	print 2
	for x in range(0, num-2):
		
		print fib_list
		fib1 = fib_list.pop()
		fib2 = fib_list.pop()
		fib3 = fib1 + fib2
		print fib3
		
		fib_list.append(fib1)
		fib_list.append(fib3)


#fibonacci_iterative(7)


#solution to problem 7
def factorial_recursive(num):
	if(num == 0):
		return 1
	else:
		return num * factorial_recursive(num - 1)

#print factorial_recursive(3)