
# Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError.
#Обрабатываем ошибку, говорим пользователю, в чем его ошибка

vvod = input('Введите любое число:')
n = int(vvod)
try:
    if n < 0:
        raise TypeError ('Число меньше нуля')
    if n > 10:
        raise IndexError ('Число больше десяти')
    if n % 2 == 0:
        raise ValueError ('Число четное')
except TypeError :
    print('Число меньше нуля')
except IndexError :
    print('Число больше десяти')
except ValueError :
	print('Число четное')

# Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть.
# Если все хорошо - пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так

list = ['qwу', '2838', 'us']
try:
	znachenie = input ('Enter index: ')
	x = int(znachenie)
	if x >= 0:
		if x >= len(list):
			raise IndexError ('Не верный ввод')
		print (list[x])
except IndexError:
	print ('Не верный ввод')
except ValueError:
	print ('Некоректный ввод')

# Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму.
#Если оба меньше - разность. Если знаки разные - возвращаем 0

def function (z, y):
	if z > 0 and y > 0:
		return z + y
	if z < 0 and y < 0:
		return z - y
	if z < 0 and y > 0:
		return 0
	if z > 0 and y < 0:
		return 0
print (function(5, -3))

# Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль

def my_function (m, w, h):
	lst = [m, w, h]
	lst.sort()
	print(lst[1],lst[2])
my_function(8, 5, 10)

# Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с четными числами из входного списка

def my_function2 (*numbers,flag):
	if flag:
		return list_num1
		print(my_function2)
	else:
		return list_num2
	print(my_function2)

def my_function3(*numbers,flag):
	list_num1 = []
	if flag == False:
		for number in numbers:
			if number % 2 == 0:
				list_nim1.append(number)
	return list_num1

def function2(*numbers, flag):
	list_num2 = []
	if flag == True:
		if number1 % 2 != 0:
			list_num2.append(number1)
	return list_num2

#     Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное. И возвращает оба

def my_function4(*number):
    list = []
    list.append(max(number))
    list.append(min(number))
    return list
print(my_function4(1, 2, 3, 4, 10))

#Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему

def fun(string, case = True):
    if case:
        return string.upper()
    else:
        return string.lower()
    print(fun('Hello ', True))

#Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер по-умолчанию glue, который равен ':'.
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. Для соединения между любых двух строк вставлять glue
def fun(*strings, glue=':'): #b
    list = []
    for string in strings: #begin
        if len(string) > 3: #b
            list.append(string)
        #end
    #e
    return glue.join(list)

 #end
print(fun('hello','www','re','good'))
