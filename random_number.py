import random

numbers = []

for index in range(10):
	numbers.append(random.randint(1, 50))
	
print(numbers)


count = 0
for number in range(len(numbers)):
	count = count + 1
	
print("The length of the list is: " ,count)


sum_of_even = 0
for number in range(count):
	if number % 2 == 0:
		sum_of_even += numbers[number]
		
print("The sum of even numbers in the list is: " ,sum_of_even)

sum_of_odd = 0
for number in range (count):
	if number % 2 != 0:
		sum_of_odd += numbers[number]
		
print("The sum of odd numbers in the list is: " ,sum_of_odd)


multiply = 1
for number in range (count):
	multiply *= numbers[number]
	
print("The sum of the multiplied number is: " , multiply)


largest_number = numbers[0]
for number in range(count):
	if number > largest_number:
		largest_number = number
print("The largest number of the element "largest_number)


smallest_number = numbers[0]
for number in range(count):
	if number < smallest_number:
		smallest_number = number
print("The smallest element in the index: " ,smallest_number)




