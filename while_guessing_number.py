import random 
r = random.randint(1, 100)

while True:
	num = input('please guess the number: ')
	num = int(num)
	if num == r:
		print('you got it right!')
		break
	elif num > r:
		print('your number is bigger than actual')
	else:
		print('your number is smaller than actual')
