# Игра "угадай число"

import random

num_x = random.randint(1, 10)
name = input('Как вас зовут? ')
num_i = input('Нажмите Enter для начала игры')
while num_i != num_x:
	num_i = int(input('Введите число от 1 до 10: '))
	if num_x == num_i:
		print('Вы угадали,',name,'!')
		break
	elif num_i > num_x:
		print('Вы загадали слишком большее число')
	elif num_i < num_x:
		print('Вы загадали слишком маленькое число ')

