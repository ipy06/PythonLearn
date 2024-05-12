"""
This is a basic python program to determine if a number is prime or not.

"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

    
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

