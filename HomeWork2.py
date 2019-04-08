# Создать лист из 6 цифр и отсортировать его по возрастанию

list = [12, 33, 9, 3, 45, 21]
list.sort()
print(list)

# Создать словарь из пяти пар: int->str, например {6: '6'}, вывести его в консоль попарно

favorite_games = {'Half Life':'Mr.Freeman','S.T.A.L.K.E.R.':'Mechenij','Metro2033':'Artem', 'War Thunder':'BoBa_KaMukag3e'}
games = favorite_games.keys()
pers = favorite_games.values()
print (favorite_games)

for key, value in favorite_games.items():
	print(key+ " -> " + value)

#for key in favorite_games.keys():
	#print(key + " -> " +favorite_games[key])


# Создать tuple (кортеж) из десяти любых дробных чисел,  найти макс. и мин. значение в нём

kortej = (1.4, 2.3, 5.3, 1.2, 3.6)
print(max(kortej))
print(min(kortej))

# Создать лист из трёх слов ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'

list = ['Earth', 'Russia', 'Moscow']
result = list[0]
n = len(list)

for i in range(1, n):
	result = result+ ' ' + list[i]
print(result)

# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить её в список по символу ':'

stroka = '/bin:usr/bin:/usr/local/bin'.split(':')
print(stroka)

# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

result = str()
for i in range(0, 101):
	if 0 == i % 7:
		result = result + ' ' +str(i)
		print (i)
		print (result)

# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

matrix = [[0, 1, 2, 3],[4, 5, 6, 7], [8, 9, 4, 9]]
print(matrix[0])
print(matrix[1])
print(matrix[2])

for row in matrix:
	for elem in row:
		print(elem, end= ' ')
	#print()

# Создать список с тремя значениями 'to-delete' и несколькими любыми другими, удалить из него все значения 'to-delete'

spisok = ['to-delete', 'to-delete', 'to-delete', '123', 'abc', 'if']
while 'to-delete' in spisok:
	spisok.remove('to-delete')
	print(spisok)

# Пройти по всем числам от 1 до 10  в обратную сторону (10-1), напечатать их в консоль

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = ''
n = len(x)

for i in range(n):
	j = -i - 1
	r = r + ' ' + str(x[j])
print(r)

