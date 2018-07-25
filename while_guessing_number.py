import random 
r = random.randint(1, 100)
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
 