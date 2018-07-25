import random 
a = input('please enter your lower range: ')
b = input('please enter your upper range: ')
a = int(a)
b = int(b)
r = random.randint(a, b)
i = 0
while True:
	i = i + 1 #same as: i += 1
	print('this is your ', i, 'try')
	num = input('please guess number: ')
	num = int(num)
	if num == r:
		print('you got it right!')
		print('this is your', i, 'try')
		break
	elif num > r:
		print('your number is bigger than actual')
	else:
		print('your number is smaller than actual')
 