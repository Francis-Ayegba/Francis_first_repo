def count_up_to(limit):
	"""Yield integers from 1 through limit."""
	number = 1
	while number <= limit:
		yield number
		number += 1


print("Counting up to 5:")
for num in count_up_to(5):
    print(num)  


# this is my first comment in this repo
