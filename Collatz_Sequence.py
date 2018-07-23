# The Collatz Sequence
#is even, then collatz() should print number // 2 and return this #value. If number is odd, then collatz() should print and return 3 * number + 1.

print('Please enter a integer to test the Collatz Sequence:')
try:
	user_input = int(input())
except ValueError:
	print('Please enter an integer.')


def collatz(number):
	print(user_input)
	while user_input != 1:
		if(user_input % 2 == 0):
			user_input = (user_input // 2)
			print(user_input)
		else:
			user_input = (user_input * 3) + 1
			print(user_input)
	return;
	
collatz(user_input)